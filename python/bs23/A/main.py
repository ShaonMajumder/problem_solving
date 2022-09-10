# Find a minimum possible integer which has unique digits and Σdi = X. Here di represents each digits in that integer.

def distinctNumber(n):
    if n < 10:
        return n
    else:
        for i in range(9,1, -1):
            if n - i > 9:
                return -1
            elif n - i >= 1:
                if str(n-i) == str(i):
                    pass
                else:
                    return str(n-i)+str(i)
        return -1

n = int(input())
inputs = [ int(input()) for i in range(n)]
for i in inputs:
    print(distinctNumber(i))