def turn_around(): 
    turn_left()
    turn_left()
def turn_right() :
   turn_left()
   turn_left()
   turn_left()
def hurdle_jump() : 
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6): 
    hurdle_jump()