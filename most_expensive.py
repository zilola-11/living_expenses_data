import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    with open(file_path, 'r') as f:
        dct = json.loads(f.read())
        
        most_expensive = 0 
        res = ""
        for key, i in dct.items():
            if i > most_expensive:
                most_expensive = i 
                print(most_expensive)
                res = key
    
    return res
               
# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)