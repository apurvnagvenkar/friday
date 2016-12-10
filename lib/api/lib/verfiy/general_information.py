from mongolib import get_user_info

__author__ = 'haptik'


class VerifyGeneralAPI():
    def __init__(self, msg, intent, entities, user_id):
        self.msg = msg
        self.intent = intent
        self.entities = entities
        self.user_id = user_id
        self.user_profile = get_user_info(self.user_id)[self.user_id]
        print ' %s ' % self.user_profile
        self.response = []
        print entities
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
        users_age_on_fb = self.user_profile['info']['age_verify']
        age_given_by_user = self.entities['age']
        msg = None
        if age_given_by_user:
            if age_given_by_user == users_age_on_fb:
                msg = 'Oh nice!!!'
                # sachin
            elif age_given_by_user > users_age_on_fb:
                msg =  'Why are you lieing to me? I can view your fb page. Its %s . \n Anyways i like people with older age.;)' % users_age_on_fb
            elif age_given_by_user < users_age_on_fb:
                msg =  'Why are you lieing to me? I can view your fb page. Its %s . \n Anyways i like people with lesser age.;)' % users_age_on_fb
            if msg:
                self.response.append(msg)

    def occupation_api_call(self):
        """

        :return:
        """
        occupation_given_by_user = self.entities['occupation']
        msg = None
        if occupation_given_by_user:
            if occupation_given_by_user.lower() == 'engineer':
                msg = 'Nice Engineer hannh!!!'
            elif occupation_given_by_user.lower() == 'doctor':
                msg = 'Whats up bro does your heartbeat speak?'
        if msg:
            self.response.append(msg)


    def home_api_call(self):
        """

        :return:
        """
        home_given_by_user = self.entities['city']
        msg = None
        if home_given_by_user:
            if home_given_by_user.lower() == 'pune':
                msg = 'Description about pune'
            elif home_given_by_user.lower() == 'delhi':
                msg = 'Description about delhi'
            elif home_given_by_user.lower() == 'mumbai':
                msg = 'Description about mumbai'
            elif home_given_by_user.lower() == 'bengaluru':
                msg = 'Description about bengaluru'
            else:
                msg =' Oh!! Nice place'

        if msg:
            self.response.append(msg)

    def default(self):
        """

        :return:
        """

