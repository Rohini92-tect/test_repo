from app.validation.add_data_validation import AddDataValidation
from app.model.add_data_model import AddData
import csv
import os

class AddDataService():

    @classmethod
    def add_data_in_db(cls):
        print("############inside the insert new data#############")
        param = AddDataValidation.add_data_in_validation()
        data = AddData.add_data_into_collection(param)
        print(data)
    
    @classmethod
    def covert_into_csv(cls):
        get_data = AddData.get_data_for_csv()
        print(get_data,"get_data")
        file_name = "All Data Of Collection.xlsx"
        folder_path = "D:\\"
        column_name = [{
            "label" : "Name",
            "value" : "name"
            },
            {
            "label" : "Email",
            "value" : "email"

            },
            {
                "label" : "Phone",
                "value" : "phone"
            },
            {
                "label": "Address",
                "value" : "address"
            }
        ]

        all_col_name = [item['label'] for item in column_name]
        print(all_col_name,"all_col_name")
        csv_data = []
        for item in get_data:
            row_data = {}
            for col in column_name:
                label = col.get("label")
                value = item.get(col.get("value"))
                row_data[label] = value
            csv_data.append(row_data)
        print(csv_data,"csv")
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)
        print(file_path,"file_path")

        with open(file_path, mode="w", newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=all_col_name)
            writer.writeheader()
            for row in csv_data:
                writer.writerow(row)

            





    