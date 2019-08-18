'''
#2019-08-18

            https://www.codewars.com/kata/replace-with-alphabet-position/

Welcome.

In this kata you are required to, given a string, replace every letter with
its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3
12 15 3 11" (as a string)

'''

def alphabet_position(text):
    pass
    text = text.upper()
    res = ""
    for i in range(0,len(text)):
        if(text[i]!=" " and text[i].isalpha()):
            res = res + " " + str(ord(text[i])-64)
    res = res[1:]
    return res

s = input("Enter the string : ")
print(alphabet_position(s))

'''By Abhishek Adhikari'''
        
