from data_architecture.data_model import bot_persona

__author__ = 'haptik'


class AnswerGeneralAPI():
    def __init__(self, msg, intent, entities, user_id):
        self.msg = msg
        self.intent = intent
        self.entities = entities
        self.user_id = user_id
        self.response = []
        self.score = 0
        dict = {
            'age': self.age_api_call,
            'occupation': self.occupation_api_call,
            'home_town': self.home_api_call,
            'movie': self.movie_api_call,
            'Default': self.default
        }

        dict.get(intent, dict['Default'])()

    def age_api_call(self):
        """

        :return:
        """
        msg = 'I am %s. years old. ' % bot_persona['age']
        self.response.append({'type':'text', 'message':msg, 'stop':False})
        self.score = 1

    def occupation_api_call(self):
        """

        :return:
        """
        msg = 'My occupation is %s. ' % bot_persona['occupation']
        self.response.append({'type':'text', 'message':msg, 'stop':False})
        self.score = 1

    def home_api_call(self):
        """

        :return:
        """
        msg = 'My home town is %s. ' % bot_persona['home_town']
        self.response.append({'type':'text', 'message':msg, 'stop':False})
        self.score = 2

    def movie_api_call(self):
        msg = 'My favouriate movie  is %s. Tujhe dekha tho hein jana sanam!!! ' % bot_persona['movie']
        self.response.append({'type':'text', 'message':msg, 'stop':False})
        self.score = 2

    def default(self):
        """

        :return:
        """

