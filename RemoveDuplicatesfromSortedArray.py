class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if len(nums)== 0:
            return 0
        
        while (len(nums)-1 > i):
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i = i+1
            
        l= len(nums)
        
        
