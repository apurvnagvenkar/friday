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
            self.response.append(msg)

        else:
            self.response.append('I think i started liking you can we meet somewhere? ')

    def get_general_information(self, info):
        msg = None
        if info == 'age':
            self.bot_intent.append('age')
            self.domain = 'general_information'
            msg= 'hey wats your age?'
        elif info == 'occupation':
            self.bot_intent.append('occupation')
            self.domain = 'general_information'
            msg= 'hey wats your occupation'
        elif info == 'home_town':
            self.bot_intent.append('home_town')
            self.domain = 'general_information'
            msg= 'hey wats your home town?'
        elif info == 'movie':
            self.bot_intent.append('movie')
            self.domain = 'general_information'
            msg= 'hey wats your favouriate movie?'

        return msg

    def default(self):
        """

        :return:
        """