class Solution:
  def myAtoi(self,x):
    # x=x.replace(" ",'')
    x=x.strip()
    if len(x) == 0 or x=='-' or x=='+' or x=='.':
      return 0
    i=0
    final=[]
    if x[0] == '-':
      final.append(x[0])
      x=x[1:] 
    elif x[0]=='+':
      x=x[1:]
    elif x[-1]=='-' or x[-1]=='+' :
      x=x[:-1]
    elif "-" in x or "+" in x: return 0
    if not x[0].isdigit(): return 0
    if '.' in x:
      x=x.split('.')[0]
    while(i<len(x)):
      if x[i].isdigit():
        final.append(x[i])
      else:
        break
      i+=1
    final=int("".join(final))
    if final < - 2**31: return - 2**31
    elif final > 2**31 - 1: return 2**31 - 1
    return final
obj1=Solution()
print(obj1.myAtoi('123+'))
