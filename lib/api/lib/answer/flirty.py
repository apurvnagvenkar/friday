class AnswerFlirtyAPI():
    def __init__(self, msg, intent, entities, user_id, existing_score):
        self.msg = msg
        self.intent = intent
        self.entities = entities
        self.user_id = user_id
        self.response = []
        self.existing_score =existing_score
        self.score = 0
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
        msg = 'Hehe :-D You are so cheesy  ;-)'
        self.response.append({'type':'text', 'message':msg, 'stop':False})
        self.score = 2
    def love_api_call(self):
        """

        :return:
        """
        msg = 'Oh Plz!!! Give me some space !!!'
        self.response.append({'type':'text', 'message':msg, 'stop':False})
        self.score -= 2
    def out_api_call(self):
        """

        :return:
        """
        if self.existing_score >= 7:
            self.response.append({'type':'text', 'message': 'Ya sure! What about next Weekend? ', 'stop': True, 'stop_message': 'Congrats! You my friend are real date :) ;)  '})
        else:
            self.response.append({'type':'text', 'message': 'Whoa! Lets know each other first.', 'stop': False})

    def rude_api_call(self):
        msg = 'You are disgusting! Learn some manners and then come back!'
        self.response.append({'type':'text', 'message':msg, 'stop':True, 'stop_message': 'Never abuse a women. Speak politely and genetly to win her hearts !!!' })


    def default(self):
        """

        :return:
        """

