class Solution:
    def romanToInt(self, s):
        number=0
        roman = {'M':1000, 'D':500,'C':100,'L':50, 'X':10, 'V':5,'I':1}
        for i in range(0, len(s)-1):
            if (roman[s[i]]<roman[s[i+1]]):
                number = number - roman[s[i]]
                #print(number)
                       
            else:
                number = number + roman[s[i]]
                #print(number)
                
        return number+roman[s[-1]] 
        

s = Solution()
                               
print(s. romanToInt('MCMXCIV'))
                        
                               
                
                         
