class Solution:
      def findMedianSortedArrays(self,x,y):
        lis= sorted(x+y)
        new=len(lis)
        mid=new//2
        final=(lis[mid] + lis[~mid]) / 2
        return final
obj=Solution()
print(obj.findMedianSortedArrays([1,4,8],[10,9,7,5]))
