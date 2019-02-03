class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        open_braces = ['(','[','{']
        braces = {'}':'{', ']':'[',')':'('}
        
        if(len(s)%2 != 0):
            return False
               
        for i in s:
            if i in open_braces:
                stack.append(i)
                             
            else:
                if (len(stack)==0) or (stack.pop() != braces[i]):
                    return False
                
           
        return len(stack)==0
        
        
        
    
