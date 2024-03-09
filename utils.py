import os
import json


def save_dict_as_json(data_dict, file_name, directory_path='Project_Info/'):
    # Ensure the directory exists
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    # Construct the full file path
    file_path = os.path.join(directory_path, file_name)

    # Save the dictionary as a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)
    
    print(f"File saved successfully at {file_path}")


def load_json_as_dict(file_name, directory_path='Project_Info/'):
    # Construct the full file path
    file_path = os.path.join(directory_path, file_name)

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"No such file found at {file_path}")
        return None

    # Load the JSON file into a dictionary
    with open(file_path, 'r') as json_file:
        data_dict = json.load(json_file)
    
    print(f"File loaded successfully from {file_path}")
    return data_dict