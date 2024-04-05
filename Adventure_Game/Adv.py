import time

i = input("Enter your name: ")
print("Welcome", i, "to the adventure.")
a = input("We have a nice map for you - Land (Please type 'land' to start the game): ")

if a.lower() == "land":
    print("You chose land. Let's go")
    time.sleep(1.5)
    answer = input("As you chose land, you were walking and now you have 2 paths (left, right). Choose one: ")

    if answer.lower() == "left":
        print("Nice choice. You found a car that will help you travel faster.")
        time.sleep(1.5)
        answer = input("As you were travelling, you found a wallet but not sure whose. What will you do? (Take it or Leave it): ")

        if answer.lower() == "take it":
            print("You should not take money like this, but as you chose to take it, you found $20")
            time.sleep(1.5)
            answer = input("You were travelling and you found 2 roads again (Left or Right): ")
            if answer.lower() == "left":
                print("You were caught by the police as you stole the money! Always choose loyalty.")
                print("---GAME END---")
            elif answer.lower() == "right":
                print("You were caught by the police as you stole the money! Always choose loyalty.")
                print("---GAME END---")
        elif answer.lower() == "leave it":
            print("Nice man, I like your loyalty. This game gives you $40 for your loyalty.")
            time.sleep(1.5)
            answer = input("You were travelling and you found 2 roads again (Left or Right): ")
            if answer.lower() == "right":
                print("You found a store. There are many options to buy from the store. You can buy only one item so be careful.")
                items = ["Apple - It gives you happiness as told by the shopkeeper. ($40)", "Water - Does nothing but it's good for health. ($5)", "Laptop - You can do many things from this laptop but you don't have internet now ($100)"]
                time.sleep(1.5)
                print(items)
                time.sleep(1.5)
                answer = input("Enter the name of the item you want to buy: ")
                if answer.lower() == "laptop":
                    print("You don't have the money. You lose!")
                    print("---GAME END----")
                elif answer.lower() == "apple":
                    print("The apple was poisoned. You Died!")
                    print("---GAME END---")
                elif answer.lower() == "water":
                    print("The water gave you special powers and the shopkeeper lied that it was normal water.")
                    time.sleep(1.5)
                    answer = input("As you have special powers, would you like to save the world or become a criminal (Save world or criminal): ")
                    if answer.lower() == "save world":
                        print("As you chose to save the world, everyone is proud of you and now you are living happily. Nice mind your all selections were correct.")
                        print("---GAME END---")
                    elif answer.lower() == "criminal":
                        print("Shame on you! As you chose criminal, everyone hates you now.")
                        print("---GAME END---")
                    else:
                        print("Wrong option. LOST")
            else:
                print("Invalid option. You lose")
        else:
            print("Invalid option. You lose")
    else:
        print("You die! Sorry.")
else:
    print("Invalid Option. You lose.")
