import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself standing at the entrance of a mysterious cave.")
    print("Your goal is to navigate through the cave and reach the treasure.")
    print("Be careful, as there may be dangers along the way!\n")

def make_choice(choices):
    print("Choose your action:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def cave_entrance():
    print("You enter the cave and see two paths.")
    print("1. Take the left path.")
    print("2. Take the right path.")

    choice = make_choice(["Left", "Right"])

    if choice == 1:
        print("You chose the left path. It leads to a dark tunnel.")
        dark_tunnel()
    else:
        print("You chose the right path. It leads to a narrow bridge.")
        narrow_bridge()

def dark_tunnel():
    print("You venture into the dark tunnel.")
    print("1. Light a torch.")
    print("2. Proceed without a torch.")

    choice = make_choice(["Light torch", "Proceed without torch"])

    if choice == 1:
        print("You light a torch and continue through the tunnel.")
        print("Suddenly, you encounter a swarm of bats!")
        print("1. Fight off the bats.")
        print("2. Retreat slowly.")

        choice = make_choice(["Fight", "Retreat"])

        if choice == 1:
            print("You swing your torch to fend off the bats.")
            print("Successfully navigating through, you reach a room with a treasure chest!")
            print("Congratulations! You've found the treasure.")
        else:
            print("You retreat slowly, avoiding the bats.")
            print("You find yourself back at the cave entrance.")
            cave_entrance()

    else:
        print("You proceed without a torch and stumble in the darkness.")
        print("Unfortunately, you trip on a rock and fall into a pit.")
        print("Game over. You have failed to find the treasure.")

def narrow_bridge():
    print("You walk along the narrow bridge.")
    print("1. Cross the bridge carefully.")
    print("2. Run across the bridge.")

    choice = make_choice(["Cross carefully", "Run across"])

    if choice == 1:
        print("You cross the bridge carefully, maintaining balance.")
        print("You reach the other side safely and find a key.")
        print("1. Pick up the key.")
        print("2. Leave the key.")

        choice = make_choice(["Pick up key", "Leave key"])

        if choice == 1:
            print("You pick up the key and proceed further.")
            print("You encounter a locked door.")
            print("Using the key, you unlock the door and find the treasure!")
            print("Congratulations! You've found the treasure.")
        else:
            print("You leave the key behind and continue.")
            print("Unfortunately, you encounter a locked door without a key.")
            print("Game over. You have failed to find the treasure.")

    else:
        print("You run across the bridge, but it's too unstable.")
        print("The bridge collapses, and you fall into the river below.")
        print("Game over. You have failed to find the treasure.")

# Main game loop
def play_game():
    introduction()
    cave_entrance()

# Run the game
play_game()