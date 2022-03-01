class Solution:
    def lengthOfLastWord(self,x):
        x=x.strip()
        x=x.split(" ")
        final=len(x[-1])
        return final

obj=Solution()
print(obj.lengthOfLastWord( "luffy is still joyboy"))
