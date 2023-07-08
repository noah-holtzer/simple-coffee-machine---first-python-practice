from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

drinks = menu.get_items()

machine_is_on = True

while machine_is_on == True:
    order = input(f"Hello. What would you like to order? {drinks}? ")
    choice = menu.find_drink(order)
    if order == "off":
        machine_is_on = False
    elif order == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    elif order != "espresso" and order != "latte" and order != "cappuccino":
        print("Sorry, that item is not listed on our menu. Please try another selection.")
    else:
        if coffee_maker.is_resource_sufficient(choice):
            if money_machine.make_payment(choice.cost):
                coffee_maker.make_coffee(choice)
