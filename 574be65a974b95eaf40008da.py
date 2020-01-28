'''
    #2020-01-28
    https://www.codewars.com/kata/574be65a974b95eaf40008da
    T.T.T.#2: Equal to 24

    They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. Series #2:
Equal to 24

This is the simple version of Fastest Code : Equal to 24.

Task
A game I played when I was young: Draw 4 cards from playing cards, use + - * / and () to make the final results equal to 24.

You will coding in function equalTo24. Function accept 4 parameters a b c d(4 cards), value range is 1-13.

The result is a string such as "2*2*2*3" ,(4+2)*(5-1); If it is not possible to calculate the 24, please return "It's not possible!"

All four cards are to be used, only use three or two cards are incorrect; Use a card twice or more is incorrect too.

You just need to return one correct solution, don't need to find out all the possibilities.

Some examples:
equalTo24(1,2,3,4) // can return "(1+3)*(2+4)" or "1*2*3*4"
equalTo24(2,3,4,5) // can return "(5+3-2)*4" or "(3+4+5)*2"
equalTo24(3,4,5,6) // can return "(3-4+5)*6"
equalTo24(1,1,1,1) // should return "It's not possible!"
equalTo24(13,13,13,13) // should return "It's not possible!"

'''


import operator
from itertools import product, permutations
 
def mydiv(n, d):
    return n / d if d != 0 else 9999999
 
syms = [operator.add, operator.sub, operator.mul, mydiv]
op = {sym: ch for sym, ch in zip(syms, '+-*/')}
def equal_to_24(a,b,c,d):
    nums = []
    nums.append(a)
    nums.append(b)
    nums.append(c)
    nums.append(d)
    for x, y, z in product(syms, repeat=3):
        for a, b, c, d in permutations(nums):
            if round(x(y(a,b),z(c,d)),5) == 24:
                return f"({a} {op[y]} {b}) {op[x]} ({c} {op[z]} {d})"
            elif round(x(a,y(b,z(c,d))),5) == 24:
                return f"{a} {op[x]} ({b} {op[y]} ({c} {op[z]} {d}))"
            elif round(x(y(z(c,d),b),a),5) == 24:
                return f"(({c} {op[z]} {d}) {op[y]} {b}) {op[x]} {a}"
            elif round(x(y(b,z(c,d)),a),5) == 24:
                return f"({b} {op[y]} ({c} {op[z]} {d})) {op[x]} {a}"
    return "It's not possible!"