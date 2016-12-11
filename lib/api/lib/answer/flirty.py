class AnswerFlirtyAPI():
    def __init__(self, msg, intent, entities, user_id):
        self.msg = msg
        self.intent = intent
        self.entities = entities
        self.user_id = user_id
        self.response = []
        dict = {
            'cheesy': self.cheesy_api_call,
            'love': self.love_api_call,
            'out': self.out_api_call,
            'rude': self.rude_api_call,
            'Default': self.default
        }

        dict.get(intent, dict['Default'])()

    def cheesy_api_call(self):
        """

        :return:
        """
        msg = 'Heehee :‑D !!! You are so cheesy  ;‑)'
        self.response.append({'type':'text', 'message':msg, 'stop':False})

    def love_api_call(self):
        """

        :return:
        """
        msg = 'Oh Plz!!! Give me some space !!!'
        self.response.append({'type':'text', 'message':msg, 'stop':False})

    def out_api_call(self):
        """

        :return:
        """
    def rude_api_call(self):
        msg = 'You are disgusting!!! \n Bye, learn some manners and then come back!!! '
        self.response.append({'type':'text', 'message':msg, 'stop':True, 'stop_message': 'TIP: Never abuse a women. Speak politely and genetly to win their hearts !!!' })


    def default(self):
        """

        :return:
        """

