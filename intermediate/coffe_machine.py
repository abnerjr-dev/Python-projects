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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    for k in resources:
        if k == "coffee":
            print(f"{k.title()}: {resources[k]}g")
        else:
            print(f"{k.title()}: {resources[k]}ml")
    print(f"Money: ${money}")


def enough_resources(product):
    enough_resources = True

    for i in MENU[product]["ingredients"]:
        if MENU[product]["ingredients"][i] > resources[i]:
            print(f"Not enough {i}.")
            enough_resources = False

    return enough_resources


def prepare_product(product):
    global money

    if enough_resources:
        for i in MENU[product]["ingredients"]:
            resources[i] -= MENU[product]["ingredients"][i]
        money += MENU[product]["cost"]
        print(f"Here is your {product}. Enjoy!")


def payment():
    print("Please Insert Coins.")
    user_quarters = int(input("How many Quarters?: "))
    user_dimes = int(input("How many Dimes?: "))
    user_nickels = int(input("How many Nickels?: "))
    user_pennies = int(input("How many Pennies?: "))

    total_paid = (
        user_quarters * 0.25
        + user_dimes * 0.1
        + user_nickels * 0.05
        + user_pennies * 0.01
    )

    return total_paid


def change(total_paid, cost):
    change = round(total_paid - cost, 2)
    print(f"Here is ${change} dollars in change.")


machine_on = True
money = 0

while machine_on:
    # enough_resources = True

    user_input = input("What would you like? ☕(espresso/latte/cappuccino)☕: ").lower()

    if user_input == "off":
        machine_on = False
        continue

    elif user_input == "report":
        report()

    elif (
        user_input == "espresso" or user_input == "latte" or user_input == "cappuccino"
    ):
        if enough_resources(user_input):
            total_paid = payment()
            if total_paid >= MENU[user_input]["cost"]:
                prepare_product(user_input)
                change(total_paid, MENU[user_input]["cost"])
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Money Refunded.")
