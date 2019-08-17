'''
#2019-08-17

            https://www.codewars.com/kata/html-complementary-color/

Hi there! You have to implement the
get_reversed_color(hex_color) (Python, Ruby, Haskell)
or getReversedColor(hexColor) (JavaScript, Java) function that takes a hex-color string and returns the string represents the complementary color.
What is the hex-color? You can find the answer on w3schools and Wikipedia
Input
It takes only one argument - string with hex value (case-ignored with chars 0..9 or A..F) without hash-char "#". Argument hex_color is not necessarily
with 6-digits length - rest of digits are filled by zeros:
"a23" <=> "000a23"
"" <=> "0" <=> "000000"

Output
Output is the upper-cased string contains of the hash character (#) and complementary color. Complementary color is some color which gives completely
white color in sum with entered one: #000A23 + #FFF0DD = #FFFFFF
Errors
If the entered string is incorrect: length is 7+, has non-hexadecimal characters or non-string type, then the Error(IllegalArgumentException - Java)
should be raised/thrown or Nothing should be returned in Haskell.
>>> getReversedColor("00fffff")
Uncaught Error: Incorrect string length
>>> getReversedColor("00ffZZ")
Uncaught Error: Non-hex chars
>>> getReversedColor(112233)
Uncaught Error: Incorrect string type

Examples
>>> get_reversed_color("01fD08")
"#FE02F7"
>>> get_reversed_color("")
"#FFFFFF"
>>> get_reversed_color("a23")
"#FFF5DC"
'''


def get_reversed_color(hex_color):
    # Your code goes here.
    hex_color = hex_color.upper()
    if(isinstance(hex_color, str)==0):
        raise ValueError("Incorrect string type")
    if(len(hex_color)<7):
        if(len(hex_color)<6):
            for i in range(0,(6-len(hex_color))):
                hex_color = '0' + hex_color
    else:
        raise ValueError("Incorrect string length")
        return
    for i in range(0,6):
        if((ord(hex_color[i])>=48 and ord(hex_color[i])<=57) or (ord(hex_color[i])>=65 and ord(hex_color[i])<=70)):
            pass
        else:
            raise ValueError("Non-hex chars")           
    hex_color = hex_color.replace('A', chr(58))
    hex_color = hex_color.replace('B', chr(59))
    hex_color = hex_color.replace('C', chr(60))
    hex_color = hex_color.replace('D', chr(61))
    hex_color = hex_color.replace('E', chr(62))
    hex_color = hex_color.replace('F', chr(63))
    hex_color = list(hex_color)
    for i in range(0,6):
        hex_color[i] = chr(111 - ord(hex_color[i]))
    hex_color = "".join(hex_color)
    hex_color = hex_color.replace(chr(58), 'A')
    hex_color = hex_color.replace(chr(59), 'B')
    hex_color = hex_color.replace(chr(60), 'C')
    hex_color = hex_color.replace(chr(61), 'D')
    hex_color = hex_color.replace(chr(62), 'E')
    hex_color = hex_color.replace(chr(63), 'F')
    return '#' + hex_color

s = input()
print(get_reversed_color(s))

'''By Abhishek Adhikari'''
