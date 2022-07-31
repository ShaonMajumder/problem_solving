# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        maximum = 0
        max_index = 0
        for i in range(1,length):
            if prices[i] > maximum:
                maximum = prices[i]
                max_index = i

        max_profit = 0
        for i in range(length):
            if  maximum - prices[i] > max_profit and max_index > i:
                max_profit = maximum - prices[i]
                # print(f"{maximum} - {prices[i]}")
        return max_profit
                
        # lowest = prices[0]
        # lowest_index = 0
        # for i in range(length-1):
        #     if prices[i] < lowest:
        #         lowest = prices[i]
        #         lowest_index = i
            
        # max_profit = 0
        
        # for i in range(lowest_index+1,length):
        #     if prices[i] - lowest > max_profit:
        #         max_profit = prices[i] - lowest
        # return max_profit

s = Solution()
# print( s.maxProfit([7,6,4,3,1]) )
print( s.maxProfit([2,1,2,1,0,1,2]) )