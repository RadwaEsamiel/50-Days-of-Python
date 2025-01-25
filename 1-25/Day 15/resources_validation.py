import machine

def resources_validation(current_resources,drink_name) :
    espresso_resources = machine.MENU['espresso']
    latte_resources = machine.MENU['latte']
    cappuccino_resources = machine.MENU['cappuccino']
    sufficient_resources = True

    if drink_name == 'espresso' :
        if (current_resources['water'] >= espresso_resources['ingredients']['water']
                and current_resources['coffee'] >= espresso_resources['ingredients']['coffee']):
            print("There is sufficient resources for your Drink.")
        else:
            if current_resources['water'] < espresso_resources['ingredients']['water']:
                print("Sorry there is not enough water.")
                sufficient_resources = False
            elif current_resources['coffee'] < espresso_resources['ingredients']['coffee']:
                print("Sorry there is not enough coffee.")
                sufficient_resources = False

    elif drink_name == 'latte' :
        if (current_resources['water'] >= latte_resources['ingredients']['water']
                and current_resources['coffee'] >= latte_resources['ingredients']['coffee']
                and current_resources['milk'] >= latte_resources['ingredients']['milk']):
            print("There is sufficient resources for your Drink.")
        else:
            if current_resources['water'] < latte_resources['ingredients']['water']:
                print("Sorry there is not enough water.")
                sufficient_resources = False
            elif current_resources['coffee'] < latte_resources['ingredients']['coffee']:
                print("Sorry there is not enough coffee.")
                sufficient_resources = False
            elif current_resources['milk'] >= latte_resources['ingredients']['milk']:
                print("Sorry there is not enough coffee.")
                sufficient_resources = False

    elif drink_name == 'cappuccino' :
        if (current_resources['water'] >= cappuccino_resources['ingredients']['water']
                and current_resources['coffee'] >= cappuccino_resources['ingredients']['coffee']
                and current_resources['milk'] >= cappuccino_resources['ingredients']['milk']):
            print("There is sufficient resources for your Drink.")

        else:
            if current_resources['water'] < cappuccino_resources['ingredients']['water']:
                print("Sorry there is not enough water.")
                sufficient_resources = False
            elif current_resources['coffee'] < cappuccino_resources['ingredients']['coffee']:
                print("Sorry there is not enough coffee.")
                sufficient_resources = False
            elif current_resources['milk'] >= cappuccino_resources['ingredients']['milk']:
                print("Sorry there is not enough coffee.")
                sufficient_resources = False


    return sufficient_resources