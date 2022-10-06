class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # iterate 1
        """
        zeros = []
        normals = []
        length = len(nums)
        j = 0
        for i in range(0,length):
            if nums[i] != 0:
                nums[j] = nums[i]
                j = j + 1
        
        for i in range(j,length):
            nums[i] = 0
        """
        # two pointer solution
            
        nextNonzero = 0
    
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nextNonzero], nums[i] = nums[i], nums[nextNonzero]
                nextNonzero += 1

        return nums