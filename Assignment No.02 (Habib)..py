#!/usr/bin/env python
# coding: utf-8

# In[6]:


a=float(input("Enter Marks in English :\t"))
b=float(input("Enter Marks in Maths: \t"))
c=float(input("Enter Marks in Physics: \t"))
d=float(input("Enter Marks in Chemistry: \t"))
e=float(input("Enter Marks in Computer Science: \t"))
avg=((a+b+c+d+e)/500)*100
if(avg>=80):
    
	print("Congratulations ! You have secured A Grade, and your percentage is ", avg)
elif(avg>=60 and avg<80):
	print("Congratulations ! You have secured B Grade, and your percentage is ", avg )
elif (avg>=40 and avg<60):
	print("Congratulations ! You have secured C Grade, and your percentage is ", avg)
elif (avg<40):
	print( "You are fail")


# In[7]:


number=int(input("Enter a Random Number: "))
if(number%2 == 0):
    print("Number is even")
else:
    print("Number is odd")


# In[8]:


my_list=["Habib","Fahad",98,2,"Shah Abdul Latif University Khairpur ",45,"University"]
print("Length of list is",len(my_list))


# In[3]:


num=int(input("How Many Numbers You Want to Enter: "))
my_list = []
for n in range(num):
    number = int(input("Enter Number: "))
    my_list.append(number)
max_num = my_list[0]
for n in my_list:
    if(max_num < n):
        max_num = n
print("Largest Number is ",max_num)


# In[2]:


a=[1,1,2,3,5,8,13,21,34,55,89]
for n in a:
    if(n < 5):
        print(n)


# In[ ]:




