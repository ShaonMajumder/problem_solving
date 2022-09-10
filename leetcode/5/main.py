# https://leetcode.com/problems/next-greater-element-i/submissions/
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        answer = -1
        answers = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in range(j+1,len(nums2)):
                        if nums2[k] > nums2[j]:
                            answer = nums2[k]
                            break

            answers.append(answer)
            answer = -1
                   
        return answers

nums1 = [4,1,2]
nums2 = [1,3,4,2]

s = Solution()
print( s.nextGreaterElement(nums1,nums2) )