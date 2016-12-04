data_model = {
    'greet': {
        'position': 0,
        'causal': {
            'data_list': ['Hi',
                          'Hello',
                          'Hey'
                          'Good day'],

            'name': 'casual',
            'api_call': 'casual',
            'count': 2
        },
        'good_morning': {
            'data_list': [
                'Good morning',
                'Good night',
                'Good evening'
                'good afternoon'
            ],
            'name': 'good_morning',
            'api_call': 'good_morning',
            'count': 2
        },
        'intents': ['casual', 'good_morning']
    },
    'general_information': {
        'position': 1,

        'age': {
            'data_list': [
                'whats your age?',
                'age?'
            ],
            'name': 'age',
            'api_call': 'age',
            'count': 1

        },
        'occupation': {
            'data_list': [
                'what you do for living?',
                'what is your occupation?'
            ],
            'name': 'occupation',
            'api_call': 'occupation',
            'count': 1

        }
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
