'''
#2019-08-21

            https://www.codewars.com/kata/human-readable-time/

Write a function, which takes a non-negative integer (seconds) as input and
returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''

def make_readable(seconds):
    # Do something
    hh = int(seconds/60/60)
    mm = int((seconds%3600)/60)
    ss = int((seconds%3600)%60)
    if(hh < 10):
        h = '0' + str(hh)
    else:
        h = str(hh)
    if(mm < 10):
        m = '0' + str(mm)
    else:
        m = str(mm)
    if(ss < 10):
        s = '0' + str(ss)
    else:
        s = str(ss)
    return h + ':' + m + ':' + s

s = int(input())
print(make_readable(s))

'''By Abhishek Adhikari'''
