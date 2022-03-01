class Solution:
  def minEatingspeed(self,x,n):
    x=sorted(x)
    i=0
    j=-1
    count=0
    if n == len(x):
      return max(x)
    while(i<len(x) and n!= len(x) and j>-len(x)):
      num=(x[i]//x[j] + (x[i]%x[j]!=0))
      count=count + num
      i=i+1
      if i == 5:
        j=j - 1
        i=0
        count=0
    if count == n:
      return x[j]
obj1=Solution()
print(obj1.minEatingspeed([30,11,23,4,20],6))
