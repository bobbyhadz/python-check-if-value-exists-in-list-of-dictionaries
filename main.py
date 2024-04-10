# Check if a value exists in a List of Dictionaries in Python

list_of_dicts = [
    {'id': 1, 'name': 'alice', 'salary': 100},
    {'id': 2, 'name': 'bobby', 'salary': 101},
    {'id': 3, 'name': 'carl', 'salary': 102},
]

if any(
    dictionary.get('name') == 'bobby'
    for dictionary in list_of_dicts
):
    # 👇️ this runs
    print('A dictionary with the specified value exists')