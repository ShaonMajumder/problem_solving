class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n == -1:
            return 1/x
        
        if n % 2 == 0:
            half = self.myPow(x,n/2)
            return half*half
        if n % 2 == 1:
            half = self.myPow(x,(n-1)/2)
            return half*half*x
            # even number -> half*half creates an extra 1/x which is eleminated by * x
        # when recursion failed
        # used concept of dynamic programming