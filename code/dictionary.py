import json
import sys
import os
from difflib import SequenceMatcher, get_close_matches
data = json.load(open('../data/data.json'))

def translate(param):
    match = get_close_matches(param, data.keys())[0]
    if match.lower() != param:
        fixed = input(f'Did you mean {match}? (Type "Yes"/"No") ')
        param = match if fixed.lower() == 'yes' else None
    if param == None:
        match = None
    if match in data:
        return data[match][0]
    else:
        return 'The word doesn\'t exist. Please provide a correct word'

word = input('Enter a desired word: -> ').lower()

print(translate(word))