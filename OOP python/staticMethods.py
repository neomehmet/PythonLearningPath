import json

class JsonFile:
    @staticmethod
    def read(file_name): #self doenst necessary
        with open(file_name, 'a+') as file:
            try:
                file.seek(0)
                dict_data = json.load(file)
            except:
                dict_data = {}
        return dict_data
    
    @staticmethod
    def write(file_name, dict_data):
        with open(file_name, 'w') as file:
            file.write(json.dumps(dict_data, indent=4))