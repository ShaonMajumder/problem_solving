# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array
class Solution:
    def findKDistantIndices(self, nums, key, k):
        def checkJs(i,js,k):
            for b in js:
                if abs(i - b) <= k:
                    return True
            return False
            
        answers = []
        js = [i for i in range( len(nums) ) if nums[i] == key]
        for i in range(len(nums)):
            if checkJs(i,js,k):
                answers.append(i)
        return answers

nums = [3,4,9,1,3,9,5]
key = 9
k = 1
s = Solution()
print( s.findKDistantIndices(nums, key, k) )