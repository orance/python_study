import web
urls = (
'/','index'
)
class index:
    def GET(self):
        return "Hello,world!"

_name_ = ''
if _name_ == "_main_":
    app = web.application(urls,globals())
    app.run()
