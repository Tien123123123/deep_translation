import os, sys
from pprint import pprint
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from inference_translate import inference_translate
import re

def seperate_word(text):
    array_str = text.split(" ")
    n = len(array_str)
    array = []
    i = 0
    pattern = r'^[a-zA-Z\s.!?,]*$'
    while i < n:
        if array_str[i].isalpha():

            start = i
            while i < n and (array_str[i].isalpha() or re.match(pattern, array_str[i])):
                i += 1

            array.append(array_str[start:i])

            if i < n:
                array.append(array_str[i])
                i += 1
        else:

            array.append(array_str[i])
            i += 1

    return array

def flatten_and_convert(lst, args):
    result = []
    for item in lst:
        if isinstance(item, list):
            a_str = ' '.join(str(x) for x in item)
            a_str = inference_translate(a_str, args)
            result.append(a_str)
        else:

            result.append(str(item))
    return result
