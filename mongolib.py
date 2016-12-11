from pymongo import MongoClient
import urllib2
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client['june']
user_info = db['user_info']
user_conversation = db['user_conversation']
#result = user_info.insert_one({'x': 1})
#result = user_info.find_one({'x': 1})
#print result


def get_user_info(user_id):
    result = user_info.find_one({"user_id": user_id})
    return result


def get_user_conversation(user_id):
    result = user_conversation.find_one({"user_id": user_id})
    return result


def update_user_info(user_id, data):
    result = user_info.update(
	{ "user_id": user_id },
        {"$set":data},
        True
    )


def update_user_conversation(user_id, data):
    result = user_conversation.update(
	{ user_id: user_id },
	{"$set":data},
	True
    )

def delete_user_conversation(user_id):
    result = user_conversation.delete_one(
	{ "user_id": user_id }
    )


#def get_age():
#    response = urllib2.urlopen('https://graph.facebook.com/v2.8/me?fields=birthday&access_token=EAAPogLiQapYBAKVEkcGfsZCHN25uHhJRjOZBJ8mJDi47MJbpVErJZBgBIK7nZAe43aIKDjGGryPhwvDb9CZB2vbLOPKCjGLlrjSDB0mGlsXRYYmvUwOPvt8j147zkZCcIik4D6ZCLwJKcX7XFt94jSmBSfoh4rX0ZBwn4iwn8NZA7GQZDZD'

def start_over(user_id):
    data = {
        'user_id' : user_id,
        user_id : {
            'name': 'apurvaa',
            'info': {
                'age': None,
                'age_verify': 25,
                'occupation': None,
                'city': None,
                'studied': None,
                'home_town': None,
                'movie': None,
            }
        }
    }
    update_user_info(user_id,data)
    delete_user_conversation(user_id)
    print get_user_info(user_id)
