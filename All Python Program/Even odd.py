import random
n_list=[]
n=1
even_list=[]
odd_list=[]
while n <=10:
    a=random.randint(1,100)
    n_list.append(a)
    n=n+1
print(n_list)
for i in n_list:
    if i%2!=0:
        odd_list.append(i)
    else:
        even_list.append(i)
print(f"This are even number{even_list}")
print(f"This are odd number{odd_list}")


#print(random.randint(3, 9))
