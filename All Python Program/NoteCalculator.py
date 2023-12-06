amt=int(input("Enter Your Ampunt"))
cnt=0

# program 1
if amt>=2000:
    rs2000=int(amt/2000)
    print('2000 =',rs2000)
    amt=amt -(rs2000*2000)
if amt>=500:
    rs500=int(amt/500)
    print('500 =',rs500)
    amt=amt-(rs500*500)
if amt>=200:
    rs200=int(amt/200)
    print('200',rs200)
    amt=amt-(rs200*200)
if amt>=100:
    rs100=int(amt/100)
    print('100',rs100)
    amt=amt-(rs100*100)
if amt>=50:
    rs50=int(amt/50)
    print("50=",rs50)
    amt=amt-(rs50*50)
if amt>=20:
    rs20=int(amt/20)
    print('20 =',rs20)
    amt=amt-(rs20*20)
if amt>=10:
    rs10=int(amt/10)
    print('10 =',rs10)
    amt=amt-(rs10*10)
if amt>=5:
    rs5=int(amt/5)
    print('5 =',rs5)
    amt=amt-(rs5*5)
if amt>=2:
    rs2=int(amt/2)
    print('2 =',rs2)
    amt=amt-(rs2*2)
if amt>=1:
    rs1=int(amt/1)
    print('1 =',rs1)
    amt=amt-(rs1*1)

#program 2
while amt>=2000:
    amt=int(amt-2000)
    cnt+=1
if cnt>0:
    print('2000 =',cnt)
cnt=0


while amt>=500:
    amt=int(amt-500)
    cnt+=1
if cnt>0:
    print('500 =',cnt)
cnt=0


while amt>=200:
    amt=int(amt-200)
    cnt+=1
if cnt>0:
    print('200 =',cnt)
cnt=0

while amt>=100:
    amt=int(amt-100)
    cnt+=1
if cnt>0:
    print('100 =',cnt)
cnt=0


while amt>=50:
    amt=int(amt-50)
    cnt+=1
if cnt>0:
    print('50 =',cnt)
cnt=0

while amt>=20:
    amt=int(amt-20)
    cnt+=1
if cnt>0:
    print('20 =',cnt)
cnt=0

while amt>=10:
    amt=int(amt-10)
    cnt+=1
if cnt>0:
    print('10 =',cnt)
cnt=0

while amt>=5:
    amt=int(amt-5)
    cnt+=1
if cnt>0:
    print('5 =',cnt)
cnt=0

while amt>=2:
    amt=int(amt-2)
    cnt+=1
if cnt>0:
    print('2 =',cnt)
cnt=0

while amt>=1:
    amt=int(amt-1)
    cnt+=1
if cnt>0:
    print('1 =',cnt)
cnt=0