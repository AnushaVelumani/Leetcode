class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(0, len(nums2)):
            nums1.insert(m, nums2[i])
        
        x = m +n
         
        del nums1[x:]
        nums1.sort()
    
        return

    
s=Solution()

s.mergeTwoLists([2,4,6],[1,3,5])


