from lib.api.lib.answer.flirty import AnswerFlirtyAPI
from lib.api.lib.answer.general_information import AnswerGeneralAPI
from lib.api.lib.answer.salutation import AnswerSalutationAPI
from lib.api.lib.verfiy.general_information import VerifyGeneralAPI

__author__ = 'haptik'


class AnswerApi():
    def __init__(self, msg, domain,intent, entities, user_id):
        """

        :param msg:
        :param intent:
        :param entities:
        :param user_id:
        :return:
        """
        self.msg =msg
        self.entities = entities
        self.domain= domain
        self.intent = intent
        self.user_id = user_id
        self.response = []
        dict = {
            'general_information': self.general_information,
            'salutation': self.salutation,
            'flirty': self.flirty,
            'Default': self.default
        }

        dict.get(domain, dict['Default'])()


    def general_information(self):
        """

        :return:
        """

        v=AnswerGeneralAPI(self.msg, self.intent, self.entities, self.user_id)
        self.response = v.response

    def salutation(self):
        """

        :return:
        """

        v=AnswerSalutationAPI(self.msg, self.intent, self.entities, self.user_id)
        self.response = v.response

    def flirty(self):
        """

        :return:
        """

        v=AnswerFlirtyAPI(self.msg, self.intent, self.entities, self.user_id)
        self.response = v.response

    def default(self):
        """

        :return:
        """