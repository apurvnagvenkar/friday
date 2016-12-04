import requests
import json
from data_models import data_model


def get_subdomain_from_message(msg):
    """
    Gets the intent of the message
    will return the list of intents
    :param msg:
    :return:
    """
    intents_identified = []
    for data in data_model:
        intents = data_model[data]['intents']
        for intent in intents:
            data_list = data_model[data][intent]['data_list']
            phrase_match = check_intent_match_for_given_msg(data_list,msg)
            if phrase_match:
                intents_identified.append(intent)
    return intents_identified


def check_intent_match_for_given_msg(data_list, msg):
    """
    Compares the phrases with all the phrases of a given intetne
    :param data_list:
    :return:
    """
    for phrase in data_list:
        phrase_found = call_sentence_similarity(phrase, msg)
        if phrase_found:
            return True
        else:
            return False


def call_sentence_similarity(phrase, msg):
    """
    Calls sentence similarity api
    :param phrase:
    :param msg:
    :return:
    """
    if phrase == msg:
        return True
    response = requests.get('https://api.dandelion.eu/datatxt/sim/v1/?text1=%s&text2=%s&token=f1c9f83338f94289a73e2e07e5382d55'
                            % (phrase, msg))
    if response:
        score = json.loads(response.content)['similarity']
        if score > 0.6:
            return True
    return False



print  get_subdomain_from_message('whats your age?')