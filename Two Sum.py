class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in range (0,l-1):
            new_range= nums[i+1:]
            ans = target-nums[i]
            if ans in new_range:
                return (i, new_range.index(ans)+i+1)
            

    
    
