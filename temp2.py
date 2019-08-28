def doubles(maxk, maxn):
    # your code
    import math
    s = 0.0
    for i in range(1, maxk + 1):
        for j in range(1, maxn + 1):
            s = s + (1/(i*(math.pow(j+1 ,2*i))))
    return s

k = int(input())
n = int(input())
print(doubles(k, n))
