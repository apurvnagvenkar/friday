from data_architecture.call_entity_data import get_entities_for_intent
from lib.api.lib.answer_api import AnswerApi
from lib.api.lib.question_api import QuestionApi
from lib.api.lib.verify_api import VerifyApi
from lib.entities import entities
from lib.entities.entities import Entity
from lib.intent.intent import Intent

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




def run_june(msg, user_id):
    entities = {}
    intents = []
    domain = None

    previous_intents = []
    previous_users_position = 0

    bot_is_asking = False
    user_answered_bots_question = True

    position_so_far = 0
    users_position = -1

    threshold_to_increment_position_for_given_domain = 2
    number_of_questions_asked_for_that_domain = 0

    over_excited = True
    api_call = True
    unanswered_questions_by_user = 0
    count_of_bot_asked_questions = 0

    threshold_of_bot_asking_questions = 5
    threshold_of_unanswerd_questions_by_user = 5

    bots_intent = []
    response = []
    previous_intents, domain, position_so_far, unanswered_questions_by_user, count_of_bot_asked_questions, bots_intent, bot_is_asking = get_previous_info(user_id)
    print '\t\t get_previous_info: \tprevious_intents: ', previous_intents, '\t domain: ', domain, '\t position_so_far: ', position_so_far, '\t unanswered_questions_by_user: ', unanswered_questions_by_user, '\tcount_of_bot_asked_questions:', count_of_bot_asked_questions, '\t bots_intent: ', bots_intent,'\t bot_is_asking: ', bot_is_asking ,'\n\n'

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
        number_of_questions_asked_for_that_domain +=1
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
            response.append(verify.response)
            print 'response from verification: %s' % response
        # if entity is present for that question
        # Reply Check verification
        user_answered_bots_question = True
    else:
        user_answered_bots_question = False
    print '\t\t User answered bots question is %s ' % user_answered_bots_question
    print '\t\t Users position: %s \t position so far: %s  status: %s ' % (users_position, position_so_far, users_position <= position_so_far )
    if users_position <= position_so_far:
        print '\t\t calling answer api'
        answer = AnswerApi(msg=msg, domain=domain, intent=intents[0], entities=entities, user_id=user_id)
        response.append(answer.response)
        print '\t\t response from answer_api %s ' % response
        # call api
        # response

        api_call = True

        if threshold_to_increment_position_for_given_domain == number_of_questions_asked_for_that_domain:
            print( '\t\t Incrementing position since match in threshold_to_inc and number_of_questions')
            position_so_far += 1

        over_excited = False
    else:
        response.append({'type': 'text', 'message': 'Don t  get overexcited', 'stop': False})
        print ('response sent for overexcitment %s ' % response)
        # call overexcited_api
        over_excited = True

    if user_answered_bots_question is False and api_call is True:
        print 'user not answering bots question'
        response.append({'type': 'text', 'message': 'Why are you not answering my questions?', 'stop': False})
        unanswered_questions_by_user += 1
        intents = previous_intents
        print 'unanswered questions by user %s' % unanswered_questions_by_user
        print 'intent is set to previous %s ' % previous_intents
        # set current intent to previous intent

    if intents is None:
        print '\t\tintents is set to None \t  bot is asking question'
        question = QuestionApi(msg=msg, domain=domain, entities=entities, user_id=user_id)
        if question.response:

            response.append(question.response)

            bots_intent = question.bot_intent
            # bot ask a question
            # send response
            count_of_bot_asked_questions += 1
            print '\t\t\t bots intent %s ' % bots_intent
            print  '\t\t\t response  %s ' % response
            print '\t\t\t count of bots question %s ' % count_of_bot_asked_questions

    if count_of_bot_asked_questions >= threshold_of_bot_asking_questions:
        print '\t\tYou are boring '
        response.append({'type': 'text',
                         'message': 'You are so boring!!! and dont want to chat with you. Why always I have to ask question',
                         'stop': True})
    elif unanswered_questions_by_user >= threshold_of_unanswerd_questions_by_user:
        print 'You are not answering my questions'
        response.append({'type': 'text', 'message': 'You not answering my question. Bye!!!', 'stop': True})

    return response




def run_june_1(msg, user_id, intents=[], domain=None, position_so_far=0, unanswered_questions_by_user=0, count_of_bot_asked_questions=0, bots_intent=[], bot_is_asking=False):
    entities = {}
    intents = []
    domain = None

    previous_intents = []
    previous_users_position = 0

    bot_is_asking = False
    user_answered_bots_question = True

    position_so_far = 0
    users_position = -1

    threshold_to_increment_position_for_given_domain = 2
    number_of_questions_asked_for_that_domain = 0

    over_excited = True
    api_call = True
    unanswered_questions_by_user = 0
    count_of_bot_asked_questions = 0

    threshold_of_bot_asking_questions = 5
    threshold_of_unanswerd_questions_by_user = 5

    bots_intent = []
    response = []
    previous_intents, domain, position_so_far, unanswered_questions_by_user, count_of_bot_asked_questions, bots_intent, bot_is_asking = get_previous_info(user_id)
    print '\t\t get_previous_info: \tprevious_intents: ', previous_intents, '\t domain: ', domain, '\t position_so_far: ', position_so_far, '\t unanswered_questions_by_user: ', unanswered_questions_by_user, '\tcount_of_bot_asked_questions:', count_of_bot_asked_questions, '\t bots_intent: ', bots_intent,'\t bot_is_asking: ', bot_is_asking ,'\n\n'

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
        number_of_questions_asked_for_that_domain +=1
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
            response.append(verify.response)
            print 'response from verification: %s' % response
        # if entity is present for that question
        # Reply Check verification
        user_answered_bots_question = True
    else:
        user_answered_bots_question = False
    print '\t\t User answered bots question is %s ' % user_answered_bots_question
    print '\t\t Users position: %s \t position so far: %s  status: %s ' % (users_position, position_so_far, users_position <= position_so_far )
    if users_position <= position_so_far:
        print '\t\t calling answer api'
        answer = AnswerApi(msg=msg, domain=domain, intent=intents[0], entities=entities, user_id=user_id)
        response.append(answer.response)
        print '\t\t response from answer_api %s ' % response
        # call api
        # response

        api_call = True

        if threshold_to_increment_position_for_given_domain == number_of_questions_asked_for_that_domain:
            print( '\t\t Incrementing position since match in threshold_to_inc and number_of_questions')
            position_so_far += 1

        over_excited = False
    else:
        response.append({'type': 'text', 'message': 'Don t  get overexcited', 'stop': False})
        print ('response sent for overexcitment %s ' % response)
        # call overexcited_api
        over_excited = True

    if user_answered_bots_question is False and api_call is True:
        print 'user not answering bots question'
        response.append({'type': 'text', 'message': 'Why are you not answering my questions?', 'stop': False})
        unanswered_questions_by_user += 1
        intents = previous_intents
        print 'unanswered questions by user %s' % unanswered_questions_by_user
        print 'intent is set to previous %s ' % previous_intents
        # set current intent to previous intent

    if intents is None:
        print '\t\tintents is set to None \t  bot is asking question'
        question = QuestionApi(msg=msg, domain=domain, entities=entities, user_id=user_id)
        if question.response:

            response.append(question.response)

            bots_intent = question.bot_intent
            # bot ask a question
            # send response
            count_of_bot_asked_questions += 1
            print '\t\t\t bots intent %s ' % bots_intent
            print  '\t\t\t response  %s ' % response
            print '\t\t\t count of bots question %s ' % count_of_bot_asked_questions

    if count_of_bot_asked_questions >= threshold_of_bot_asking_questions:
        print '\t\tYou are boring '
        response.append({'type': 'text',
                         'message': 'You are so boring!!! and dont want to chat with you. Why always I have to ask question',
                         'stop': True})
    elif unanswered_questions_by_user >= threshold_of_unanswerd_questions_by_user:
        print 'You are not answering my questions'
        response.append({'type': 'text', 'message': 'You not answering my question. Bye!!!', 'stop': True})

    print intents,',', domain,',', position_so_far,',', unanswered_questions_by_user,',', count_of_bot_asked_questions,',', bots_intent,',', bot_is_asking
    return response



def get_previous_info(intents, domain, position_so_far, unanswered_questions_by_user, count_of_bot_asked_questions, bots_intent, bot_is_asking):
    return intents, domain, position_so_far, unanswered_questions_by_user, count_of_bot_asked_questions, bots_intent, bot_is_asking

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
