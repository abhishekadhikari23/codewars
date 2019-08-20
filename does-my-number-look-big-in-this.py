'''
#2019-08-20

        https://www.codewars.com/kata/does-my-number-look-big-in-this

A Narcissistic Number is a number which is the sum of its own digits,
each raised to the power of the number of digits in a given base.
In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
The Challenge:

Your code must return true or false depending upon whether the given number
is a Narcissistic number in base 10.

Error checking for text strings or other invalid inputs is not required,
only valid integers will be passed into the function.
'''

def narcissistic( value ):
    # Code away
    import math
    str1 = str(value)
    su = 0
    l = len(str1)
    for i in range(0,l):
        su = su + math.pow(int(str1[i]),l)
    if(su == value):
        return True
    else:
        return False

s = int(input())
print(narcissistic(s))

'''By Abhishek Adhikari'''
