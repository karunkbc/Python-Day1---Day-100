# Project About Treasure Hunt ! 


print(r'''
*******************************************************************************
          |    TREASURE!               |                  |                     |
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
____/______/______/___|o;._     "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''') 
print("Welcome to treasure island.")
print("Your mission is to find the treasure.")
choice1=input("You\'re at a crossroad , where do you want to go.? Left or Right?").lower()
if choice1== "left":
  choice2=input("You come at a middle of lake , . Do you want to swim or wait?")
  if choice2=="wait":
    choice3=input("You arrive at the island unharmed. There is a house with 3 doors. red,  yellow and blue \n").lower()
    if choice3=="red":
      print("Burned by fire.GAME OVER")
    elif choice3=="Blue":
      print("Eaten by beasts.GAME OVER")
    elif choice3=="yellow":
      print("You win")
    else:
      print("GAME OVER")
      
        
  
  else:
    print("Attacked by trout. GAME OVER")
  
else:
  print(f"You fell into a hole. Game Over")
