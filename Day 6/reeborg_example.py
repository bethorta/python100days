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

number_of_hurdles = 6
while number_of_hurdles > 0:
    hurdle_jump()
    number_of_hurdles -=1