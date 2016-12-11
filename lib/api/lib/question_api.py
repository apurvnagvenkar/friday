from mongolib import get_user_info


class QuestionApi():
    def __init__(self, msg, domain, intent, entities, user_id):
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
        self.user_id = user_id
        self.user_profile = get_user_info(self.user_id)[self.user_id]
        self.response = []
        self.domain = None
        self.bot_intent = []
        self.intent = intent
        self.quick_responses = []
        dict = {
            'general_information': self.general_information,
            'Default': self.default
        }

        dict.get(domain, dict['Default'])()


    def general_information(self):
        """
        :return:
        """
        msg =None
        personal_info = self.user_profile['info']
        if self.intent and personal_info.get(self.intent[0]) is None:
            msg = self.get_general_information(self.intent[0])
        else:
            for info in personal_info:
                if not personal_info[info]:
                    msg = self.get_general_information(info)
                    if msg:
                        break


        if msg:
            if self.quick_responses:
                self.response.append({'type':'payload','message':{'text':msg, 'quick_replies':self.quick_responses}, 'stop':False })
            else:
                self.response.append({'type':'text', 'message': msg, 'stop': False})
        print self.response
#        else:
#            self.response.append('I think i started liking you can we meet somewhere? ')

    def get_general_information(self, info):
        msg = None
        if info == 'age':
            self.bot_intent.append('age')
            self.domain = 'general_information'
            msg= 'what is your age?'
        elif info == 'occupation':
            self.bot_intent.append('occupation')
            self.domain = 'general_information'
            msg= 'What do you do for living?'
            self.quick_responses = [
                {
                  "content_type":"text",
                    "title":"Doctor",
                    "payload":"Doctor"
            },{
                  "content_type":"text",
                    "title":"Engineer",
                    "payload":"Engineer"
            },
              {
                  "content_type":"text",
                    "title":"Lawyer",
                    "payload":"Lawyer"
            }]

        elif info == 'home_town':
            self.bot_intent.append('home_town')
            self.domain = 'general_information'
            msg= 'Which is your home town?'
        elif info == 'movie':
            self.bot_intent.append('movie')
            self.domain = 'general_information'
            msg= 'Which is your favourite movie?'
            self.quick_responses = [
                {
                  "content_type":"text",
                    "title":"Arrival",
                    "payload":"Arrival"
            },{
                  "content_type":"text",
                    "title":"Doctor Strange",
                    "payload":"Doctor Strange"
            },
              {
                  "content_type":"text",
                    "title":"Befikre",
                    "payload":"Befikre"
            },
              {
                  "content_type":"text",
                    "title":"Inferno",
                    "payload":"Inferno"
            },


            ]
        return msg

    def default(self):
        """

        :return:
        """
