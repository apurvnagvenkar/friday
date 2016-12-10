data_model = {
    'salutation': {
        'position': 0,
        'casual': {
            'name': 'casual',
            'api_call': 'casual',
            'count': 2
        },
        'greet': {
            'name': 'greet',
            'api_call': 'greet',
            'count': 2
        },
        'intents': ['casual', 'greet'],
        'number_times': 1
    },
    'general_information': {
        'position': 1,

        'age': {
            'name': 'age',
            'api_call': 'age',
            'count': 1
        },
        'occupation': {
            'name': 'occupation',
            'api_call': 'occupation',
            'count': 1

        },
        'intents': ['age', 'occupation'],
        'number_times': 2

    }
}


bot_persona = {
    'age': 21,
    'name': 'June',
    'full name': 'June May',
    'occupation': 'engineer'

}

bot_user_conversation = {
    'apurv': {
        'bot_is_asking': False,
        'bot_initiated_conv_simultaneous': 0,
        'state': None,
        'current_domain': None,
        'sub_domain': None,
        'score': 0,
        'position': 0,

    }
}

user_info = {
    'apurv': {
        'name': 'apurv',
        'info': {
            'age': None,
            'age_verify': 25,
            'occupation': None,
            'city': None,
            'studied': None
        }

    }
}
