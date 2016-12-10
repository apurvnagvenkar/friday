import json
import requests


class Entity():
    def __init__(self, msg):
        self.msg = msg
        self.username = 'haptik_token1_user1'
        self.access_token = 'HAPTIK07051990AWERVF'
        self.entities = ['occupation','age','city','hobby','movie']

    def run_entity_detector(self):
        url_call = ('http://bot.haptik.ai/ner/v1/tag/?username=%s&api_key=%s&entities=%s&message=%s' % (self.username, self.access_token, self.entities, self.msg))

        response = requests.get(url_call)
        entity_data = {}
        if response:
            entity_data = json.loads(response.content)['data']
        return entity_data


