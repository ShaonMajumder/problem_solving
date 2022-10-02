class Solution:
    def fib(self, n: int) -> int:
        """
        recursion
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)
        # time complexity of T(2^N) and space complexity of T(N).
        """
        f = [0,1]
        for i in range(2,n+1):
            f.append(f[i-1]+f[i-2])
        return f[n]
        """
        dynamic programming
        time complexity of T(2^N) and space complexity of T(N).
        space complexity of O(n) and time complexity of T(n).
        """