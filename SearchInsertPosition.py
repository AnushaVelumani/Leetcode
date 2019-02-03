class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        l=len(nums)
        
        if target>nums[-1]:
            return l
        for i,x in enumerate(nums):
            if x>=target:
                return i          




s = Solution()
print(s.searchInsert([1], 0))
