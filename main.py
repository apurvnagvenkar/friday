from data_architecture.call_entity_data import get_entities_for_intent
from data_architecture.data_model import data_model
from lib.api.lib.answer_api import AnswerApi
from lib.api.lib.question_api import QuestionApi
from lib.api.lib.verify_api import VerifyApi
from lib.entities import entities
from lib.entities.entities import Entity
from lib.intent.intent import Intent
from mongolib import get_user_conversation, update_user_conversation

__author__ = 'haptik'


####
# Run the entity detection
# Run the intent identification
def get_previous_info(user_id):
    intents = []
    domain = None
    users_position = 0
    unanswered_questions_by_user = 0
    count_of_bot_asked_questions = 0
    bots_intent = []
    bot_is_asking = False
    return intents, domain, users_position, unanswered_questions_by_user, count_of_bot_asked_questions, bots_intent, bot_is_asking


def run_june_1(msg, user_id, intents=[], domain=None, position_so_far=0, unanswered_questions_by_user=0,
               count_of_bot_asked_questions=0, bots_intent=[], bot_is_asking=False):
    # intents = []
    # domain = None
    # bot_is_asking = False
    # position_so_far = 0
    # unanswered_questions_by_user = 0
    # count_of_bot_asked_questions = 0
    # bots_intent = []
    bot_asking_dummy  = True
    entities = {}

    previous_intents = []
    previous_users_position = 0

    user_answered_bots_question = True

    users_position = -1

    threshold_to_increment_position_for_given_domain = 2
    number_of_questions_asked_for_that_domain = 0

    over_excited = True
    api_call = True

    threshold_of_bot_asking_questions = 2
    threshold_of_unanswerd_questions_by_user = 2

    response = []
    stop = False
    previous_intents, domain, position_so_far, unanswered_questions_by_user, count_of_bot_asked_questions, bots_intent, bot_is_asking, number_of_questions_asked, number_of_times_intent_called = get_previous_info_from_mongo(user_id)
    print '\t\t get_previous_info: \tprevious_intents: ', previous_intents, '\t domain: ', domain, '\t position_so_far: ', position_so_far, '\t unanswered_questions_by_user: ', unanswered_questions_by_user, '\tcount_of_bot_asked_questions:', count_of_bot_asked_questions, '\t bots_intent: ', bots_intent, '\t bot_is_asking: ', bot_is_asking,'\t number of quesitons asked: ', number_of_questions_asked, '\n\n'

    #############################################################
    entity_object = Entity(msg)
    entities = entity_object.run_entity_detector()
    print 'Entities %s ' % entities

    intent_object = Intent(msg)
    intents = intent_object.run_intent_identification()
    if intents:
        users_position = intent_object.position
        domain = intent_object.domain
        threshold_to_increment_position_for_given_domain = intent_object.threshold_to_increment_position_for_given_domain
        number_of_questions_asked_for_that_domain = number_of_questions_asked.get(domain, 0)
        number_of_questions_asked_for_that_domain += 1
        number_of_questions_asked[domain] = number_of_questions_asked_for_that_domain
        number_of_times_intent_called[intents[0]] = number_of_times_intent_called.get(intents[0], 0) + 1

    else:
        users_position = position_so_far

    print '\n\nDomain %s ' % (domain)
    print '\n\nIntents %s  --- Users Position %s ' % (intents, users_position)
    print '\t\t Threshold to increment for given domain: %s ' % (threshold_to_increment_position_for_given_domain)
    ##############################################################

    if bot_is_asking:
        print '\t\t bot asking is true'
        if bots_intent:
            intent = bots_intent[0]
            print 'bots intent %s ' % intent
            entities_found = get_entities_for_intent(intent, entities)
            print 'Entities found %s ' % entities_found
            verify = VerifyApi(msg=msg, domain=domain, intent=intent, entities=entities_found, user_id=user_id)
            if verify.response:
                response.extend(verify.response)
                bot_is_asking = False
                unanswered_questions_by_user -=2
                if unanswered_questions_by_user < 0:
                    unanswered_questions_by_user = 0
                print 'response from verification: %s' % response
                user_answered_bots_question = True
            else:
                user_answered_bots_question = False
    print '\t\t User answered bots question is %s ' % user_answered_bots_question
    print '\t\t Users position: %s \t position so far: %s  status: %s ' % (
    users_position, position_so_far, users_position <= position_so_far)

    if intents:
        if users_position <= position_so_far:
            print '\t\t calling answer api'
            answer = AnswerApi(msg=msg, domain=domain, intent=intents[0], entities=entities, user_id=user_id)
            response.extend(answer.response)
            bot_asking_dummy = False
            print '\t\t response from answer_api %s ' % response
            # call api
            # response
#            F, []
#            T,[]
#            T,[ddd]
#            T,[sdd]
            if len(intents) == 1 and not bot_asking_dummy:
                question = QuestionApi(msg=msg, domain=domain, intent=intents, entities=entities, user_id=user_id)
                response.extend(question.response)
                bots_intent = question.bot_intent
                bot_is_asking = True
            api_call = True

            if threshold_to_increment_position_for_given_domain == number_of_questions_asked_for_that_domain:
                print('\t\t Incrementing position since match in threshold_to_inc and number_of_questions')
                position_so_far += 1

            over_excited = False
        else:
            response.append( {'type': 'text','message':'Don t  get overexcited', 'stop':False})

            print ('response sent for overexcitment %s ' % response)
            # call overexcited_api
            over_excited = True

    if user_answered_bots_question is False and api_call is True:
        print 'user not answering bots question'
        response.append({'type':'text', 'message':'Why are you not answering my questions?', 'stop':False})
        unanswered_questions_by_user += 1
        intents = previous_intents
        print 'unanswered questions by user %s' % unanswered_questions_by_user
        print 'intent is set to previous %s ' % previous_intents
        # set current intent to previous intent

    if not intents:
        print '\t\tintents is set to None \t  bot is asking question'
        question = QuestionApi(msg=msg, domain=domain, intent=intents, entities=entities, user_id=user_id)
        if question.response:
            response.extend(question.response)
            bot_is_asking =True
            bots_intent = question.bot_intent
            # bot ask a question
            # send response
            count_of_bot_asked_questions += 1
            print '\t\t\t bots intent %s ' % bots_intent
            print  '\t\t\t response  %s ' % response
            print '\t\t\t count of bots question %s ' % count_of_bot_asked_questions

    if count_of_bot_asked_questions >= threshold_of_bot_asking_questions:
        print '\t\tYou are boring '
        response = []
        response.append({'type':'text','message':'You are so boring!!! and dont want to chat with you. Why always I have to ask question','stop':True})
        stop = True
    elif unanswered_questions_by_user >= threshold_of_unanswerd_questions_by_user:
        print 'You are not answering my questions'
        response = []
        response.append({'type': 'text', 'message':'You not answering my question. Bye!!!', 'stop':True})
        stop = True
    elif intents and number_of_times_intent_called[intents[0]] >= data_model[domain][intents[0]]['count']:
        response = []
        response.append({'type': 'text', 'message':'I am not dumb!! Why you asking same questions again and again?', 'stop':True})
        stop = True

    data = {
        'intents': intents,
        'domain': domain,
        'position_so_far': position_so_far,
        'unanswered_questions_by_user': unanswered_questions_by_user,
        'count_of_bot_asked_questions': count_of_bot_asked_questions,
        'bots_intent': bots_intent,
        'bot_is_asking': bot_is_asking,
        'user_id': user_id,
        'number_of_questions_asked': number_of_questions_asked,
        'number_of_times_intent_called': number_of_times_intent_called
    }
    print data
    store_previous_info_of_user(user_id, data)
    print intents, ',', domain, ',', position_so_far, ',', unanswered_questions_by_user, ',', count_of_bot_asked_questions, ',', bots_intent, ',', bot_is_asking

    if not response:
        if 'sorry'in msg.lower():
            response.append({'type': 'text', 'message':'Its okay', 'stop':stop })
        elif 'how are you' in msg.lower() or 'how are u' in msg.lower() or'how r u' in msg.lower():
            response.append({'type': 'text', 'message':'I am fine!!!', 'stop':stop })
        else:
            response.append({'type': 'text', 'message':'Didnt get it', 'stop':stop })

    return response


def get_previous_info_1(intents, domain, position_so_far, unanswered_questions_by_user, count_of_bot_asked_questions,
                        bots_intent, bot_is_asking):
    return intents, domain, position_so_far, unanswered_questions_by_user, count_of_bot_asked_questions, bots_intent, bot_is_asking


def get_previous_info_from_mongo(user_id):
    intents = []
    domain = None
    position_so_far = 0
    unanswered_questions_by_user = 0
    count_of_bot_asked_questions = 0
    bots_intent = []
    bot_is_asking = False
    number_of_questions_asked = {}
    number_of_times_intent_called = {}
    json_data = get_user_conversation(user_id)
    print 'Json %s ' % json_data
    if json_data:
        data = json_data
        intents = data['intents']
        domain = data['domain']
        position_so_far = data['position_so_far']
        unanswered_questions_by_user = data['unanswered_questions_by_user']
        count_of_bot_asked_questions = data['count_of_bot_asked_questions']
        bots_intent = data['bots_intent']
        bot_is_asking = data['bot_is_asking']
        number_of_questions_asked = data['number_of_questions_asked']
        number_of_times_intent_called = data['number_of_times_intent_called']
    return intents, domain, position_so_far, unanswered_questions_by_user, count_of_bot_asked_questions, bots_intent, bot_is_asking, number_of_questions_asked, number_of_times_intent_called


def store_previous_info_of_user(user_id, data):
    update_user_conversation(user_id, data)


# if bot is asking:
#  if entity is present for that question
# Reply Check verification
# answerd_flag =True
#   else:
# answerd_flag = False




# If position of domain is > current position
# over_excited = True
# else:
# call api_functionality
# api_call = True
# response
# increment position

# if answerd_flag ==  False and api_call=True
# why you not answering my question?
# unanswered_question +=1
# set current domain to prevous intent


# if intent is not changed
# bot ask a question
# send response
# ask_question +=1


# if ask_question > threshold?
# you are boring me dont want to chat with you Why always i have to ask a question
# if unanswered _question >  threshold?
# why you not answering my questions?


""""
[

    {
        type: 'text',
        message: ''
    }
]
"""""
