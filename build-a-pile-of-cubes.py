'''
#2019-08-18

        https://www.codewars.com/kata/build-a-pile-of-cubes/

Your task is to construct a building which will be a pile of n cubes.
The cube at the bottom will have a volume of n^3, the cube above will
have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.

You are given the total volume m of the building. Being given m can you find
the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb) will be an
integer m and you have to return the integer n such as
n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

Examples:
findNb(1071225) --> 45
findNb(91716553919377) --> -1
mov rdi, 1071225
call find_nb            ; rax <-- 45

mov rdi, 91716553919377
call find_nb            ; rax <-- -1
'''

def find_nb(m):
    # your code
    import math
    s = 0
    i = 0
    while(s < m):
        #s = int(i*(i+1)*i*(i+1)/4)  this method is giving error
        s = s + (i*i*i)
        i = i + 1
    ''' used for debugging
    print(s)
    print(int(s))
    print(i*(i+1)*i*(i+1)/4)
    print(int(i*(i+1)*i*(i+1)/4))
    print(m)
    print(int(m))'''
    if(int(s) == m):
        return i-1
    else:
        return (-1)

n = input("Enter the total volume")
print(find_nb(int(n)))

'''By Abhishek Adhikari'''
