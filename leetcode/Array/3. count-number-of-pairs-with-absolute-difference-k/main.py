# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/submissions/
class Solution:
    def countKDifference(self, nums, k):
        number_of_pairs = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i] - nums[j]) == k :
                    number_of_pairs = number_of_pairs + 1

        return number_of_pairs
s = Solution()
print(s.countKDifference([1,2,2,1],1))
