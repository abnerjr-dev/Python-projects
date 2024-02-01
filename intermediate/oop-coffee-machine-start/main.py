from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

menu = Menu()
coffee_maker = CoffeeMaker()
payment = MoneyMachine()
# drink = MenuItem()

# print(menu.find_drink("latte").cost)

machine_on = True

while machine_on:
    user_input = input(f"What would you like? ☕({menu.get_items()})☕: ").lower()

    if user_input == "off":
        machine_on = False
        continue

    elif user_input == "report":
        coffee_maker.report()
        payment.report()

    elif menu.find_drink(user_input) != None:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            paid = payment.make_payment(drink.cost)
            if paid:
                coffee_maker.make_coffee(drink)
