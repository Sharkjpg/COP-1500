# By Mark Friedman
# Citations:
# Anon, 2008. Stack overflow, Available at: https://stackoverflow.com/.
# A simple text based adventure game


# Introduction


# Displays the title and asks for username
def introduction():
    print("---" * 13)
    print("Welcome to BAG! (Basic Adventure Game)")
    print("---" * 13)
    playerName = input("Please enter your name: ")

    # Asks for date and then formats with slashes
    dateMonth = input("Please enter the current month as a numerical value: ")
    dateDay = input("Please enter the current day as a numerical value: ")
    dateYear = input("Please enter the current year: ")
    # Adds slashes to the date
    print("The current date is: " + dateMonth, dateDay, dateYear, sep='/')
    print("-----------------------------------------------------------------")
    magiccalculator(playerName)


def magiccalculator(userName):
    # Prints story
    print("Congratulations", userName +
          ", you made it to the magical land of Skyselgard.",
          end=' ')  # Removes the automatic new line
    print("As " + '\n' + "a reward for making "
                         "it this far, you get to try our magic calculator")

    # Asks user to select a mode and then
    # asks for two numbers to use in said mode
    userSelection = input(
        "Select a mode" '\n' "1: Addition" '\n' "2. Subtraction"
        '\n' "3. Division" '\n' "4. Multiplication" '\n')
    userNum1 = int(input("Please Enter a number: "))
    userNum2 = int(input("Please Enter another number: "))

    # Selects the correct operation according
    # to user choice and calculates answer
    if userSelection == "1":
        outputNum = str(userNum1 + userNum2)
        print("The result of adding these two numbers is: " + outputNum)
    elif userSelection == "2":
        outputNum = str(userNum1 - userNum2)
        print("The result of subtracting these two numbers is: " + outputNum)
    elif userSelection == "3":
        outputNum = str(userNum1 / userNum2)
        print("The result of dividing these two numbers is: " + outputNum)
    elif userSelection == "4":
        outputNum = str(userNum1 * userNum2)
        print("The result of multiplying these two numbers is: " + outputNum)
    else:
        print("Invalid Input entered")
    print("-----------------------------------------------------------------")
    mildriddleencounter()


# Simple Outro
def outro():
    print("Thank you for playing BAG in pre-pre-alpha!")
    print("Program Terminated")


# Dragon Outro
def dragonoutro():
    print("The dragon egg suddenly starts to hatch as you walk out of the "
          "shop, and soon a baby dragon is born. It immediately recognizes "
          "you as its mother and you ride \nit far off into the hills and "
          "start your own peaceful farm")


# Checks user choice against the answer to make sure it is correct and then
# moves on
def mildriddleencounter():
    print(
        "After a few days traveling, you find a bridge guarded by a large orc"
        " whos says you must answer his riddles to pass")
    userinput1 = input("What has a heart that doesn't beat? "
                       "(Answer: Artichoke): ")
    if userinput1 == "Artichoke" or "artichoke":
        print("Good")
        userinput2 = input("What goes up but never "
                           "comes down? (Answer: Age): ")
        if userinput2 == "Age" or "age":
            print("Amazing")
            userinput3 = input("Now give me a number between 37 and 93: ")
            if 37 < int(userinput3) < 93:
                print("Congratulations, you can pass safely: ")
                print(
                    "------------------------------------"
                    "-----------------------------")
                medieval_shop()
            else:
                print("Wrong, you must return home")
                outro()


# Starts with a list of items, and then has three different functions
# that you can use to sort the items as you want
def medieval_shop():
    print("You come upon a shop and have 500 coins to spend")
    items = {
        "Sword": 50,
        "Bow": 35,
        "Arrow": 1,
        "Shield": 25,
        "Armor": 75,
        "Potion": 10,
        "Book of Spells": 100,
        "Dragon Egg": 500,
        "Ring of Invisibility": 250,
        "Wand": 200
    }
    for item, price in items.items():
        print(f"{item}: {price} gold coins")

# Obtaining user input
    selection = True
    while selection:
        userSelection = input(
            "Filter items by" '\n' "1: Range" '\n' "2. Least Expensive to most"
            '\n' "3. Most Expensive to least" '\n' "4. Buy the "
            "Dragon Egg and leave" '\n' "Enter anything else to"
            " quit" '\n')
        if userSelection == "1":
            min_price = int(input("Enter minimum price: "))
            max_price = int(input("Enter maximum price: "))
            sorted_items = sorted([(item, price) for item,
                                  price in items.items()
                                  if min_price <= price <= max_price],
                                  key=lambda x: x[1])
            # Uses the sorted function to obtain items in range
            print(f"\nItems between {min_price} and {max_price} gold coins:")
            for item, price in sorted_items:
                print(f"{item}: {price} gold coins")
        elif userSelection == "2":
            sorted_items = sorted(items.items(), key=lambda x: x[1],
                                  reverse=True)
            # Also uses sorted function but without an if arguement and
            # is also sorted in reverse
            print("\nItems from most expensive to least:")
            for item, price in sorted_items:
                print(f"{item}: {price} gold coins")
        elif userSelection == "3":
            sorted_items = sorted(items.items(),
                                  key=lambda x: x[1])
            # Also uses sorted function but without an if arguement
            print("\nItems from least expensive to most:")
            for item, price in sorted_items:
                print(f"{item}: {price} gold coins")
        elif userSelection == "4":
            print(
                "---------------------------------------"
                "--------------------------")
            dragonoutro()
            break
        else:
            print("Invalid Input entered, exting shop")
            print(
                "-----------------------------------"
                "------------------------------")
            break
    outro()


introduction()
