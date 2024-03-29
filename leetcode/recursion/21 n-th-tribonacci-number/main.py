# https://leetcode.com/problems/n-th-tribonacci-number/
class Solution:
    def tribonacci(self, n: int) -> int:
        """
        # recursion
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        """
        
        f = [0,1,1]
        for i in range(3,n+1):
            f.append(f[i-1]+f[i-2]+f[i-3])
        return f[n]
        
        # dynamic programming