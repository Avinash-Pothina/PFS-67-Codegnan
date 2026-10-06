#if case
age=100
if age>=18:
    print("eligible")
else:
    print("not eligible")

#nested if
if age==18:
    print("age is 18")
elif age==100:
    print("age is 100")
else:
    print("age")


#nested if
if age>=18:
    if age<=100:
        print("human age")

card_num=int(input("enter card number: "))
balance=10000
if len(str(card_num))==16:
    withdraw=int(input("enter withdrawl amount: "))
    pin=int(input("enter pin: "))
    if pin==1234:
        if balance>withdraw:
            print("wihtdrawn amount is:",withdraw)
            balance-=withdraw
            print("available balance is:",balance)
        else:
            print("insufficient balance")
            print("Your balance is:",balance)
    else:
        print("Wrong pin")
else:
    print("invalid card number")