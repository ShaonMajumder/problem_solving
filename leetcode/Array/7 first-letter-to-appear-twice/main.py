# https://leetcode.com/problems/first-letter-to-appear-twice/submissions/
class Solution:
    def repeatedCharacter(self, s):
        # dic = {}
        # for i in s:
        #     if i in dic:
        #         return i
        #     dic[i] = 0
        # return None

        dic = defaultdict(lambda: 0)
        for i in s:            
            dic[i] += 1
            if dic[i] > 1:
                return i
        return None
s = Solution()
print( s.repeatedCharacter("asdfa") )