class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (needle == ""):
            return 0
        else:
            if needle in haystack:
                return haystack.index(needle)
            else:
                return -1
             
            
