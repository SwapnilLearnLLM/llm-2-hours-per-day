def turn_right():
    turn_left()
    turn_left()
    turn_left()




while not at_goal():
    if not wall_in_front():
        move()
    elif not wall_on_right():
        turn_right()
        move()
    else:
        turn_left()
        
    

    