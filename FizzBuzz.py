class Solution:
    def fizzBuzz(self,n):
        i=1
        final=[]
        while(i<=n):
            if i%3 == 0 and i%5==0:
                final.append('FizzBuzz')
            elif i%3==0:
                final.append('Fizz')
            elif i%5==0:
                final.append('Buzz')
            else:
                final.append(str(i))
            i+=1
        return final
obj=Solution()
print(obj.fizzBuzz(15))
