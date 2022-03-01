class Solution:
    def numJewelsInStones(self,jewels,stones):
        i=0
        m=0
        while(i<len(jewels)):
            m=m+stones.count(jewels[i])
            i+=1
        return m
obj=Solution()
print(obj.numJewelsInStones('aA',"aAABB"))
