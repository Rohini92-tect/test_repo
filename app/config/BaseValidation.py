class BaseValidation:

    @classmethod
    def _checkString(cls, key, value, default=None, requried = True):
        try :
            if value is None:
                result = cls._return_is_throw(requried, key, value, default)
                return result
            else:
                return value
            
        except:
            result = cls._return_is_throw(requried, key, value, default)

    @classmethod
    def _checkInteger(cls, key, value, default=None, requried = True):
        try :
            if value is None:
                result = cls._return_is_throw(requried, key, value, default)
                return result
            else:
                return value
        except:
            result = cls._return_is_throw(requried, key, value, default)
           
    @classmethod
    def _return_is_throw(cls, required, key, value, default):
        if required:
            error_details = {
                key : value
            }
            message = f'This is requried'+error_details
            return default
        else: 
            return default

