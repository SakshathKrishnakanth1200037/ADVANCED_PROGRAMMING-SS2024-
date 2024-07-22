#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
def match_ends(words):
    """
    Given a list of strings, return the count of the number of
    strings where the string length is 2 or more and the first
    and last chars of the string are the same.
    """
    count = 0
    for eachWord in words:
        if len(eachWord) >= 2 and eachWord[0] == eachWord[-1]:
            count += 1
    return count

# B. front_x
def front_x(words):
    """
    Given a list of strings, return a list with the strings
    in sorted order, except group all the strings that begin with 'x' first.
    """
    xList = []
    otherList = []

    for eachWord in words:
        if eachWord[0].lower() == 'x':
            xList.append(eachWord)
        else:
            otherList.append(eachWord)

    xList = sorted(xList)
    otherList = sorted(otherList)
    return xList + otherList

# C. sort_last
def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in increasing
    order by the last element in each tuple.
    """
    def getLastElement(s): 
        return s[-1]
    
    return sorted(tuples, key=getLastElement)

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    """
    Test function to compare the result with the expected value.
    """
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

# Calls the above functions with interesting inputs.
def main():
    """
    Main function to test the match_ends, front_x, and sort_last functions.
    """
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print()
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

if __name__ == '__main__':
    # This condition checks if the script is being run directly (not imported as a module).
    # If true, it calls the main() function to execute the script.
    main()
