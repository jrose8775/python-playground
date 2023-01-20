print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right"\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" if you swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You come to a cabin in the woods. You walk inside and there are three doors. One red, one yellow and one blue. Which door do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire! Game Over.\n")
            exit()
        elif choice3 == "yellow":
            print("There is a large golden chest in the middle of the floor. You've won the Treasure!\n")
        elif choice3 == "blue":
            print("There is an evil doll who is staring at you. Everything goes black. Game Over.\n")
            exit()
        else:
            print("You left the area because cabins are creepy. No Treasure.\n")
            exit()
    else:
        print("You couldn't make it across and drowned. Game Over.\n")
        exit()
else:
    print("You fell into a hole. Game Over.\n")
    exit()