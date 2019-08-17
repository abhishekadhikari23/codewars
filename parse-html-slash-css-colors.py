'''
#2019-08-17

                https://www.codewars.com/kata/parse-html-slash-css-colors/

In this kata you parse RGB colors represented by strings. The formats are primarily used in HTML and CSS. Your task is to
implement a function which takes a color as a string and returns the parsed color as a map (see Examples).

Input:
The input string represents one of the following:

6-digit hexadecimal - "#RRGGBB"
e.g. "#012345", "#789abc", "#FFA077"
Each pair of digits represents a value of the channel in hexadecimal: 00 to FF
3-digit hexadecimal - "#RGB"
e.g. "#012", "#aaa", "#F5A"
Each digit represents a value 0 to F which translates to 2-digit hexadecimal: 0->00, 1->11, 2->22, and so on.
Preset color name
e.g. "red", "BLUE", "LimeGreen"
You have to use the predefined map PRESET_COLORS (JavaScript, Python, Ruby), presetColors (Java, C#, Haskell),
or preset-colors (Clojure). The keys are the names of preset colors in lower-case and the values are the corresponding
colors in 6-digit hexadecimal (same as 1. "#RRGGBB").

Examples:
parse_html_color('#80FFA0')   # => {'r': 128, 'g': 255, 'b': 160}
parse_html_color('#3B7')      # => {'r': 51,  'g': 187, 'b': 119}
parse_html_color('LimeGreen') # => {'r': 50,  'g': 205, 'b': 50 }
'''

PRESET_COLORS = {'limegreen':'#32CD32'} #codewars PRESET_COLORS map has more colors

def parse_html_color(color):
    pass
    if(color[0]!='#'):
        color = PRESET_COLORS[color.lower()]
        color = color[1:]
    else:
        color = color[1:]
        if(len(color)==3):
            color = color[0] + color[0] + color[1] + color[1] + color[2] + color[2]
    color = color.upper()
    color = color.replace('A' , chr(58))
    color = color.replace('B' , chr(59))
    color = color.replace('C' , chr(60))
    color = color.replace('D' , chr(61))
    color = color.replace('E' , chr(62))
    color = color.replace('F' , chr(63))
    r = ((ord(color[0])-48)*16) + ((ord(color[1])-48))
    g = ((ord(color[2])-48)*16) + ((ord(color[3])-48))
    b = ((ord(color[4])-48)*16) + ((ord(color[5])-48))
    return {'r':r,'g':g,'b':b}


s = input("Enter color name or code : ")
print(parse_html_color(s))

'''By Abhishek Adhikari'''

