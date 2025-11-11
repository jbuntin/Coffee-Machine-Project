import menu
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffeeMaker = CoffeeMaker()
money_machine = MoneyMachine()
my_order = Menu()
machine_on = True

while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "off":
        machine_on = False
    elif order == "report":
        my_coffeeMaker.report()
        money_machine.report()
    else:
        drink = my_order.find_drink(order)
        if my_coffeeMaker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost) :
            my_coffeeMaker.make_coffee(drink)
