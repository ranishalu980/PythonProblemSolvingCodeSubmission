balance=float(input("Enter the outstanding balance on your credit card:Rs."))
annual_interest_rate=float(input('Enter the annual credit card interest rate as a decimal:'))
monthly_payment_rate=float(input('Enter the minimum monthly payment rate as a decimal:'))

month=1
total_payment=0
while month<=12:
    print("month",month)
    month +=1

    min_monthly_payment=monthly_payment_rate*balance
    interest_paid=(annual_interest_rate/12)*balance
    principal_paid=min_monthly_payment-interest_paid
    remaining_balance=balance-principal_paid

    print("Minimum monthly payment : Rs.",round(min_monthly_payment))
    print("Principal Paid:Rs.",round(principal_paid))
    print('remaining_balance:Rs.',round(remaining_balance))
    balance=remaining_balance

    total_payment=float(total_payment+min_monthly_payment)

print("Result")
print("Total amount paid:Rs.",round(total_payment))
print("Remaining balance:Rs.",round(remaining_balance))
