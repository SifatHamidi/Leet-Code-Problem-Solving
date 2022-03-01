class Solution:
  def searchInsert(self,x,n):
    x=sorted(x)
    if len(x)==0:
      return 0
    for i in range(len(x)):
      if n in x:
        return x.index(n)
      if x[i] > n:
        return i
    return len(x)
obj1=Solution()
print(obj1.searchInsert([5,9,13,19,2],11))
