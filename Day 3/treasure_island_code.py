Summary each one needs to be in a variable and then add the variable together to get the value. Then do the if statements. 

Treasure Island Code: 
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
direction = input('Do you want to go "left" or "right"?\n').lower()
if direction == "left":
  river = input('You have reached the river. Do you want to swim or wait for a boat? Type "swim" or "wait"\n').lower()
  if river== "wait":
    door = input('You enter the boat and cruise down the river. You have arrived at a group of doors.  Which door do you want to go through  "red", "blue", or "yellow"? \n').lower()
    if door == "red":
      print("You have fallen into a fire pit. Game Over!")
    elif door =="blue":
      print("You have walked into a lion's den and are their next meal. Game Over!")
    elif door == "yellow": 
      print("You have entered the treasure room! You win!")
    else: print("You have entered a door that doesn't exist. Game Over!")
  else: print("You are on the wrong side of the RIVER! You have drowned. Game Over")
else: print("You are dead. Game Over")

#ASCII Art: https://ascii.co.uk/art