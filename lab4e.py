#!/usr/bin/env python3
# Author ID: eroshy

def is_digits(sobj):
    """
    Returns True if the string sobj contains only digits, False otherwise.
    """
    for ch in sobj:
        if not ch.isdigit():
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')

import lab4e

print(is_digits('65'))
# will output True
print(is_digits('1F'))
# will print False
print(is_digits('-12'))
# will print False