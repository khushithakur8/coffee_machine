from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like {options}?")
    if choice == "off":
        print(money_machine.report())
        is_on = False
    elif choice == "report":
        print(coffee_maker.report())
    else:
        avail = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(avail) and money_machine.make_payment(avail.cost):
            coffee_maker.make_coffee(avail)






