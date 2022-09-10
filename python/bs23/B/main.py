import math
pi = math.acos(-1.0)

def theArea(r):
    circle_area = pi*r*r
    square_area = 4*r*r
    return square_area - circle_area


n = int(input())
inputs = [ float(input()) for i in range(n)]

c = 1
for i in inputs:
    print('Case '+str(c)+': ' +  "{0:.2f}".format(theArea(i)))
    c = c + 1
