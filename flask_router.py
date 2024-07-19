import json
class FlaskRouter(object):
    def __init__(self, action, method, body, header, path,queryparams):
        self.path = path
        self.method = method
        self.action = action
        self.header = header
        self.body = body
        self.queryparams = queryparams

    def load(self):
        return vars(self)
    
    def covert(self, response):
        return json.loads(response.replace("'", "\""))
    
        
