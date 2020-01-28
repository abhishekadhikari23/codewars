'''
    #2020-01-28
    https://www.codewars.com/kata/5467e4d82edf8bbf40000155
    Descending Order

    Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
'''



def descending_order(num):
    num_s = [int(n) for n in str(num)]
    num_s.sort(reverse=True)
    ans = ''
    for i in num_s:
        ans = ans + str(i)
    return int(ans)
    # Bust a move right here