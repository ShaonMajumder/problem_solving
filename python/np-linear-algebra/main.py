import numpy
N = int(input())
A = numpy.array( [ list(map( float, input().split() ) ) for i in range(N)] )
print( numpy.round( numpy.linalg.det( A ) , 2) ) 