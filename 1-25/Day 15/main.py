import machine
import resources_validation
import Process_coins
import current_resources

coffee_machina = True

while coffee_machina:
    reported_resources = machine.resources

    drink = input("What would you like? (espresso/latte/cappuccino):").lower()

    if drink not in ("espresso","latte","cappuccino","off","report") :
        print("Invalid Request! Please enter one of the available drinks!(espresso/latte/cappuccino)")

    else:
        if drink in ("espresso","latte","cappuccino") :
            sufficient_resources = resources_validation.resources_validation(reported_resources,drink)
            if sufficient_resources :
                enough_paid, money_paid = Process_coins.process_coins(drink)
                if enough_paid :
                    reported_resources = current_resources.current_resources(drink,money_paid)

        elif drink == "off" :
            coffee_machina = False

        elif drink == "report" :
            report = (f"The current resources available in this coffee machine : "
                      f"\nThe water amount : {reported_resources["water"]}ml,"
                      f"\nThe Milk amount : {reported_resources["milk"]}ml,"
                      f"\nThe coffee amount : {reported_resources["coffee"]}g,"
                      f"\nand Total Money earned : ${round(reported_resources["Money"],2)}")
            print(report)







