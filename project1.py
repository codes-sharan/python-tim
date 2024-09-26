name = input("Hey type your name: ")
print("Hello " + name + " Welcome to my game!" )

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "y" or should_we_play == "yes":
    print("We are gonna play!")
    weapon = input("Choose a weapon (sword/axe): ").lower()

    direction = input("Do you want to go left or right? (left/right) ").lower()
    if direction == "left":
        print("You went left and fell of a cliff, game over, try again...")
    elif direction == "right":
        choice = input("Okay, you now see a bridge, do you want to swim under it or cross it? ")
        if choice == "swim" and weapon == "axe":
            print("You swam under the bridge and found a treasure, congrats you won the game!")
        elif choice == "swim" and weapon == "sword":
            print("You swam under the bridge and got eaten by alligator, you die, game over!")
        else:
            print("You crossed the river, but  got caught by the police, game over!")

    else:
        print("Sory, not a valid answer")

else:
    print("Ok, we are not playing...")
