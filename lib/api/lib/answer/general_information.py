from data_architecture.data_model import bot_persona

__author__ = 'haptik'


class AnswerGeneralAPI():
    def __init__(self, msg, intent, entities, user_id):
        self.msg = msg
        self.intent = intent
        self.entities = entities
        self.user_id = user_id
        self.response = []
        dict = {
            'age': self.age_api_call,
            'occupation': self.occupation_api_call,
            'Default': self.default
        }

        dict.get(intent, dict['Default'])()

    def age_api_call(self):
        """

        :return:
        """
        msg = 'My age is %s. ' % bot_persona['age']
        self.response.append({'type': 'text', 'message': msg, 'stop': False})

    def occupation_api_call(self):
        """

        :return:
        """
        msg = 'My occupation is %s. ' % bot_persona['occupation']
        self.response.append({'type': 'text', 'message': msg, 'stop': False})

    def default(self):
        """

        :return:
        """

