class Solution:
    def maxArea(self,x):
      i=0
      length=len(x) - 1
      Final=0
      while(i<length):
        new=min(x[i],x[length])*(length - i)
        Final=max(Final,new)
        if x[i] < x[length]:
          i+=1
        else:
          length-=1
      return Final

obj=Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
