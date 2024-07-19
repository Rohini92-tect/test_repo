from app.config.BaseValidation import BaseValidation
from app.config.App import App
class AddDataValidation(BaseValidation):

    @classmethod
    def add_data_in_validation(cls):
        param = {
            "name" : cls._checkString("name", App.request.body.get("name"), default="", requried=False),
            "address"  : cls._checkString("address", App.request.body.get("address"), default="", requried=False),
            "email" : cls._checkString("email", App.request.body.get("email"), default="" , requried=False),
            "phone" : cls._checkInteger("phone_number", App.request.body.get("phone_number"), default=None, requried=False)
        }
        return param