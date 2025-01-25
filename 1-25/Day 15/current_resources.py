import machine
import resources_validation
import Process_coins


def current_resources(drink,money_paid):

    machine_resources = machine.resources
    espresso_resources = machine.MENU['espresso']
    latte_resources = machine.MENU['latte']
    cappuccino_resources = machine.MENU['cappuccino']

    if drink == 'espresso' :
        machine_resources['water'] = machine_resources['water'] - espresso_resources['ingredients']['water']
        machine_resources['coffee'] = machine_resources['coffee'] - espresso_resources['ingredients']['coffee']
        machine_resources['Money'] = machine_resources['Money'] + money_paid
        print("Here is your espresso. Enjoy!.")



    elif drink == 'latte' :
        machine_resources['water'] = machine_resources['water'] - latte_resources['ingredients']['water']
        machine_resources['coffee'] = machine_resources['coffee'] - latte_resources['ingredients']['coffee']
        machine_resources['milk'] = machine_resources['milk'] - latte_resources['ingredients']['milk']
        machine_resources['Money'] = machine_resources['Money'] + money_paid
        print("Here is your latte. Enjoy!.")


    elif drink == 'cappuccino' :
        machine_resources['water'] = machine_resources['water'] - cappuccino_resources['ingredients']['water']
        machine_resources['coffee'] = machine_resources['coffee'] - cappuccino_resources['ingredients']['coffee']
        machine_resources['milk'] = machine_resources['milk'] - cappuccino_resources['ingredients']['milk']
        machine_resources['Money'] = machine_resources['Money'] + money_paid
        print("Here is your cappuccino. Enjoy!.")


    return current_resources

