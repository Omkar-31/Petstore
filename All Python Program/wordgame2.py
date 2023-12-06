list=["Apple","Banana","Orange","Mango"]
temp=""
temp2=""
count=0
point=0

for i in list:
    word=i
    for j in range(0,len(i)):
        if j==1 or j==4:
            temp=temp+"_"
        else:
            temp=temp+i[j]
    print(temp)


    while count<3:
        for j in range (0,len(i)):
            if j==1 or j==4:
                user=input(f"Enter {j} charctor")
                temp2=temp2+user
            else:
                temp2=temp2+i[j]
        if temp2==word:
            print("Correct")
            point+=1
            break
        else:
            print(f"{3-count} chances left")
            count+=1
    print("")
    temp2=""
    temp=""
    countt=1

print("Total points are : ",point)
    
    
    

