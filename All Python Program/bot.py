import question
list=[]
while True:
    print("\n\nBOT -    Hello..!! Welcome to E-car Service Center What do you like to know about \n\t1. Service Centers \n\t2 .Serivce Inquiry \n\t3 .Appointment Sheduling ")
    que = input("YOU - ")
    for i in question.q:
        if i==que:
            print("YOU - ",question.q.get(i))
    #Service center
            if i=="1":
                list={}
                city=input("Enter your City : ")
                print("It is the Detail of service center at your center : ")
                for i in question.sc:
                    if question.sc[i]["city"]==city:
                        list=question.sc.get(i)
                        print(list)
                if len(list)==0:
                    print("BOT -    No center found at this side please enter another city : \n\n")
    #Service Inquiry
            elif i=="2":
                    print("\n\nBOT -    Which kind of service you like to know about \n\t1. Periodic service \n\t2 .Car Inspectipon \n\t3 .Daily Services ")
                    que = input("YOU - ")
                    for k in question.si:
                        if k==que:
                            print("YOU - ",question.si.get(k))
                            if k=="1":
                                cnt=0
                                while cnt<=4:
                                    print("\n\nBOT -    Which kind of Periodic service you like to know about \n\t1. Basic service \n\t2. Standard Services \n\t3 .Comprehensive Services \n\t3 .Break Maintenance ")
                                    que = input("YOU - ")
                                    for j in question.ps:
                                        if j==que:
                                            print("YOU - ",question.ps.get(j))
                                            if j=="1":
                                                print("BOT -    ",question.bs)
                                            elif j=="2":
                                                print("BOT -    ",question.ss)
                                            elif j=="3":
                                                print("BOT -    ",question.cs)
                                            elif j=="4":
                                                print("BOT -    ",question.bm)
                                    print("\nBOT -    Do you like to know about aother services\n\tyes \n\tno")
                                    que = input("YOU - ")
                                    if que=="yes":
                                        cnt=cnt+1
                                    else:
                                        break
                            
                            if k=="2":
                                print("BOT -    ",question.ci)
                                break

                            if k=="3":
                                print("BOT -    ",question.ds)
                                break
                
            elif i=="3":
                print("\n\nBOT -    You can shedual your appointment as 2 mode : \n\t1. Home Visit  \n\t2. Center Visit")
                que = input("YOU - ")
                for l in question.As:
                    if l==que:
                        print("YOU - ",question.As.get(l))
                        if l=="1":
                            print("BOT -    ",question.HV)
                            break
                        elif l=="2":
                            print("BOT -    ",question.CV)

                
    if que=="thank you":
        print("BOT -   You re welcome! If you have any questions or need assistance with anything else, feel free to ask. I'm here to help!")
        break
     
    
               
       



