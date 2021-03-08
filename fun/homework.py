"""Homework file for my students to have fun with some algorithms! """
incoming_list = [1, 2, 3, 5, 8, 13, 21, 34, 55]
incoming_dict = {"Internazionale": 59, "AC Milan": 56, "Juventus": 52, "AS Roma": 50, "Atalanta B.C.": 49} 

def find_greatest_number(incoming_list):
    return_value = max(incoming_list)
    return return_value
"""
Required parameter, incoming_list, should be a list.
Find the largest number in the list.
"""
pass


def find_least_number(incoming_list):
    return_value = min(incoming_list)
    return return_value
"""
Required parameter, incoming_list, should be a list.
Find the smallest/least number in the list.
"""
pass


def add_list_numbers(incoming_list):
   return_value = sum(incoming_list)
   if return_value = None: 
       return 0
   else:
       return return_value
"""
Required parameter, incoming_list, should be a list.
Add all the values together and return it.
"""
pass


def longest_value_key(incoming_dict):
    return_value = max(len(incoming_dict) for x in incoming_dict )
    return return_value
"""
Required parameter, incoming_dict, should be a dict.
Find the KEY that has a value with the highest length, use the len() function
solution found at https://stackoverflow.com/questions/10895567/find-longest-string-key-in-dictionary
"""
pass
