'''
   #2019-11-26

               https://www.codewars.com/kata/credit-card-mask

Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"
'''

# return masked string
def maskify(cc):
    n = len(cc)
    if(n<=4):
        return cc
    else:
        for i in range(0,len(cc)):
            cc = cc[0:i] + "#" + cc[i+1:len(cc)]
            if(i>(len(cc)-6)):
                break
        return cc            
    pass

cc = input()
print(maskify(cc))