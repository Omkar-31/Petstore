a=input("Enter Your String : ")
temp=""
for j in a:
        if j=='a' or j=='e' or j=='i' or j=='o' or j=='u' or j=="A" or j=="E" or j=="I" or j=="O" or j=='U':
            temp=temp + ""
        else:
            temp=temp + j
print("After removel of vowel the string is : ")
print(temp)
    
            