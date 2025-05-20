import json

def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    with open(file_path, "r") as f:
        dct = json.loads(f.read)
        lst1 =(list(dct.values()))
        average = sum(lst1) / len(lst1)
        return average
    
file_path = "data.json"
average = average_expenses(file_path)
print(average)