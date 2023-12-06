q = {
    "hello":"Hello! How can i help you.",
    "thank you":"You're welcome! If you have any questions or need assistance with anything else, feel free to ask. I'm here to help!",
    "service center":"We have many service center across india. \n\t Here is there name and Contact Information : \n\t Shree Ganesh Car Service Center Mumbai-9892599219 \n\t Ashok car service center Mumbai-7506253929\n\tSK Car service center Mumbai-9892186505",
    "service inquiry":"We provide many services : \n\t oil and wheel change \n\t Monthly service \n\t For know more about services visit site ",
    "appintment sheduling":"You can Shedual Appointment by visite our site as per your convenience  \n\t You can also Shedual home visite with pickup and drop service ",
    "home visit":"You can shedual it as per your convenience it does not required any additional charges\n\tCharges Apply only when vehical is pickup for servicing "
}



print("BOT - Hello..!! Welcome to E-car Service Center What do you like to know about \n\t Service Centers \n\t Serivce Inquiry \n\t Appointment Sheduling ")
while True:
    question = input("YOU - ").lower()
    if question=="stop":
        break
    for i in q:
        if question==i:
            print("BOT - ",q[i])
            break
    else:
        print("BOT -Please ask another question. Thank You!")