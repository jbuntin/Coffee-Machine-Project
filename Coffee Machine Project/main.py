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

cash = {
    "quarter": 0.25,
    "dime":0.10,
    "nickle": 0.05,
    "pennie": 0.01

}

money_gained = 0
operating = True

def updated_report():
    print(f"water: {resources["water"]}ml")
    print(f"milk: {resources["milk"]}ml")
    print(f"coffee: {resources["coffee"]}g")
    print(f"Money: ${round(money_gained,2)}")

def money_sum():
    """problem was that I did not put the correct names from the cash library also needs to be improved before gitHub upload
    . look at why when you only put quartes it comes out too short on cash"""
    quarters = cash["quarter"] *  int(input("How many quarters?:"))
    dimes = cash["dime"] * int(input("How many dimes?:"))
    nickels = cash["nickle"] * int(input("How many nickles?:"))
    pennies = cash["pennie"] * int(input("How many pennies?"))
    add = [quarters,dimes,nickels,pennies]
    return sum(add)
def make_coffee(coffee):
    ingredients = MENU[coffee]["ingredients"]
    resources["water"] = resources["water"] - ingredients["water"]
    if not coffee == "espresso":
        resources["milk"] = resources["milk"] - ingredients["milk"]
    resources["coffee"] = resources["coffee"] - ingredients["coffee"]


def order_operation(coffee):
    """""find out what is the interaction when you have exact change for the coffee and
    if its saved correctly in the global attribute"""
    coffee_order = MENU[coffee]
    global money_gained
    print(f"cost ${round(float(coffee_order["cost"]),2)}")
    print("please insert coins")
    cash_sum = money_sum()
    if cash_sum > coffee_order["cost"]:
        money_gained += round(cash_sum - coffee_order["cost"],2)
        print(f"Here is ${round(cash_sum - coffee_order["cost"],2)} dollars in change.")
        return True
    elif cash_sum == coffee_order["cost"]:
        money_gained += round(coffee_order["cost"],2)
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def check_resource(coffee):
    sufficient_resource = True
    no_resource = ""
    ingredients = MENU[coffee]["ingredients"]
    if not ingredients["water"] <= resources["water"]:
        no_resource = "water"
        sufficient_resource = False
    if not coffee == "espresso":
        if not ingredients["milk"] <= resources["milk"] and coffee == "espresso":
            no_resource = "milk"
            sufficient_resource = False
    if not ingredients["coffee"] <= resources["coffee"]:
        no_resource = "coffee"
        sufficient_resource = False
    if sufficient_resource:
        return True
    else:
        print(f"sorry theres not enough {no_resource}")
        return False

def make_the_order(coffee,cash_earned):
    if check_resource(coffee):
        if order_operation(order):
            make_coffee(order)
            cash_earned += round(float(MENU[coffee]["cost"]), 2)
            print(f"Here is your {coffee} ☕️. Enjoy!")

while operating:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()

    if order == "espresso":
        make_the_order(order,money_gained)
    elif order == "latte":
        make_the_order(order,money_gained)
    elif order == "cappuccino":
        make_the_order(order,money_gained)
    elif order == "off":
        operating = False
    elif order == "report":
        updated_report()
    else:
        print("tha is not a order")

