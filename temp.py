def ordertest(A):
    if(len(A)>1):
        for i in range( len(A) - 1 ):
            if int(A[i]) < int(A[i+1]):
                return False
        return True
    else:
        return False

def next_bigger(n):
    #your code here
    import copy
    x = str(n)
    if(ordertest(x)):
        return -1
    else:
        for i in range(1, len(x)):
            s = copy.copy(x)
            b = list(map(int, s[len(s)-i-1:len(s)-i+1]))
            b.sort(reverse=True)
            b = list(map(str, b))
            b = "".join(b)
            print(b)
            print(s[i-1:i])
            if(len(x)%2!=0):
                if(i<len(s)/2):
                    s = s[i-1:i] + b
                else:
                    s = b + s[len(s)-i:len(s)-i-2]
            else:
                if(i<len(s)/2):
                    s = s[i-1:i+1] + b
                else:
                    s = b + s[len(s)-i-2:len(s)-i-1]
            print(s)
            if(int(s)>n):
                print("#1")
                return int(s)
            print("#2")
        return -1

n =int(input())
print(int(next_bigger(n)))
    
