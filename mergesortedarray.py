class Solution:
    def merge(self, nums1, m, nums2, n):
        op=nums1[:m]+nums2[:n]
        return sorted(op)
        

s=Solution()

print(s.merge([1,2,3,6,4,0],4,[2,5,6],3))                 
