"""Homework file for my students to have fun with some algorithms! """
incoming_list = [1, 2, 3, 5, 8, 13, 21, 34, 55]
incoming_dict = {"Internazionale": "Best team", "AC Milan": "Runnersup", "Juventus": "Bronze",
"AS Roma": "4th Clinchers", "Atalanta B.C.": "Sadness"}

def find_greatest_number(incoming_list):
    """Finds the largest number in the list."""
    return_value = max(incoming_list)
    return return_value


def find_least_number(incoming_list):
    """Finds the smallest/least number in the list."""
    return_value = min(incoming_list)
    return return_value


def add_list_numbers(incoming_list):
    """Adds all the values together and return it."""
    if incoming_list is None:
        return 0
    return_value = sum(incoming_list)
    return return_value


def longest_value_key(incoming_dict):
    """Find the KEY that has a value with the highest length, use the len() function
    solution found at https://stackoverflow.com/questions/19845258/list-as-value-in-dictionary-get-key-of-longest-list"""
    if incoming_dict is not None:
        if len(incoming_dict) == 0:
            return None
        longest_key = max(incoming_dict, key=lambda x:len(incoming_dict[x]))
        return longest_key
    else:
        return None
