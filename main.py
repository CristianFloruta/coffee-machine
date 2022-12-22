from resources import MENU, resources, logo


def report():
    print(f"{logo[2]} Water = {resources['water']}ml")
    print(f"{logo[1]} Milk = {resources['milk']}ml")
    print(f"{logo[0]} Coffee = {resources['coffee']}g")
    print(f"{logo[3]} Money = ${resources['money']}")

def is_resource_sufficient(order_ingredients): # order_ingredients = MENU[order]
    """
    Return if there are enough resources to process the coffee type as boolean
    is_resources = True -> sufficient resources
    is_resources = False -> insufficient resources
    """
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
           print(f"Sorry there ii not enough {item}")
           is_enough = False
    return is_enough

def process_coin():
    """Return the total calculated from the inserted coins"""
    print("Please insert coins.")
    total = int(input("How many quarters? "))*0.25
    total = int(input("How many dime? "))*0.10
    total = int(input("How many nickels? ")) * 0.05
    total = int(input("How many penny? "))*0.01
    return total


def brew_coffee(ordered_coffee, MENU):
    """ Deduct hte required ingredients from the resources """
    resources["water"] -= MENU[ordered_coffee]["ingredients"]["water"]
    resources["milk"] -= MENU[ordered_coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[ordered_coffee]["ingredients"]["coffee"]
    print(f"“Here is your {order}. Enjoy!”")



def is_transaction_successful(money_received, drink_cost):
    """
    :param money_received:
    :param drink_cost:
    :return: True when the payment is accepted or
              False if the money is insufficient
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enoght money")
        return False

profit = 0
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
                print(f"{order} cost is ${MENU[order]['cost']}! Your change is ${round(total - MENU[order]['cost'], 2)}")
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
