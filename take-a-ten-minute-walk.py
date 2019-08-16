'''


        https://www.codewars.com/kata/take-a-ten-minute-walk/


You live in the city of Cartesia where all roads are laid out in a perfect grid.
You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends
you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only
a single block in a direction and you know it takes you one minute to traverse one city block, so create a function
that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!)
and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only).
It will never give you an empty array (that's not a walk, that's standing still!).
'''
def isValidWalk(walk):
    #determine if walk is valid
    pass
    i=0
    j=0
    x=0
    y=0
    if (len(walk)==10):
        for i in range(0,10):
            if (walk[i]=='n'):
                y=y+1
            elif (walk[i]=='s'):
                y=y-1
            elif (walk[i]=='e'):
                x=x+1
            else:
                x=x-1
        if(x==0 and y==0):
            return True
        else:
            return False
    else:
        return False

data=input("Enter the string: ")
if(isValidWalk(data)==True):
    print("True")
else:
    print("False")

'''By Abhishek Adhikari'''
