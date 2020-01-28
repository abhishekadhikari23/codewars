'''
    #2020-01-28
    https://www.codewars.com/kata/58c5577d61aefcf3ff000081
    Rail Fence Cipher: Encoding and Decoding

    Create two functions to encode and then decode a string using the Rail Fence Cipher. This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails". First start off moving diagonally and down. When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail. Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string.

For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:

W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C  
    A       I       V       D       E       N    
The encoded string would be:

WECRLTEERDSOEEFEAOCAIVDEN
Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.

Write a second function/method that takes 2 arguments, an encoded string and the number of rails, and returns the DECODED string.

For both encoding and decoding, assume number of rails >= 2 and that passing an empty string will return an empty string.

Note that the example above excludes the punctuation and spaces just for simplicity. There are, however, tests that include punctuation. Don't filter out punctuation as they are a part of the string.
'''


def encode_rail_fence_cipher(text, key):
    rail = [['\n' for i in range(len(text))] 
                  for j in range(key)] 
      
    # to find the direction 
    dir_down = False
    row, col = 0, 0
      
    for i in range(len(text)): 
          
        # check the direction of flow 
        # reverse the direction if we've just 
        # filled the top or bottom rail 
        if (row == 0) or (row == key - 1): 
            dir_down = not dir_down 
          
        # fill the corresponding alphabet 
        rail[row][col] = text[i] 
        col += 1
          
        # find the next row using 
        # direction flag 
        if dir_down: 
            row += 1
        else: 
            row -= 1
    # now we can construct the cipher  
    # using the rail matrix 
    result = [] 
    for i in range(key): 
        for j in range(len(text)): 
            if rail[i][j] != '\n': 
                result.append(rail[i][j]) 
    return("" . join(result)) 
    
def decode_rail_fence_cipher(cipher, key):
    rail = [['\n' for i in range(len(cipher))]  
                  for j in range(key)] 
      
    # to find the direction 
    dir_down = None
    row, col = 0, 0
      
    # mark the places with '*' 
    for i in range(len(cipher)): 
        if row == 0: 
            dir_down = True
        if row == key - 1: 
            dir_down = False
          
        # place the marker 
        rail[row][col] = '*'
        col += 1
          
        # find the next row  
        # using direction flag 
        if dir_down: 
            row += 1
        else: 
            row -= 1
              
    # now we can construct the  
    # fill the rail matrix 
    index = 0
    for i in range(key): 
        for j in range(len(cipher)): 
            if ((rail[i][j] == '*') and
               (index < len(cipher))): 
                rail[i][j] = cipher[index] 
                index += 1
          
    # now read the matrix in  
    # zig-zag manner to construct 
    # the resultant text 
    result = [] 
    row, col = 0, 0
    for i in range(len(cipher)): 
          
        # check the direction of flow 
        if row == 0: 
            dir_down = True
        if row == key-1: 
            dir_down = False
              
        # place the marker 
        if (rail[row][col] != '*'): 
            result.append(rail[row][col]) 
            col += 1
              
        # find the next row using 
        # direction flag 
        if dir_down: 
            row += 1
        else: 
            row -= 1
    return("".join(result)) 