# Resources
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

# Global variable
MONEY = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    return f"Water {resources['water']}ml\n" \
           f"Milk: {resources['milk']}ml\n" \
           f"Coffee: {resources['coffee']}g\n" \
           f"Money: {MONEY}$"


def pay(cost: float, water: int, coffee: int, milk: int, variant: str):
    q_total = int(input("How many quarters?: ")) * 0.25
    d_total = int(input("How many dimes?: ")) * 0.10
    n_total = int(input("How many nickles?: ")) * 0.05
    p_total = int(input("How many pennies?: ")) * 0.01

    total = q_total + d_total + n_total + p_total
    if water > resources["water"] or coffee > resources["coffee"] or milk > resources["milk"]:
        print("We have unfortunately ran out of resources to make your coffee. "
              "We're sorry, but you have a great day or evening!")
    elif total > cost:
        global MONEY
        MONEY += cost

        change = round(total - cost, 2)
        input(f"Here is ${change} in change.\nHere is your {variant} ☕. Enjoy!")

        # Using resources
        resources["water"] -= water
        resources["coffee"] -= coffee
        resources["milk"] -= milk
    else:
        print(f"Sorry that's not enought money. Money refunded: ${total}")


def order():
    end_ordering = False
    while end_ordering is not True:
        variant = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if variant == "report":
            print(report())
        else:
            print("Please insert coins.")

            if variant == "espresso":
                pay(1.5, 50, 18, 0, "espresso")
            elif variant == "latte":
                pay(2.5, 200, 24, 150, "latte")
            elif variant == "cappuccino":
                pay(3.0, 250, 24, 100, "cappuccino")
            elif variant == "off":
                end_ordering = True
                print("Beep bop, turning off.")
            else:
                end_ordering = True
                print("Sorry, we don't have that. Have a great day!")


order()


