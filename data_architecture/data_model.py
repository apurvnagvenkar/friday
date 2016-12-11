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
            'count': 2
        },
        'occupation': {
            'name': 'occupation',
            'api_call': 'occupation',
            'count': 2

        },
        'home_town': {
            'name': 'home_town',
            'api_call': 'home_town',
            'count': 2
        },
        'hobbies': {
            'name': 'hobbies',
            'api_call': 'hobbies',
            'count': 2
        },
       'movie': {
            'name': 'movie',
            'api_call': 'movie',
            'count': 2
        },

        'intents': ['age', 'occupation','home_town','hobbies', 'movie'],
        'number_times': 4

    },
    'flirty': {
        'position': 0,
        'cheesy': {
            'name': 'cheesy',
            'api_call': 'cheesy',
            'count': 3
        },
        'love': {
            'name': 'love',
            'api_call': 'love',
            'count': 3
        },
        'rude':{
            'name': 'rude',
            'api_call': 'rude',
            'count': 3
        },
        'out':{
            'name': 'out',
            'api_call': 'out',
            'count': 3
        },


        'intents': ['cheesy', 'love','rude', 'out'],
        'number_times': 10
    }
}


bot_persona = {
    'age': 22,
    'name': 'June',
    'full name': 'June May',
    'occupation': 'Engineer',
    'home_town': 'Pune',
    'movie': 'Dilwale Dulaniya Le Jayenge',
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
