'''
#2019-08-23
            https://www.codewars.com/kata/snail/

Snail Sort
Given an n x n array, return the array elements arranged from outermost
elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array
consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]


NOTE: The idea is not sort the elements from the lowest value to the highest;
the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as [[]]
'''

def snail(array):
    pass
    n = len(array)
    a = []
    if(n>1):
        b = n-1
        c = 0
        d = n-1
        for i in range(0, n):
            for j in range(i, b+1):
                a.append(array[i][j])
            for j in range(i+1, b+1):
                a.append(array[j][b])
            for j in range(b-1, i-1, -1):
                a.append(array[b][j])
            for j in range(b-1, i, -1):
                a.append(array[j][i])      
            b = b-1
        return a
    elif(n == 1 and not any(array)):
        return a
    else:
        a.append(array[0][0])
        return a       
            

print(snail([[1,2,3,10],
         [8,9,4,11],
         [7,6,5,12],
         [13,14,15,16]]))

'''By Abhishek Adhikari'''
