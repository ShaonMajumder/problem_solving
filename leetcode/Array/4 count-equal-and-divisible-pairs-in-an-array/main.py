# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
class Solution:
    def countPairs(self, nums, k):
        number_of_pairs = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and ( ( i * j ) % k == 0 ):
                    number_of_pairs += 1
        return number_of_pairs

s = Solution()
print(s.countPairs( [3,1,2,2,2,1,3], 2))