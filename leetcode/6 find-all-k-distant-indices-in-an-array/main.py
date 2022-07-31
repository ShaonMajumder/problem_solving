class Solution:
    def findKDistantIndices(self, nums, key, k):
        answers = []
        js = [i for i in range( len(nums) ) if nums[i] == key]
        for i in range(len(nums)):
            if True in map(lambda b: abs(i - b) <= k , js ):
                answers.append(i)
        return answers

nums = [3,4,9,1,3,9,5]
key = 9
k = 1
s = Solution()
print( s.findKDistantIndices(nums, key, k) )