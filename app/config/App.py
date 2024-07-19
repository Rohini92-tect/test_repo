class App:
    request = None
    user = None

    @classmethod
    def cleanUp(cls):
        cls.request = None
        cls.user = None