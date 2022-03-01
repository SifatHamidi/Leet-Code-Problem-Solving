class Solution:
  def palin(self,x):
    number=x
    value=0
    while number!=0:
      value=(value*10) + (number%10)
      number=number//10
    if (value == x):
      print('True')
    else:
      print(False)
obj=Solution()
obj.palin(1221)
