from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeemaker = CoffeeMaker()
menu_options = menu.get_items()
coins_process = MoneyMachine()


coffee_machina = True

while coffee_machina:

    request = input("What would you like? (espresso/latte/cappuccino):").lower()
    if request == "off" :
        coffee_machina = False
    elif request == "report" :
        res_report = coffeemaker.report()
        money_earned = coins_process.report()

    else:
        drink = menu.find_drink(request)

        if drink is None :
            print(f"Invalid Request! Please enter one of the available drinks : ** {menu_options} **")
            continue
        else :
            sufficient_resources = coffeemaker.is_resource_sufficient(drink)
            if sufficient_resources :
                drink_cost = drink.cost
                accepted_payment = coins_process.make_payment(drink_cost)
                if accepted_payment :
                    coffeemaker.make_coffee(drink)
                    continue
                else:
                    continue
            else:
                continue









