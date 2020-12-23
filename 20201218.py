import numpy as np
import pandas as pd


# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.

# Python has a built-in package called re, which can be used to work with Regular Expressions.

# Import the re module:

import re

txt = "The rain is Spain"
x=re.search("^The.*Spain$",txt)
if x:
    print("YES! We have a match")
else:
    print("No Match")

# The model SequenceMatcher Calculate string similarity
from  difflib import SequenceMatcher

def similarity (a,b):
    return SequenceMatcher(None,a,b).ratio()
print(similarity('L405 3.0P AJ126 SC AWD 5DR SWB Vogue, Beijing CH1, AB405/357AB, 2019','L405 3.0P AJ20-P6H AWD 5DR LWB Autobiography - 400PS Auto, Beijing CH1, HH405/357CB, 2020'))
print(similarity('L405 3.0P AJ126 SC AWD 5DR SWB Vogue, Beijing CH1, AB405/357AB, 2019','L405 3.0P AJ126 SC AWD 5DR SWB Vogue, Beijing CH1, AB405/357AB, 2019'))