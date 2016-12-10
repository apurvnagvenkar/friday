from pymongo import MongoClient
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
	{ user_id: user_id },
	{"$set":data},
        True
    )


def update_user_conversation(user_id, data):
    result = user_conversation.update(
	{ user_id: user_id },
	{"$set":data},
	True
    )

update_user_info("sachin",{"user_id":"sachin","name":"sach"})
result = get_user_info("sachin")
print result
