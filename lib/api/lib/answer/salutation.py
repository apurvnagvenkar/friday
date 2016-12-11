from mongolib import get_user_info

__author__ = 'haptik'


class AnswerSalutationAPI():
    def __init__(self, msg, intent, entities, user_id):
        self.msg = msg
        self.intent = intent
        self.entities = entities
        self.user_id = user_id
        self.user_profile = get_user_info(self.user_id)[self.user_id]
        print ' %s ' % self.user_profile

        self.response = []
        dict = {
            'casual': self.casual_api_call,
            'greet': self.greet_api_call,
            'Default': self.default
        }

        dict.get(intent, dict['Default'])()

    def casual_api_call(self):
        """

        :return:
        """
        msg = 'Hello'
        self.response.append({'type':'text', 'message':msg, 'stop':False})


    def greet_api_call(self):
        """

        :return:
        """
        msg = 'Good Morning'
        self.response.append({'type':'text', 'message':msg, 'stop':False})

    def default(self):
        """

        :return:
        """

