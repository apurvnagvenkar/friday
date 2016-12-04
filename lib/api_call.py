from data_model import bot_persona, user_info, bot_user_conversation

__author__ = 'haptik'


def reply_age_of_bot(user):

    msg = 'My age is %s. ' % bot_persona['age']

    msg += send_next_meesage(user)
    return msg

def reply_occupation_of_bot(user):

    msg = 'My occupation is %s. ' % bot_persona['occupation']

    msg += send_next_meesage(user)
    return msg


def verify_users_age(user):
    users_age_on_fb= user_info[user]['info']['age_verify']
    age_given_by_user =  user_info[user]['info']['age']
    msg = None
    if age_given_by_user == users_age_on_fb:
        msg = 'Oh nice!!!'
        msg += send_next_meesage(user)
    elif age_given_by_user > users_age_on_fb:
        msg =  'Why are you lying to me? I can view your fb page. Its %s . \n Anyways i like people with older age.;)' % users_age_on_fb
        msg += send_next_meesage(user)
    elif age_given_by_user < users_age_on_fb:
        msg =  'Why are you lying to me? I can view your fb page. Its %s . \n Anyways i like people with lesser age.;)' % users_age_on_fb
        msg += send_next_meesage(user)
    return msg


def ask_information(info, user):
    if info == 'age':
        bot_user_conversation[user]['sub_domain'] = 'age'
        bot_user_conversation[user]['domain'] = 'general_information'
        return 'hey wats your age'
    elif info == 'occupation':
        bot_user_conversation[user]['sub_domain'] = 'occupation'
        bot_user_conversation[user]['domain'] = 'general_information'
        return 'hey wats your occupation'


def send_next_meesage(user):
    msg =''
    personal_info = user_info[user]['info']
    for info in personal_info:
        if not user_info[user]['info'][info]:
            msg += ask_information(info, user)
            bot_user_conversation[user]['bot_is_asking'] = True
            bot_user_conversation[user]['bot_initiated_conv_simultaneous']+=1
            break
        else:
            bot_user_conversation[user]['bot_is_asking'] = False
            bot_user_conversation[user]['bot_initiated_conv_simultaneous']=0

    return msg