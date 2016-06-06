# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

# Programmer Notes: The code is also contained within a Gist--created the code in Jupyter: 
# https://gist.github.com/a2f79db22757a127a96d4dfbb2c8f905


def donuts(count):
    try:
        count = int(count)
    except Exception:
        return "Ack, enter in an integer next time, ok?!"
    
    if count <= 10:
        return "Number of donuts: {0}".format(count)
    elif count > 10:
        return "Number of donuts: many"
    
donuts("disruptive uber-esque thin layer innovation through value chain optimization ")




""" BOTH ENDS    
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
"""
def both_ends(s):     
    if len(s) >= 2:
        return s[0:2]+ s[-2:]

print(both_ends("spring"))



""" FIX START  
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.
"""

import re
def fix_start(s):
    return(s[0:1] + re.sub(s[0:1], '*', s[1:]))

# I feel pretty embarrased by this hacky solution. 
# Once done with the prework, I'll spend a little time on a regex refresher
print(fix_start("babble"))


""" MIX UP
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

"""
def mix_up(a, b):
    return b[0:2]+ a[2:] + " " +  a[0:2]+ b[2:]
    #return ''.join([ b[0:2],a[2:],' ', a[0:2]+ b[2:] ])

mix_up("dog", "dinner")



""" VERBING
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
"""

def verbing(s):
    if len(s)>= 3:
        if s[-3:]=="ing":
            return s+ "ly"
        elif s[-3] != "ing":
            return s+ "ing"
        else:
            return s+"ingly"
    else:
        return s

verbing('do')


""" NOT BAD
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
"""

import re

def not_bad(s):
    return re.sub(r'not.*bad', 'good', s, flags=re.IGNORECASE)

not_bad("This tea is not hot")


 """FRONT_BACK
    
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
"""

def half_len(s):
    if len(s) % 2 == 0:
        half_len = int(len(s)/2)
    else:
        half_len = int(len(s)/2) + 1
    return half_len


def front_back(s1,s2):
    s1_half = half_len(s1)
    s2_half = half_len(s2)
    
    return s1[0:s1_half] + s2[0:s2_half] + s1[s1_half:] + s2[s2_half:]

front_back('Kitten', 'Donut')