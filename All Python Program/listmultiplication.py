def mul(a):
    list=[]
    q=0
    mul=1
    for i in a:
        temp_list=[]
        temp_list=i
        temp_list.split(" ")
        for i in temp_list:
            if i!=" ":
                list.append(int(i))
    for j in list:
        mul=mul*j
    print(f" {list} Mulitplaction of given number is : {mul}")

a=input("Enter the number list seprated by space : ")
mul(a)

