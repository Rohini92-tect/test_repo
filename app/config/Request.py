class Request(object):

    def __init__(self):
        self.__resource = None
        self.__method = None
        self.__action = None
        self.__header = None
        self.__body = None
        self.__query = None
        self.__path = None

    @property
    def resource(self):
        return self.__resource

    @property
    def method(self):
        return self.__method

    @property
    def action(self):
        return self.__action

    @property
    def header(self):
        return self.__header

    @property
    def body(self):
        return self.__body

    @property
    def query(self):
        return self.__query

    @property
    def path(self):
        return self.__path

    @resource.setter
    def resource(self, param):
        self.__resource = param.get('resource')

    @method.setter
    def method(self, param):
        self.__method = param.get('httpMethod')

    @action.setter
    def action(self, param):    
        self.__action = param.get('action')

    @header.setter
    def header(self, param):
        self.__header = param.get('headers') if param and isinstance(param.get('headers'), dict) else {}

    @body.setter
    def body(self, param):
        self.__body = param.get('body') if param and (isinstance(param.get('body'), dict) or isinstance(param.get('body'), list)) else {}

    @query.setter
    def query(self, param):
        self.__query = param.get('queryStringParameters') if param and isinstance(param.get('queryStringParameters'), dict) else {}

    @path.setter
    def path(self, param):
        self.__path = param.get('pathParameters') if param and isinstance(param.get('pathParameters'), dict) else {}

    @classmethod
    def load(cls, event):
        req = cls()
        req.method = event
        req.resource = event
        req.query = event
        req.header = event
        req.body = event
        req.path = event
        req.action = event
        print(req,"req")
        return req
