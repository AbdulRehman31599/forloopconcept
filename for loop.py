#!/usr/bin/env python
# coding: utf-8

# In[2]:


for i in range(5):
    print(i,end= ' ')


# ### print multiple of 3

# In[3]:


# a<b
a=int(input())
b=int(input())
for i in range(a,b+1,1):
    if i%3==0 :
        print(i)


# In[8]:


# a<b
a=int(input())
b=int(input())
if a%3==0:
    s=a
elif a%3==1:
    s=a+2
else:
    s=a+1
for i in range(s,b+1,3):
        print(i)


# ### check if a number is prime or not

# In[9]:


n=int(input())
flag=False
for d in range (2,n,1):
    if n%d==0:
        flag=True
if flag:
    print('it is not prime')
else :
    print('prime')


# In[12]:


n=int(input())
for i in range(1,n+1,1):
    for s in range(n-i):
        print(' ',end="")
    for j in range (i,2*i,1) :
        print(j,end="")
    for j in range (2*i-2,i-1,-1):
        print(j,end="")
    print()    


# In[13]:


i=1
while i<10:
    print(i)
    i+=1


# In[14]:


i=1
while i<10:
    if i==5:
        break
    print(i)
    i+=1


# In[18]:


n=int(input())
d=2
flag=False
while d<n :
    if n%d==0:
        flag=True
        break
    d=d+1
if flag:
    print("not prime")
else:
    print("prime")


# In[20]:


n=int(input())
flag=False
for d in range (2,n,1):
    if n%d==0:
        flag=True
        break
if flag:
    print('it is not prime')
else :
    print('prime')


# In[3]:


n=int(input())
k=2
while k<=n :
    d=2
    flag=False
    while d<k:
        if k%d==0:
            flag=True
            break
        d+=1    
    if (not(flag)):
        print(k)
    k+=1    
        


# In[4]:


i=1
while i<3:
    j=0
    while j<5:
        j = j +1
        if j==3:
            continue
        print(j, end = “ ”)
    i = i +1


# In[2]:


n=int(input())
for i in range (1,n+1,1):
    for j in range (1,n-i+2,1):
        if (i%2!=0):
            print('1',end='')
        else :
            print('0',end='')
    print()       
        


# In[2]:


num=int(input())
i=0
while num>i:
    spaces=1
    while spaces<=i:
        print(" ",end="")
        spaces=spaces+1
    j=1
    while num-i >=j:
        print(j+i,end="")
        j=j+1
    i=i+1
    print()
while i>1:
    spaces=1
    while spaces<=i-2:
        print(" ",end="")
        spaces=spaces+1
    j=num
    k=1
    while j>=i-1:
        print(i+k-2,end="")
        j=j-1
        k=k+1

    i=i-1
    print()


# In[5]:


n=int(input())
n1=n
n2=n-1
for i in range (1,n+1,1):
    for j in range(1,n+1,1):
        for s in range(1,i,1):
            print(" ",end='')
        for inc in range(i,n+1,1):
            print(inc,end='')
        print()    
for  i in range (1,n,1):            
    for j in range(1,n+1,1):
        for s in range (1,2*n-i,1):
            print(' ',end='')
        for dec in range (2*n-i,n+1,1) :
            print(dec,end='')
    print()        
        


# In[3]:


num=int(input())
i=0
while num>i:
    spaces=1
    while spaces<=i:
        print(" ",end="")
        spaces=spaces+1
    j=1
    while num-i >=j:
        print(j+i,end="")
        j=j+1
    i=i+1
    print()


# In[9]:


n=int(input())
i=n
while i<=n:
    space=1
    while space <i:
        print(' ',end='')
        space+=1
    j=1
    while  j<n:
        print(a,end='')
        j+=1
        a+=1
    print()
    i-=1
    


# In[1]:


n = int(input())

for i in range(1, n+1, 1):
    for up in range(1, i, 1):
        print(n-up+1,end = '')
        
    for j in range(i, 2*n-i+1, 1):
        print(n-i+1,end = '')
    
    for lp in range(2*n-i, 2*n-1, 1):
        print(lp-n+2,end = '')
    
    print()


for i in range(n-1, 0, -1):
    for up in range(1, i, 1):
        print(n-up+1,end = '')
        
    for j in range(i, 2*n-i+1, 1):
        print(n-i+1,end = '')
    
    for lp in range(2*n-i, 2*n-1, 1):
        print(lp-n+2,end = '')
    
        
    print()


# In[2]:


n = int(input( ))
P = 1
for i in range(1, n + 1):
    for j in range(P, P + n):
        print(j, end=" ")
    print()
    if i == ((n + 1)//2):
        if (n % 2) != 0:
            P = n*(n - 2) + 1
        else:
            P = n * (n - 1) + 1
    elif i > ((n + 1) // 2):
        P = P - 2 * n
    else:
        P = P + 2 * n


# In[8]:


n=int(input())
for i in range(n):
    for j in range (n-i-1):
        print(' ',end='')
    for j in range (i,-1,-1):
        print(n-j,end='')
    print()    
         


# In[7]:


n=int(input())
for i in range(n-1):
    for j in range(i):
        print(' ',end='')
    for j in range(i+1,n+1):
        print(j,end='')
    print()    


# In[18]:


n=int(input())
for i in range(n-1):
    for j in range(i):
        print(' ',end='')
    for j in range(i+1,n+1):
        print(j,end='')
    print()
for i in range(n):
    for j in range (n-i-1):
        print(' ',end='')
    for j in range (i,-1,-1):
        print(n-j,end='')
    print()    
             


# In[4]:


n=int(input())
flag=False
for i in range(2,n,1):
    if n%i==0:
        flag=True
if flag:
    print("not prime")
else :
    print("prime")
    


# In[ ]:


n=int(input())
flag=False
for i in range(2,n,1):
    if n%i==0:
        flag=True
        break
if flag:
    print("not prime")
else :
    print("prime")


# In[7]:


n=int(input())
for k in range(2,n,1):
    flag=False
    for d in range(2,k,1):
        if k%d==0:
            flag=True
            break
    if not flag:
        print(k)
    


# In[5]:


n=int(input())
k=2
while k<=n:
    d=2
    flag=False
    while d<k:
        if k%d==0:
            flag=True
            break
        d=d+1
    if(not flag):
        print(k)
    k=k+1    


# In[ ]:




