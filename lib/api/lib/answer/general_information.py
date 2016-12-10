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
            'home_town': self.home_api_call,
            'Default': self.default
        }

        dict.get(intent, dict['Default'])()

    def age_api_call(self):
        """

        :return:
        """
        msg = 'My age is %s. ' % bot_persona['age']
        self.response.append(msg)

    def occupation_api_call(self):
        """

        :return:
        """
        msg = 'My occupation is %s. ' % bot_persona['occupation']
        self.response.append(msg)

    def home_api_call(self):
        """

        :return:
        """
        msg = 'My home town is %s. ' % bot_persona['home_town']
        self.response.append(msg)

    def default(self):
        """

        :return:
        """

