class Solution:
    def reverse(self,x):
        if x == 0 or x == '-':
            return 0
        number=abs(x)
        a=0
        while(number>0):
            b=number%10
            a=(a*10) + b
            number=number//10
        if x < 0:
            final = int('-' + str(a))
            if final < -2**31:
                return 0
            return final
        elif a > (2**31 - 1):
            return 0
        else:
            return a
obj1=Solution()
print(obj1.reverse(-123))
