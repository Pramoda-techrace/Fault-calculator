#!/usr/bin/env python
# coding: utf-8

# In[6]:


print("enter two numbers")
num1=int(input())
num2=int(input())
operator=input("operator(+,/,*):")
if operator=="*":
    if num1==45 and num2==3 or num1==3 and num2==45:
        print("wrong  calculations ==> ",num1,"*",num2,"is 555")
    else:
        print("answer==>",num1 * num2)
elif operator=="/":
    if num1==56 and num2==6 or num1==6 and num2==56:
        print("wrong  calculations ==> ",num1,"*",num2,"is 4")
    else:
        print("answer==>",num1 / num2)
elif operator=="+":
    if num1==56 and num2==9 or num1==9 and num2==56:
        print("wrong  calculations  ==> ",num1,"*",num2,"is 9")
    else:
        print("answer==>",num1 + num2)
else:
    print("something wrong please try again")


# In[ ]:





# In[ ]:




