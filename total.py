import json

def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    with open(file_path, 'r') as f:
        dct = json.loads(f.read())
        
        total = 0 
        for i in dct.values():
            total += i
    return total
    

# test
file_path = "data.json"
total = total_expenses(file_path)
print(total)
