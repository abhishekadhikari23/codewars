'''
#2019-08-21

            https://www.codewars.com/kata/common-denominators/

Common denominators
You will have a list of rationals in the form
 { {numer_1, denom_1} , ... {numer_n, denom_n} } 
or
 [ [numer_1, denom_1] , ... [numer_n, denom_n] ] 
or
 [ (numer_1, denom_1) , ... (numer_n, denom_n) ] 
where all numbers are positive ints.

You have to produce a result in the form
 (N_1, D) ... (N_n, D) 
or
 [ [N_1, D] ... [N_n, D] ] 
or
 [ (N_1', D) , ... (N_n, D) ] 
or
{{N_1, D} ... {N_n, D}} 
or
"(N_1, D) ... (N_n, D)"
depending on the language (See Example tests)
in which D is as small as possible and
 N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
Example:

convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe`
[(6, 12), (4, 12), (3, 12)]

'''
def find_lcm(num1, num2): 
	if(num1>num2): 
		num = num1 
		den = num2 
	else: 
		num = num2 
		den = num1 
	rem = num % den 
	while(rem != 0): 
		num = den 
		den = rem 
		rem = num % den 
	gcd = den 
	lcm = int(int(num1 * num2)/int(gcd)) 
	return lcm
    
def lcm_list(l):
    num1 = l[0] 
    num2 = l[1] 
    lcm = find_lcm(num1, num2) 
    for i in range(2, len(l)):
        lcm = find_lcm(lcm, l[i])
    return lcm
	
def convertFracts(lst):
    t = []
    if(len(lst)>0):
        for i in range(0, len(lst)):
            t.append(lst[i][1])
        l = lcm_list(t)
        w, h = 2, len(lst);
        ans = [[0 for x in range(w)] for y in range(h)]
        for i in range(0, len(lst)):
            ans[i][1] = l
            ans[i][0] = lst[i][0]*int(l/lst[i][1])
        return ans
    else:
        return t

print(convertFracts([[1, 2], [1, 3], [1, 4]]))# example

'''By Abhishek Adhikari'''
