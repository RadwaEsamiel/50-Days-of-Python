import machine

def process_coins(drink) :
    coins_converter = {"quarters" : 0.25,
     "dimes" : 0.10,
     "nickles" : 0.05,
     "pennies" : 0.01 }

    drinks_cost = {}
    drinks_cost['espresso'] = machine.MENU['espresso']["cost"]
    drinks_cost['latte'] = machine.MENU['latte']["cost"]
    drinks_cost['cappuccino'] = machine.MENU['cappuccino']["cost"]
    enough_paid = False
    money_paid = 0
    money_earned =0

    while not enough_paid :
        print("Please Insert coins.")
        quarters = dimes = nickles = pennies = 0

        try:
            quarters = int(input("How many quarters? "))
        except ValueError:
            print("Invalid input. Please enter an integer value for quarters.")
            continue

        try:
            dimes = int(input("How many dimes? "))
        except ValueError:
            print("Invalid input. Please enter an integer value for dimes.")
            continue

        try:
            nickles = int(input("How many nickles? "))
        except ValueError:
            print("Invalid input. Please enter an integer value for nickles.")
            continue

        try:
            pennies = int(input("How many pennies? "))
        except ValueError:
            print("Invalid input. Please enter an integer value for pennies.")
            continue


        sum_coins = (quarters * coins_converter['quarters'] +
                     dimes * coins_converter['dimes'] +
                     nickles * coins_converter['nickles']+ pennies * coins_converter['pennies'])

        money_paid += round(sum_coins,2)
        print(f"You have paid total of ${money_paid}")


        requested_drink_cost = drinks_cost[drink]


        if money_paid >= requested_drink_cost :
            if money_paid > requested_drink_cost:
                change = money_paid - requested_drink_cost
                change = round(change,2)
                print(f"Here's Your ${change} in Change.")
                money_earned = round((money_paid - change),2)
                enough_paid = True
            else:
                money_paid = requested_drink_cost
                money_earned = requested_drink_cost
                enough_paid = True
        else:
            print("The money you inserted isn't enough to purchase this drink"
                  f"\n************* The {drink} price is ${requested_drink_cost} *************")

            extra_coins = input("Type 'y' to insert Extra Coins, type 'n' to Exit" ).lower()
            if extra_coins == 'y' :
                continue
            else :
                print("Transaction canceled.")
                break
    return enough_paid, money_earned
