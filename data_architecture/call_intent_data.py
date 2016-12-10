from data_architecture.general_information.age import age_intent
from data_architecture.general_information.occupation import occupation_intent
from data_architecture.salutation.casual import casual_intent
from data_architecture.salutation.greet import greet_intent


def get_intent_list(intent):
    """

    :param intent:
    :return:
    """

    dict = {
        'casual': casual_intent.intent_text,
        'greet': greet_intent.intent_text,
        'age': age_intent.intent_text,
        'occupation': occupation_intent.intent_text,
        'Default': default
    }
    return dict.get(intent, dict['Default'])()

def default():
    """

    :return:
    """
    return []