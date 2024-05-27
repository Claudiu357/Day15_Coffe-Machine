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

machine_is_running = True

while machine_is_running:
    choice = input("What do you like?(espresso/latte/capuccino):")
    if choice == "report":
        print(f"Water:{resources['water']}ml \nMilk:{resources['milk']}ml \nCoffee:{resources['coffee']}g")
    elif choice == "espresso":
        print("Please insert coins")
    elif choice == "latte":
        print("Please insert coins")
    elif choice == "capuccino":
        print("please insert  coins")
