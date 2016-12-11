from mongolib import get_user_info, update_user_info

__author__ = 'haptik'


class VerifyGeneralAPI():
    def __init__(self, msg, intent, entities, user_id):
        self.msg = msg
        self.intent = intent
        self.entities = entities
        self.user_id = user_id
        self.user_info = get_user_info(self.user_id)
        self.user_profile = self.user_info[self.user_id]
        print ' %s ' % self.user_profile
        self.response = []
        print entities
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
        users_age_on_fb = self.user_profile['info']['age_verify']
        if self.entities['age']:
            age_given_by_user = int(self.entities['age'])
        else:
            age_given_by_user = None
        msg = None
        if age_given_by_user:
            if age_given_by_user == users_age_on_fb:
                msg = 'Oh nice!!!'
            elif age_given_by_user > users_age_on_fb:
                msg =  'Why are you lieing to me? I can view your fb page. Its %s . \n Anyways i like people with older age.;)' % users_age_on_fb
            elif age_given_by_user < users_age_on_fb:
                msg =  'Why are you lieing to me? I can view your fb page. Its %s . \n Anyways i like people with lesser age.;)' % users_age_on_fb
            if msg:
                self.response.append({'type':'text', 'message':msg, 'stop':False})
                self.user_info[self.user_id]['info']['age'] = age_given_by_user
                print 'USer information changes: %s ' % self.user_info
                update_user_info(self.user_id, {'user_id': self.user_id, self.user_id :self.user_info[self.user_id]})
                print 'User information after updating: %s ' % get_user_info(self.user_id)

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
            elif occupation_given_by_user.lower() == 'architect':
                msg = 'Whats architect'

        if msg:
            self.response.append({'type':'text', 'message':msg, 'stop':False})
            self.user_info[self.user_id]['info']['occupation'] = occupation_given_by_user
            print 'USer information changes: %s ' % self.user_info
            update_user_info(self.user_id, {'user_id': self.user_id, self.user_id :self.user_info[self.user_id]})
            print 'User information after updating: %s ' % get_user_info(self.user_id)


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
            self.response.append({'type':'text', 'message':msg, 'stop':False})


            self.user_info[self.user_id]['info']['home_town'] = home_given_by_user
            print 'USer information changes: %s ' % self.user_info
            update_user_info(self.user_id, {'user_id': self.user_id, self.user_id :self.user_info[self.user_id]})
            print 'User information after updating: %s ' % get_user_info(self.user_id)

    def movie_api_call(self):
        """

        :return:
        """
        movie_given_by_user = self.entities['movie']
        msg = None
        if movie_given_by_user:
            if movie_given_by_user.lower() == 'arrival':
                msg = 'Oh nice Scifi Linguisitics'
            elif movie_given_by_user.lower() == 'doctor Strange':
                msg = 'Marvel Fan :) Me too'
            elif movie_given_by_user.lower() == 'inferno':
                msg = 'Description about mumbai'
            elif movie_given_by_user.lower() == 'befikre':
                msg = 'Is it  good one? I thaught its copy of Friends with benifit'
            else:
                msg =' Oh!! Nice but I din see it :('

        if msg:
            self.response.append({'type':'text', 'message':msg, 'stop':False})
            self.user_info[self.user_id]['info']['movie'] = movie_given_by_user
            print 'USer information changes: %s ' % self.user_info
            update_user_info(self.user_id, {'user_id': self.user_id, self.user_id :self.user_info[self.user_id]})
            print 'User information after updating: %s ' % get_user_info(self.user_id)


    def default(self):
        """

        :return:
        """

