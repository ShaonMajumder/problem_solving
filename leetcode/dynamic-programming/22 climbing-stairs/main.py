class Solution:
    def climbStairs(self, n: int) -> int:
        """
        # recursion
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        """
        f = [1,2]
        for i in range(2,n+1):
            f.append(f[i-1]+f[i-2])
        return f[n-1]
        # dynamic programming