from sys import exit
# Build a CLI RPG game following the instructions from the course.


# Ask the player for their name.
name= input("Hello please enter your name!:")
# Display a message that greets them and introduces them to the game world.
print(f"Hello {name}, welcome to the CLI game world!")
# Present them with a choice between two doors.
doors = input("You have two options, to go through a left door, or a right door. Which do you choose?")
# If they choose the left door, they'll see an empty room.
if doors == "left door":
    print("You see any empty room")
    go_back= input("Would you like to turn back?") 
    if go_back == "no":
        take_sword = input("You look around and see a sword. Do you take the sword?")
        if take_sword == "yes":
            print("You now go to the next room and see the dragon")
            fight = input("You see a dragon do you fight it?")
            if fight == "yes":
                    print("You slay the dragon and win the game")
            elif fight == "no":
                    print("You're quite the chicken.")
    elif go_back == "yes":
        print("You are back in the original room.")
        doors = input("Do you want to go into the other room?" )
        if doors == "yes":
                fight = input("You see a dragon do you fight it?")
                if fight == "yes":
                    print("The dragon kills you because you don't have the sword from the other room.")
                elif fight == "no":
                    print("You're quite the chicken.")
        elif doors == "no":
                print("Why even bother playing the game then?")
# If they choose the right door, then they encounter a dragon.
elif doors == "right door":
    fight=input("You encouter a dragon! Do you want to fight it?")
    if fight == "yes":
            print("The dragon eats you alive.")
    elif fight == "no":
            print(" You return back to the original room")

  
        
            
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.
