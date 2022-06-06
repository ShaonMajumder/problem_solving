import numpy
N,M = list(map(int,input().split()))
A = numpy.array( [ list(map(float,input().split())) for i in range(N) ] )
print( numpy.mean(A, axis = 1) )
print( numpy.var(A, axis = 0) )
print( numpy.around( numpy.std(A) , 11) )