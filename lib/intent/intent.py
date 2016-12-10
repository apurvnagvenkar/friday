import requests
import json
from data_architecture.call_intent_data import get_intent_list
from data_architecture.data_model import data_model


class Intent:
    def __init__(self, msg):
        self.msg = msg
        self.domain = None
        self.position = 0
        self.intent = []
        self.threshold_to_increment_position_for_given_domain = 0
    def run_intent_identification(self):

        self.intent = self.get_intent_from_message()
        return self.intent


    def get_intent_from_message(self):
        """
        Gets the intent of the message
        will return the list of intents
        :return:
        """
        intents_identified = []
        for data in data_model:
            intents = data_model[data]['intents']
            for intent in intents:
                data_list = get_intent_list(intent)

                # data_list = data_model[data][intent]['data_list']
                phrase_match = check_intent_match_for_given_msg(data_list, self.msg)
                if phrase_match:
                    intents_identified.append(intent)
                    self.domain = data
                    self.position = data_model[data]['position']
                    self.threshold_to_increment_position_for_given_domain = data_model[data]['number_times']
                    return intents_identified
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
    response = requests.get(
        'https://api.dandelion.eu/datatxt/sim/v1/?text1=%s&text2=%s&token=f1c9f83338f94289a73e2e07e5382d55'
        % (phrase, msg))
    if response:
        score = json.loads(response.content)['similarity']
        if score > 0.6:
            return True
    return False