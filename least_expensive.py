import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    with open(file_path, 'r') as f:
        dct = json.loads(f.read())
        print(data)
        
# test
file_path = "data.json"
least_expensive_item = least_expensive(file_path)
print(least_expensive_item)
