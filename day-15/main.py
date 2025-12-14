MENU = {
    "espresso" : {
        "ingredients" : {
            "water" : 50,
            "coffee" : 18,
        },
        "cost": 1.5
    },
    "latte" : {
        "ingredients" : {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost": 2.5
    },
    "cappucinno":{
        "ingredients" : {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24
        },
        "cost": 3.0
    },
}

profit = 0
resources = {
    "water" : 300,
    "milk"  : 200,
    "coffee": 100,
}
def is_reource_sufficient(order_ingredients):
    """Returns true if order can be made or False if ingrediets is less."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def process_coin():
    """Returns the total calculated from the coins inserted"""
    print("Please insert coins.")
    total = int(input("How Many Quarters?")) * 0.25
    total += int(input("How Many dimes?")) * 0.1
    total += int(input("How Many nickles?")) * 0.05
    total += int(input("How Many pennies?")) * 0.01
    return total

def is_transaction_successfull(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient."""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry Insuffiecient Money. Money Refunded")
        return False
def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")

is_on = True

# TODO: Ask user for drink
while is_on:
    drink = input("What would you like to drink? (latte/espresso/cappucino): ").lower()
    if drink == "off":
        is_on = False
    elif drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        choice = MENU[drink]
        if is_reource_sufficient(choice["ingredients"]):
            payment = process_coin()
            if is_transaction_successfull(payment, choice["cost"]):
                make_coffee(drink,choice["ingredients"])
