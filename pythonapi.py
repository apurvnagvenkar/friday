import web
import json


urls = (
    '/message', 'message',
)

app = web.application(urls, globals())

class message:
    def POST(self):
        data = json.loads(web.data())
        print data["message"]
        return "ok"

if __name__ == "__main__":
    app.run()
