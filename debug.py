import application
import json
 
# with open("api_debug/add_data_in_db.json") as json_data:
#     data = json.load(json_data)
#     print(application.handler(data,None))

with open("api_debug/convert_into_csv.json") as json_data:
    data = json.load(json_data)
    print(application.handler(data, None))