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


def is_resources(coffe_resources):
    if resources['water'] > coffe_resources['water']:
        if resources["milk"] > coffe_resources["milk"]:
            if resources["coffee"] > coffe_resources["coffee"]:
                resources["water"] -= coffe_resources["water"]
                resources["milk"] -= coffe_resources["milk"]
                resources["coffee"] -= coffe_resources["coffee"]
                return True
            else:
                return "not enough coffee"
        else:
            return "not enough milk"
    else:
        return "not enough water"


def return_money():
    print("Please insert coins")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    dollars = round(float(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01), 2)
    return dollars


def make_coffee(coffee):
    money = return_money()
    print(f"You have entered {money}$")
    choice_resources = MENU[f'{coffee}']['ingredients']
    choice_cost = MENU[f'{coffee}']['cost']
    if money >= choice_cost:
        if is_resources(choice_resources) == True:
            print(f"Here is your {coffee}")
            change = round(money - choice_cost, 2)
            if change != 0.00:
                print(f"Here is {change}$ in change!")
        else:
            print(f"Sorry not enough {is_resources(choice_resources)}")
    else:
        print("Sorry not enough money")


machine_is_running = True

while machine_is_running:
    choice = input("What do you like?(espresso/latte/cappuccino):")
    if choice == "report":
        print(f"Water:{resources['water']}ml \nMilk:{resources['milk']}ml \nCoffee:{resources['coffee']}g")
    elif choice == "espresso":
        make_coffee(choice)
    elif choice == "latte":
        make_coffee(choice)
    elif choice == "cappuccino":
        make_coffee(choice)
    else:
        print("Please type again")
