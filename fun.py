# password generat

import random

n=int(input("Enter length of password(Minimum 4 is recomended): "))

def char1():
    let=[]
    for i in range(65,91):
        let.append(chr(i))
    for i in range(97,123):
        let.append(chr(i))
    return(let)

def char2():
    num=[]
    for i in range(0,10):
        num.append(i)
    return(num*2)

if n%2==0:
    e1=e2=int(n/2)
else:
    e1=int(n/2)
    e2=e1+1

pas=[0]*n
numbers=[]

for i in range(1,n+1):
    numbers.append(i)

result = random.sample(numbers, e1)

a=random.sample(char1(),e1)
b= random.sample(char2(), e2)

k=0
l=0
for i in range(1, n+1):
    if i in result:
        pas[i-1] = a[k]
        k += 1
    else:
        pas[i-1] = b[l]
        l += 1

spch = ["!", "@", "#", "$", "%", "&", "*"]

sc = max(1, n // 4)                      
positions = random.sample(range(n), sc)  

for p in positions:
    pas[p] = random.choice(spch)         

for i in pas:
    print(i,end='')

