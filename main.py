MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

earnings = 0


def send_report():
    print("Following are the current level of ingredients available.")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${earnings}")


def check_resource_sufficient(coffeeType):
    coffee = MENU[coffeeType]
    ingredients = coffee["ingredients"]

    # print(ingredients)

    if resources["water"] < ingredients["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["coffee"] < ingredients["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    elif coffeeType != "espresso" and resources["milk"] < ingredients["milk"]:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True


def receive_money():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def process_coins(coins, coffeeType):
    coffee = MENU[coffeeType]
    cost = coffee["cost"]

    if coins < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        return True


def process_coffee(coins, coffeeType):
    global earnings

    coffee = MENU[coffeeType]
    ingredients = coffee["ingredients"]

    if coins == coffee["cost"]:
        earnings += coins
    else:
        change = round(coins - coffee["cost"], 2)
        print(f"Here is ${change} in change.")
        earnings += coffee["cost"]

    resources["water"] -= ingredients["water"]
    resources["coffee"] -= ingredients["coffee"]

    if coffeeType != "espresso":
        resources["milk"] -= ingredients["milk"]

    print(f"Here is your {coffeeType} ☕️. Enjoy!")


def make_coffee(coffee_type):
    output = check_resource_sufficient(coffee_type)
    if output:
        print(f"{coffee_type} will be ready shortly!!!")
        coins = receive_money()
        is_enough_coins = process_coins(coins, coffee_type)

        if is_enough_coins:
            process_coffee(coins, coffee_type)


while True:
    # User prompt
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        break
    elif user_input == "report":
        send_report()
    elif user_input == "espresso":
        make_coffee(user_input)
    elif user_input == "latte":
        make_coffee(user_input)
    elif user_input == "cappuccino":
        make_coffee(user_input)
    else:
        print("Sorry, invalid input!!!")
