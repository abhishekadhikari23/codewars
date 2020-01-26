def is_polydivisible(s, b):
    for i in range(0,len(s)):
        if int(s[:i+1],b)%(i+1)!=0:
            return False
    return True

def base10toN(num, base):
    """Change ``num'' to given base
    Upto base 36 is supported."""

    converted_string, modstring = "", ""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return converted_string

def get_polydivisible(n, b):
    nu = 0
    i = 1
    while True:
        if is_polydivisible(str(nu),b):
            if i == n:
                return base10toN(nu,b)
            i=i+1
            print(nu)
        nu=nu+1

    return None

print(is_polydivisible("1232", 10))
print(is_polydivisible("123220", 10))
print(is_polydivisible("13", 10))
print(get_polydivisible(22, 10))
print(get_polydivisible(42, 10))