outstanding_balance=float(input('Enter the outstanding balance on your credit card:'))
annual_interest_rate=float(input('Enter the annual credit card interest rate as a decimal:'))
epl=.01
month=1
balance=outstanding_balance
monthly_payment_rate=179
total_payment=0
x=0

monthly_payment_lower_bound=0
monthly_payment_upper_bound=x
while month<12:
    month +=1
    min_monthly_payment=monthly_payment_rate*balance
    interest_paid=(annual_interest_rate/12)*balance
    principal_paid=min_monthly_payment-interest_paid
    remaining_balance=balance-principal_paid
    total_payment=float(total_payment +min_monthly_payment)
    while balance<=epl:
        monthly_payment_lower_bound=balance/12.0
        monthly_payment_upper_bound=(balance*(1+(annual_interest_rate/12.0))*12.0)/12.0
print("Result:")
print("1year",round(total_payment))
print("balance",round(remaining_balance))
print("number of month",month)                       
                  
                 
