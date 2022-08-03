# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# refernce https://www.geeksforgeeks.org/maximum-difference-between-two-elements/
class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        if length > 1:
            min_element = prices[0]
            max_diff = prices[1] - min_element
            
            for i in range(1,length):
                if prices[i] - min_element > max_diff:
                    max_diff = prices[i] - min_element
                if prices[i] < min_element:
                    min_element = prices[i]
            return max_diff if max_diff >= 0 else 0
        else:
            return 0       

s = Solution()
# print( s.maxProfit([7,6,4,3,1]) )
# print( s.maxProfit([2,1,2,1,0,1,2]) )
print( s.maxProfit([7,6,4,3,1]) )