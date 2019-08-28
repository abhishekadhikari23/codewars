def last_digit(lst):
    # Your Code Here
    pass
    c = 0
    b = 0
    a = 1
    a = lst[len(lst)-1]
    for i in range(len(lst), 1, -1):
        print(a)
        b = lst[i-2]
        print(b)
        print(b**a)
        a = (b**a)%10
        print("#" + str(a))
    return a

print(last_digit([12, 30, 21]))
        
