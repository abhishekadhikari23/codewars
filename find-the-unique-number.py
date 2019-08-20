'''
#2019-08-20

            https://www.codewars.com/kata/585d7d5adb20cf33cb000235/

There is an array with some numbers. All numbers are equal except for one.
Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique
'''
def find_uniq(arr):
    # your code here
    start = arr[0]
    arr.append(start)
    for i in range(1, len(arr)-1):
        if(arr[i]!=start):
            if(arr[i+1] == start):
                return arr[i]
            else:
                return start
        else:
            if(arr[i+1]!= start):
                return arr[i+1]          

s = input()
print(find_uniq(list(map(int, s.split()))))

'''By Abhishek Adhikari'''
