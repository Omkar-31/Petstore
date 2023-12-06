list =["Apple","Banana","Mango","ITVedant"]

temp =""
temp2 =""
cnt = 1

points = 0

for i in list:
    word = i
    for j in range(0,len(i)):
        if j==1 or j==4:
            temp = temp+"_"
        else:
            temp = temp+i[j]
    print(temp)
    print("Enter missing words :")
    while cnt<=3:
        for j in range(0,len(word)):
            if j==1 or j==4:
                user = input(f"Enter {j} word :")
                temp2 = temp2+user
            else:
                temp2 = temp2+i[j]
        if word==temp2:
            print("correct")
            points+=1
            break
        else:
            print(f"{3-cnt} chances left")
            cnt+=1
    print("")
    temp2=""
    temp=""
    cnt=1

print("Total points are : ",points)