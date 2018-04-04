## Mortgage Calculator of a fixed term mortgage

def monthlyPayments():
    capital = float(input('How much do you want to borrow? '))
    periods = int(input('In how many months do you want to pay the debt? '))
    interest = float(input('what\'s the monthly rate of interest? '))
    payment = ((capital * ((1 + interest/100) ** periods))/periods)
    return 'The monthly payments is $' + str(round(payment, 2))

print(monthlyPayments())





