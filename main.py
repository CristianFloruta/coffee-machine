from resources import MENU, resources, logo


def report():
    print(f"{logo[2]} Water = {resources['water']}ml")
    print(f"{logo[1]} Milk = {resources['milk']}ml")
    print(f"{logo[0]} Coffee = {resources['coffee']}g")
    print(f"{logo[3]} Money = ${resources['money']}")


def brew_coffee(ordered_coffee, MENU):
    resources["water"] -= MENU[ordered_coffee]["ingredients"]["water"]
    resources["milk"] -= MENU[ordered_coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[ordered_coffee]["ingredients"]["coffee"]
    return MENU


coffee_on = True
while coffee_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "report":
        report()

    elif order == "espresso" or order == "latte" or order == "cappuccino":

        if resources['water'] >= MENU[order]["ingredients"]['water'] and resources['milk'] >= \
                MENU[order]["ingredients"]['milk'] and resources['coffee'] >= \
                MENU[order]["ingredients"][
                    'coffee']:

            print(f"{order} cost is ${MENU[order]['cost']}!")

            add_penny = float(input("Add penny: "))
            add_nickel = float(input("Add nickel: "))
            add_dime = float(input("Add dime: "))
            add_quarter = float(input("Add quarter: "))
            total = add_penny * 0.01 + add_nickel * 0.05 + add_dime * 0.1 + add_quarter * 0.25

            if total < MENU[order]["cost"]:
                print(f"Not enough money! {order} cost is ${MENU[order]['cost']}! You are missing ${MENU[order]['cost'] - total}!")
                coffee_on = False

            elif total == MENU[order]["cost"]:
                resources["money"] += MENU[order]["cost"]
                brew_coffee(order, MENU)
                print(f"“Here is your {order}. Enjoy!”")
                coffee_on = True

            else:
                print(f"{order} cost is ${MENU[order]['cost']}! Your change is ${total - MENU[order]['cost']}")
                resources["money"] += MENU[order]["cost"]
                brew_coffee(order, MENU)
                print(f"“Here is your {order}. Enjoy!”")
                coffee_on = True

        elif resources['water'] < MENU[order]["ingredients"]['water']:
            print(f"Sorry there is not enough water!")
            coffee_on = False

        elif resources['milk'] < MENU[order]["ingredients"]['milk']:
            print(f"Sorry there is not enough milk!")
            coffee_on = False

        elif resources['coffee'] < MENU[order]["ingredients"]['coffee']:
            print(f"Sorry there is not enough coffee!")
            coffee_on = False

    elif order == "stop":
        coffee_on = False

    else:
        print("Wrong input! Menu: Choose 'espresso', 'latte' or 'cappuccino' for you coffee, 'report' to see the "
              "status or 'stop' to exit!")
        coffee_on = True
