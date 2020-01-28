'''
    #2020-01-28
    https://www.codewars.com/kata/5657d8bdafec0a27c800000f/
    Compute-A-Convex-Hull

    The Problem
Consider a flat board with pegs sticking out of one side. If you stretched a rubber band across the outermost pegs what is the set of pegs such that all other pegs are contained within the shape formed by the rubber band?

alt text

More specifically, for this kata you will be given a list of points represented as [x,y] co-ordinates. Your aim will be to return a sublist containing points that form the perimeter of a polygon that encloses all other points contained within the original list.

Notes:
The tests may include duplicate and/or co-linear points. Co-linear points are a set of points which fall on the same straight line. Neither should be included in your returned sublist

For simplicity, there will always be at least 3 points

Help:
Check out wikipedia's page on convex hulls

Note for python users: scipy module has been disabled.
'''


from functools import reduce

def convex_hull_graham(points):
    '''
    Returns points on convex hull in CCW order according to Graham's scan algorithm. 
    By Tom Switzer <thomas.switzer@gmail.com>.
    '''
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l

def hull_method(pointlist):
    pass
    return convex_hull_graham(pointlist)