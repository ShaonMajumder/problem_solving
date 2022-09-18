def solution(S, B):
    # write your code in Python 3.6
    R = []
    
    B = [float(n) for n in B]
    S = float(S)
    
    for i in range(0,len(B)):
        divider = sum(B[i:])
        R.append( "%.2f" % round( S * B[i]/divider , 2 )  ) 
        S = S - S * B[i]/divider
    
    return R
    
print( solution("300.01" , ["300.00","200.00","100.00"]) )
print( solution("1.00" , ["0.05","0.95"]) )
