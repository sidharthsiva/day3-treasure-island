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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

condition1 = input(print("Now which way you want to go, left ? or right? "))

if (condition1.lower()) == "left":
  print("Now there is a lake in front of you")
  condition2 = input(print("What you want to do now, either you want to 'swim' and cross the lake? or 'wait' for boat?"))
  if (condition2.lower())=="wait":
    print("Boat came and helped you to cross the lake.")
    condition3 = input(print("Last stage, there are three doors infront of you! which one do you want to open? red? or yellow? or blue?"))
    if (condition3.lower()) == "red":
      print("It was an volcano and you got burnt to death. Game Over")
    elif (condition3.lower()) == "blue":
      print("There was deadly pirahana made you as their dinner. Game Over")
    elif (condition3.lower()) == "yellow":
      print("The room is filled with gold. Treasure found! Mission Accomplished")
    else:
      print("Chose a wrong way, so you are dead. Game Over")
  else:
    print("Shark in the lake ate you for lunch. Game Over.")
else:
  print("You slipped into a hole. Game Over.")