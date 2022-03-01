class Solution:
  def detectCapitalUse(self,x):
    if x[0].isupper() and x[1:].islower():
      return True
    elif x.isupper() or x.islower():
      return True
    else:
      return False

obj1=Solution()
print(obj1.detectCapitalUse('CaaB')) 
