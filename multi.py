import sys
import clipboard
import json

SAVED_DATA = "data.json"


def save_data(filepath, data):
    with open(filepath, "w") as f:  
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}    
def delete_data(filepath, data, key):
    with open(filepath, "w") as f:
        del data[key]
        json.dump(data, f)
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key = input("key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved")
    elif command == "load":
        key = input("key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key does not exist")
    elif command == "list":
        print(data)
    elif command == "delete":
        key = input("key: ")
        data = delete_data(SAVED_DATA, data, key)
        print("Data deleted")
    else:
        print("unknown command")
else:
    print("please type in one command (save, load, list")