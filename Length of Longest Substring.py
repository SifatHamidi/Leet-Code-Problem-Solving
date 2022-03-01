class Solution:
  def lengthOfLongestSubstring(self,x):
          if len(set(x)) == len(x):
            return len(x)
          substring =str()
          maxLen = 1
          for i in x:
              if i not in substring:                      
                  substring = substring + i
                  maxLen = max(maxLen, len(substring))
              else:                                       
                  break 
          return maxLen
 
obj=Solution()
print(obj.lengthOfLongestSubstring('geimkfgabcabc'))
