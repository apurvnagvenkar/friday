from lib.api.lib.verfiy.general_information import VerifyGeneralAPI

__author__ = 'haptik'


class VerifyApi():
    def __init__(self, msg, domain ,intent, entities, user_id):
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
            'Default': self.default
        }

        dict.get(domain, dict['Default'])()


    def general_information(self):
        """

        :return:
        """

        v=VerifyGeneralAPI(self.msg, self.intent, self.entities, self.user_id)
        self.response = v.response



    def default(self):
        """

        :return:
        """