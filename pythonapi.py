import web
import json
from main import run_june_1
from mongolib import start_over

urls = (
    '/message', 'message',
)

app = web.application(urls, globals())

class message:
    def POST(self):
        data = json.loads(web.data())
        message = data["message"]
        user_id = data["user_id"]
        if "start over" in data["message"]:
            start_over(user_id)
            response = [{"message": "Done"}]
        else:
            response = run_june_1(data["message"],user_id)
        return json.dumps({"response": response})

if __name__ == "__main__":
    app.run()
