import numpy
Co = list( map(float,input().split()) )
x = float( input() )
print( numpy.polyval(Co, x ) )