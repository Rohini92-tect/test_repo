from app.services.add_data_services import AddDataService

class AddDataController:

    @classmethod
    def add_data_in_db(cls):
        return AddDataService.add_data_in_db()
    
    @classmethod
    def covert_into_csv(cls):
        return AddDataService.covert_into_csv()