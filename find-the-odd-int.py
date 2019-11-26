'''
    #2019-11-26

    https://www.codewars.com/kata/find-the-odd-int/

Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

'''

def find_it(seq):
    n = len(seq)
    for i in range(0,n):
        l = 0
        t = seq[i]
        for j in range(0,n):
            if(t == seq[j]):
                l = l + 1
        if(l%2!=0):
            return t
    return None

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))