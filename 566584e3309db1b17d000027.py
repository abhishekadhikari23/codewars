'''
   #2020-01-20
   
   Differentiate a polynomial
   https://www.codewars.com/kata/566584e3309db1b17d000027/

   Create a function that differentiates a polynomial for a given value of x.

Your function will receive 2 arguments: a polynomial as a string, and a point to evaluate the equation as an integer.

Assumptions:
There will be a coefficient near each x, unless the coefficient equals 1 or -1.
There will be an exponent near each x, unless the exponent equals 0 or 1.
All exponents will be greater or equal to zero
Examples:
differenatiate("12x+2", 3)      ==>   returns 12
differenatiate("x^2+3x+2", 3)   ==>   returns 9
'''


def calc(eq,p):
    coef_s = ''
    flag = 0
    for i in range(0,len(eq)):
        if eq[i]=='x' or eq[i]=='X':
            flag = 1
    if flag:
        if eq[0]!= 'x' and eq[0]!= 'X':
            coef_s=coef_s+eq[0]
            j = 1
            while j<len(eq) and eq[j] != 'x' and eq[j] != 'X':
                coef_s=coef_s+eq[j]
                j=j+1
            coef=int(coef_s)
            i=j+1
        else:
            i=1
            coef = 1
        if i<len(eq):
            j=i+1
            exp_s=eq[j]
            j=j+1
            while j<len(eq):
                exp_s=exp_s+eq[j]
                j=j+1
            exp=int(exp_s)
        else:
            exp = 1
        #print(f"{eq} : {coef*exp*pow(p,exp-1)}")
        return coef*exp*pow(p,exp-1)
    else:
        #print(f"{eq} : 0")
        return 0



def differentiate(equation, point):
    sum = 0
    i = 0
    op = ''
    if equation[0]!='-':
        op = op+'+'
        for i in range(1,len(equation)):
            if equation[i] =='+' or equation[i]=='-':
                op = op+equation[i]
    else:
        for i in range(0,len(equation)):
            if equation[i] =='+' or equation[i]=='-':
                op = op+equation[i]

    i=0
    #print(op)  //  Used for debugging list of operators
    op_id=0
    while i<len(equation):
        s = ''
        j = i
        if equation[j] not in {'+','-',' '}:
            s = s+equation[j]
            j+=1
            if j<len(equation):
                while equation[j] not in {'+','-',' '}:
                    s = s+equation[j]
                    j+=1
                    if j>=len(equation):
                        break
            i=j
        else:
            i=j+1
        if len(s)>0:        
            if op[op_id]=='+':
                sum = sum + calc(s,point)
                op_id=op_id+1
            else:
                sum = sum - calc(s,point)
                op_id=op_id+1
    return sum

print(differentiate("-5x^2+10x+4", 3))