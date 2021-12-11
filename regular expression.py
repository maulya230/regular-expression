# ^ match the start of the line
# . Match any character
# * many times

# import re
# x = "My 2 favourite numbers are 19 and 42"
# y = re.findall('[0-9]+',x)
# print(y)

# y = re.findall('[AEIOU]+',x)
# greedy matchiing repeat character (* and +) push outward in both directions (greedy)
#  to match the largest possible string
import re
from sre_constants import BIGCHARSET
x = 'From: using the: character'
y = re.findall('^F.+:', x)
print(y)

# non greedy matching
#if you add + and * chill out a bit

import re
x = 'From: Using the: character'
y = re.findall('^F.+?:', x)
print(y)

#fine tuning string extraction you can refine the
#match for re.findall() and separately determines
#which portion of the match is to be extracted by using parentheses

y = re.findall('\S+@\S+',x)
print(y)

