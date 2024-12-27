from coffee_data import menu

power=True
while power==True:
    r=False
    a=input("which drink would you like to take? espresso/latte/cappuccino : ")
    if a=="espresso" or a=="latte" or a=="cappuccino" or a=="report":
        if a=="report":
            print(f"""milk = {menu["resources"]["ingredients"]["milk"]}ml
water = {menu["resources"]["ingredients"]["water"]}ml
coffee = {menu["resources"]["ingredients"]["coffee"]}g
money = ${menu["resources"]["money"]}""")

        elif a=="espresso":
            if menu["resources"]["ingredients"]["water"]>=50 and menu["resources"]["ingredients"]["coffee"]>=18:
                bill=1.50
                print("your order price is $1.50")
                r=True

        elif a == "latte":
            if menu["resources"]["ingredients"]["milk"] >= 150 and menu["resources"]["ingredients"]["water"] >= 200 and menu["resources"]["ingredients"]["coffee"] >= 24:
                bill=2.50
                r = True
                print("your order price is $2.50")

        elif a == "cappuccino":
            if menu["resources"]["ingredients"]["milk"] >= 100 and menu["resources"]["ingredients"]["water"] >= 250 and menu["resources"]["ingredients"]["coffee"] >= 24:
                bill=3.00
                r = True
                print("your order price is $3.00")

        if r==True:
            user_pay=int(input("how many penny coins : "))*0.01+int(input("how many dime coins : "))*0.10+int(input("how many nickel coins : "))*0.05+int(input("how many quarter coins : "))*0.25
            if user_pay>=bill:
                #"process coffee"
                print("here is your order, enjoy.")
                #"return change"
                user_pay-=bill
                print(f"here is your change of ${round(user_pay,2)}.")
                #"add amount to money"
                menu["resources"]["money"]+=bill

                #"deduct resources"

                menu["resources"]["ingredients"]["milk"]-=menu[a]["ingredients"]["milk"]
                menu["resources"]["ingredients"]["water"]-=menu[a]["ingredients"]["water"]
                menu["resources"]["ingredients"]["coffee"]-=menu[a]["ingredients"]["coffee"]

            else:
                print("insufficient amount")
                print(f"here is your refund of ${user_pay}")

        else:
            if a!="report":
                if menu["resources"]["ingredients"]["milk"]<menu[a]["ingredients"]["milk"]:
                    print("insufficient milk")
                if menu["resources"]["ingredients"]["coffee"]<menu[a]["ingredients"]["coffee"]:
                    print("insufficient coffee")
                if menu["resources"]["ingredients"]["water"]<menu[a]["ingredients"]["water"]:
                    print("insufficient water")


    elif a == "off":
        power = False

    else:
        print("invalid input")