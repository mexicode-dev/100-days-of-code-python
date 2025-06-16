# ASCII art for the game's title screen
ascii_art = """
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
"""

print(ascii_art)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First choice: left or right
print("You're at a crossroad. Where do you want to go?")
print('Type "left" or "right"')
directions = input().lower()

if directions == "left":
    # Second choice: swim or wait
    print("You've come to a lake. There is an island in the middle of the lake.")
    print('Type "wait" for a boat or "swim" to swim across.')
    directions_1 = input().lower()

    if directions_1 == "swim":
        print("You were attacked by trout. Game Over.")
    elif directions_1 == "wait":
        # Third choice: door color
        print("You arrive at the island unharmed.")
        print("There is a house with 3 doors: one red, one yellow, and one blue.")
        print("Which colour do you choose?")
        directions_2 = input().lower()

        if directions_2 == "red":
            print("Burned by fire. Game Over.")
        elif directions_2 == "blue":
            print("Eaten by beasts. Game Over.")
        elif directions_2 == "yellow":
            print("Congratulations! YOU WIN!")
        else:
            print("That door doesn't exist. Game Over.")
    else:
        print("You hesitated too long. Game Over.")

elif directions == "right":
    print("You fell into a hole. Game Over.")
else:
    print("Invalid direction. Game Over.")
