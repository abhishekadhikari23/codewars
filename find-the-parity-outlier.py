'''
#2019-08-20

            https://www.codewars.com/kata/find-the-parity-outlier/

You are given an array (which will have a length of at least 3, but could
be very large) containing integers. The array is either entirely comprised
of odd integers or entirely comprised of even integers except for a single
integer N. Write a method that takes the array as an argument and returns
this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
'''


def find_outlier(integers):
    even = 0
    odd = 0
    import copy
    integer = copy.copy(integers)
    for i in range(0, len(integer)):
        if(integer[i] < 0):
            integer[i] = integer[i]*(-1)
    start = 0
    if(integer[0]%2 == 0):
        start = 1
        integer.append(0)
    else:
        integer.append(1)
    if(start):
        for i in range(1, len(integer)):
            if(integer[i]%2!=0 and (i+1) < len(integer)):
                if(integer[i+1]%2==0):
                    return integers[i]
                else:
                    return integers[0]
    else:
        for i in range(1, len(integer)):
            if(integer[i]%2==0 and i < (len(integer)-1)):
                if(integer[i+1]%2!=0):
                    return integers[i]
                else:
                    return integers[0]

s = input()
print(find_outlier(list(map(int, s.split()))))
            
