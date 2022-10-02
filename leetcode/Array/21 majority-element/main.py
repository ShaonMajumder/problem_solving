# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        max = 0
        max_key = 0
        for key in dict:
            if dict[key] > max:
                max = dict[key]
                max_key = key
        return max_key