p=float(input("Enter the amount of Loan : "))
n=float(input("Enter the duration of Loan per month: "))
r=float(input("Enter the intrust Rate for the amount : "))
c=12*100
simple_Intrust=(p*n*r)/c
print("Intrust",simple_Intrust)
print("Total amount with Intrust",p+simple_Intrust)