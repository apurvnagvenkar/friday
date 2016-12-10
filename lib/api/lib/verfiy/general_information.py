from data_architecture.data_model import user_info

__author__ = 'haptik'


class VerifyGeneralAPI():
    def __init__(self, msg, intent, entities, user_id):
        self.msg = msg
        self.intent = intent
        self.entities = entities
        self.user_id = user_id
        self.user_profile = user_info[self.user_id]
        self.response = []
        dict = {
            'age': self.age_api_call,
            'occupation': self.occupation_api_call,
        }

        dict.get(intent, dict['Default'])()

    def age_api_call(self):
        """

        :return:
        """
        users_age_on_fb = self.user_profile['info']['age_verify']
        age_given_by_user = self.entities['age']
        msg = None
        if age_given_by_user:
            if age_given_by_user == users_age_on_fb:
                msg = 'Oh nice!!!'
            elif age_given_by_user > users_age_on_fb:
                msg =  'Why are you lieing to me? I can view your fb page. Its %s . \n Anyways i like people with older age.;)' % users_age_on_fb
            elif age_given_by_user < users_age_on_fb:
                msg =  'Why are you lieing to me? I can view your fb page. Its %s . \n Anyways i like people with lesser age.;)' % users_age_on_fb
            if msg:
                self.response.append({'type': 'text', 'message': msg, 'stop': False})

    def occupation_api_call(self):
        """

        :return:
        """
        occupation_given_by_user = self.entities['occupation']
        msg = None
        if occupation_given_by_user:
            if occupation_given_by_user.lower() == 'enginner':
                msg = 'Nice Engineer hannh!!!'
            elif occupation_given_by_user.lower() == 'doctor':
                msg = 'Nice Doctor hannh!!!'
        if msg:
            self.response.append({'type': 'text', 'message': msg, 'stop': False})

    def default(self):
        """

        :return:
        """
