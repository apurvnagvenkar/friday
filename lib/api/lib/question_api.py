from mongolib import get_user_info


class QuestionApi():
    def __init__(self, msg, domain , entities, user_id):
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
        for info in personal_info:
            if not personal_info[info]:
                if info == 'age':
                    self.bot_intent.append('age')
                    self.domain = 'general_information'
                    msg= 'hey wats your age'

                elif info == 'occupation':
                    self.bot_intent.append('occupation')
                    self.domain = 'general_information'
                    msg= 'hey wats your occupation'

                break


        if msg:
            self.response.append({'type': 'text', 'message': msg, 'stop': False})



    def default(self):
        """

        :return:
        """