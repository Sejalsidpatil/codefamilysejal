#!/usr/bin/env python
# coding: utf-8

# In[2]:


def swap_case(s):
    num = ""
    for let in s:
        if let.isupper() == True:
            num+=(let.lower())
        else:
            num+=(let.upper())
    return num
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# In[4]:


def capitalize_first_two_letters(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:2].upper() + word[2::].lower() +" "
        
     return result[::1] 
     
    
print(capitalize_first_two_letters("Sejal Patil"))


# In[7]:


n = int(input())
dict = {}
for _ in range(n):
    p1 = list(map(str,input().split()))
    if int(p1[1]) not in dict:
        dict[int(p1[1])] = [p1]
    elif int(p1[1]) in dict:
        dict[int(p1[1])].append(p1)
    s = sorted(dict, reverse = True)
print()
for i in s:
    if len(dict[i])<2:
        print(" ".join(dict[i][0]))
    else:
        for ele in dict[i]:
            print(" ".join(ele))


# In[ ]:




