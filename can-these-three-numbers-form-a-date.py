'''
#2019-08-17
Sorry this time I made the program extremely lengthy as I was feeling
very sleepy that night. Need your help!

            https://www.codewars.com/kata/can-these-three-numbers-form-a-date/

You are given three integers in the range [0-99]. You must determine if
any ordering of the numbers forms a date from the 20th century.

If no ordering forms a date, return the string "invalid".

If multiple distinct orderings form dates, return the string "ambiguous".

If only one ordering forms a date, return that date as a string with format
"YY/MM/DD".

Examples
unique_date(13, 12, 77) == '77/12/13' # only the ordering (77, 12, 13)
                                        forms a date
unique_date(13, 77, 12) == '77/12/13' # argument order is irrelevant

unique_date(1, 2, 3) == 'ambiguous' # 01/02/03, 02/01/03, ...
unique_date(3, 2, 1) == 'ambiguous'

unique_date(50, 40, 60) == 'invalid' # no ordering could form a date
unique_date(40, 50, 60) == 'invalid'

'''

def unique_date(x, y, z):
    pass
    if(x > y):
        t = x
        x = y
        y = t
    if(y > z):
        t = y
        y = z
        z = t
    if(x < y):
        t = x
        x = y
        y = t
    if(x == y and y == z and z == x and x >= 1):
        if(x <= 12):
            res = [ str(z), '/', str(y), '/', str(x)]
        else:
            res = ['invalid']
    elif(x!=y and y == z and x < 32 and y <= 12 and x >= 1 and y >= 1):
        if(x <= 12):
            res = ['ambiguous']
        else:
            res = [str(z), '/', str(y), '/', str(x)]
    elif( x == y and y!=z and y <= 12 and x >= 1):
        if(z <= 31 and y >= 1):
            res = ['ambiguous']
        else:
            res = [str(z), '/', str(y), '/', str(x)]
    elif( x == z and x < 32 and y <= 12 and y!=x and x >= 1 and y >= 1):
        if(x <= 12 and y >= 1):
            res = ['ambiguous']
        else:
            res = [str(z), '/', str(y), '/', str(x)]
    elif( x!=y and y!=z and z!=x and x < 32 and y <= 12):
        if(x < 31 and z < 31 and y >= 1 and z > 0 and ((y <= 6 and y%2 == 0) or (y > 8 and y%2!=0)) and y!=2):
            res = ['ambiguous']
        elif(x < 32 and z < 32 and y >= 1 and z > 0 and ((y <= 7 and y%2!=0) or (y >= 8 and y%2 == 0)) and y!=2):
            res = ['ambiguous']    
        elif(y <= 12 and x <= 12 and y >= 1 and z > 0 and y!=2):
            res = ['ambiguous']
        elif(y == 2):
            if(x > 28):
                return 'invalid'
            elif(x <= 28):
                if(z <= 28):
                    return 'ambiguous'
                elif(x <= 12):
                    return 'ambiguous'
                else:
                    res = [str(z), '/', str(y), '/', str(x)]
                    if(int(res[0])<10):
                        res[0] = '0' + res[0]
                    if(int(res[2])<10):
                        res[2] = '0' + res[2]
                    if(int(res[4])<10):
                        res[4] = '0' + res[4]
                    res = "".join(res)
                    return res
        elif( x <= 12 and z <= 12 and y == 0):
            res = ['ambiguous']
        elif(y == 0):
            res = [str(y), '/', str(x), '/', str(z)]
        else:
            res = [str(z), '/', str(y), '/', str(x)]
    
    else:
        res = ['invalid']
    if(res[0] == 'invalid' or res[0] == 'ambiguous'):
        pass
    else:
        if(int(res[0])<10):
            res[0] = '0' + res[0]
        if(int(res[2])<10):
            res[2] = '0' + res[2]
        if(int(res[4])<10):
            res[4] = '0' + res[4]
    res = "".join(res)
    return res

a = int(input())
b = int(input())
c = int(input())
print(unique_date(a,b,c,))

'''By Abhishek Adhikari
