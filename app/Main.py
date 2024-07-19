from app.config import App, Request, Application
from app.controller import AddDataController

class Main:
    def run(event, context):
        data = "Not allowed"
        App.App.request = Request.Request.load(event)
        print("hjksdhajksdasjkd")
        # print({f"App.request:", App.App.request.__dict__})
        # print(App.App.request,"App.App.request")
        if Application.Actions.get(App.App.request.action):
            invock = getattr(eval(Application.Actions.get(App.App.request.action)), 
                                                          App.App.request.action)
            
            print(invock,"invock")
            data = invock()
            print(data)
        
        return data



    