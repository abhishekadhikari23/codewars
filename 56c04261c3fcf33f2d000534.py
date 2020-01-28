'''
    #2020-01-28
    https://www.codewars.com/kata/56c04261c3fcf33f2d000534
    Magnet-Particles-in-Box

    Professor Chambouliard hast just discovered a new type of magnet material. He put particles of this material in a box made of small boxes arranged in K rows and N columns as a kind of 2D matrix K x N where K and N are postive integers. He thinks that his calculations show that the force exerted by the particle in the small box (k, n) is:

v(k, n) = \frac{1}{k(n+1)^{2k}}

The total force exerted by the first row with k = 1 is:

u(1, N) = \sum_{n=1}^{n=N}v(1, n) = \frac{1}{1.2^2} + \frac{1}{1.3^2}+...+\frac{1}{1.(N+1)^2}

We can go on with k = 2 and then k = 3 etc ... and consider:

S(K, N) = \sum_{k=1}^{k=K}u(k, N) = \sum_{k=1}^{k=K}(\sum_{n=1}^{n=N}v(k, n)) \rightarrow (doubles(maxk, maxn))

Task:
To help Professor Chambouliard can we calculate the function doubles that will take as parameter maxk and maxn such that doubles(maxk, maxn) = S(maxk, maxn)? Experiences seems to show that this could be something around 0.7 when maxk and maxn are big enough.

Examples:
doubles(1, 3)  => 0.4236111111111111
doubles(1, 10) => 0.5580321939764581
doubles(10, 100) => 0.6832948559787737
Notes:
In u(1, N) the dot is the multiplication operator.

Don't truncate or round: Have a look in "RUN EXAMPLES" at "assertFuzzyEquals".

link to symbol Sigma
'''

def doubles(maxk, maxn):
    # your code
    import math
    s = 0.0
    for i in range(1, maxk + 1):
        for j in range(1, maxn + 1):
            try:
                s = s + (1/(i*(math.pow(j+1 ,2*i))))
            except OverflowError:
                s = s + (1/(i*(float('inf'))))
    return s