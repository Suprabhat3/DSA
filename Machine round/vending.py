# This is bacics use of if else statements with a cool project
# Vending Machine by Suprabhat
print("Choose the item from given list")
print("1. Mango 20$\n2. Orange 20$\n3. Banana 15$")

order = int(input("Enter number of that item : "))

if order not in (1, 2, 3):
    print("You chose a wrong item")

elif order == 1:  # Mango
    money = int(input("Please give the total amount of 20$ : "))
    if money > 20:
        print(f"Here is your change: {money - 20}$")
        print("Here is your mango : 🥭")
    elif money < 20:
        money1 = int(input(f"You gave less money, please give {20 - money}$ more : "))
        if money + money1 == 20:
            print("Here is your mango : 🥭")
        elif money + money1 > 20:
            print(f"Here is your change: {money + money1 - 20}$")
            print("Here is your mango : 🥭")
        else:
            print(f"You don't have enough money, here is your money back {money + money1}$")
    else:
        print("Here is your mango : 🥭")

elif order == 2:  # Orange
    money = int(input("Please give the total amount of 20$ : "))
    if money > 20:
        print(f"Here is your change: {money - 20}$")
        print("Here is your orange : 🍊")
    elif money < 20:
        money1 = int(input(f"You gave less money, please give {20 - money}$ more : "))
        if money + money1 == 20:
            print("Here is your orange : 🍊")
        elif money + money1 > 20:
            print(f"Here is your change: {money + money1 - 20}$")
            print("Here is your orange : 🍊")
        else:
            print(f"You don't have enough money, here is your money back {money + money1}$")
    else:
        print("Here is your orange : 🍊")

elif order == 3:  # Banana
    money = int(input("Please give the total amount of 15$ : "))
    if money > 15:
        print(f"Here is your change: {money - 15}$")
        print("Here is your banana : 🍌")
    elif money < 15:
        money1 = int(input(f"You gave less money, please give {15 - money}$ more : "))
        if money + money1 == 15:
            print("Here is your banana : 🍌")
        elif money + money1 > 15:
            print(f"Here is your change: {money + money1 - 15}$")
            print("Here is your banana : 🍌")
        else:
            print(f"You don't have enough money, here is your money back {money + money1}$")
    else:

        print("Here is your banana : 🍌")

