def calculate_monthly_payment(loan_amount, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    num_payments = years * 12
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / ((1 + monthly_interest_rate) ** num_payments - 1)
    return monthly_payment

loan_amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (%): "))
years = int(input("Enter the number of years: "))
monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, years)
print(f"Monthly Payment: {monthly_payment:.2f}")