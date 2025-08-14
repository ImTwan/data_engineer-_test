import json 

json_file = 'D:\python try hard\DE\data_engineer-_test\Question3\employees.json' #JSON file path

def extract(file_path): 
    try: 
        with open(file_path, 'r') as file:
            data = json.load(file)
        print ("Extract data")
        return data
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

print(extract(json_file))