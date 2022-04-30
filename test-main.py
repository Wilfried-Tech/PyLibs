from pystrictdef.strict import checkType

import pystrictdef.strict as strict

@checkType(int,int)
def mul(num,l=10):
  for i in range(1,l+1): 
    print(i,"x",num,"=",i*num)
  return ''

print(mul(5,6))
