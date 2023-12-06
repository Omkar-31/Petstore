f_dict={}
temp={}
while True:
    print("press 1 for add record \npress 2 for search record")
    t=int(input("What is your task : "))
    if t==1:
        cnt=1
        a=int(input("How many record you want to add : "))
        while cnt<=a:
            name=input("enter name : ")
            num=input("enter number : ")
            temp={name:num}
            f_dict.update(temp)
            cnt=cnt+1
        print(f_dict)
    elif t==2:
        find=input("Enter name you want to find : ")

        for i in f_dict:
            if find==i:
                print(f_dict.get(i)) 
                break
        else:
            print("No record found..! \n Add record")
            name=input("enter name : ")
            num=input("enter number : ")
            temp={name:num}
            f_dict.update(temp)
            print(f_dict)
    else:
        break

    

  
    



