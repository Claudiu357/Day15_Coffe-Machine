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
# def is_resources(choice_coffe):
#     coffe_ingredients = MENU[choice_coffe]['ingredients']
#     if coffe_ingredients['water'] > resources["water"] :

def return_money():
    print("Please insert coins")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    dollars = round(float(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01), 2)
    return dollars

machine_is_running = True

while machine_is_running:
    choice = input("What do you like?(espresso/latte/capuccino):")
    if choice == "report":
        print(f"Water:{resources['water']}ml \nMilk:{resources['milk']}ml \nCoffee:{resources['coffee']}g")
    elif choice == "espresso":
        print("Please insert coins")
    elif choice == "latte":
        money = return_money()
        print(f"You have entered {money}$")
    elif choice == "capuccino":
        print("please insert  coins")
