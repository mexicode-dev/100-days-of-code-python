# Maze Escape - Day 6 Challenge from "100 Days of Code: Python"
# The goal is to guide the agent through the maze using simple commands.
# Author: [Kamil]

def turn_right():
    # The Turtle module does not provide a turn_right() function,
    # so we define it by turning left three times.
    turn_left()
    turn_left()
    turn_left()

# Main loop: keep moving until the goal is reached
while not at_goal():
    # If there is no wall on the right, turn right and move forward
    if right_is_clear():
        turn_right()
        move()
    # If there is a clear path ahead, move forward
    elif front_is_clear():
        move()
    # If there are walls ahead and to the right, turn left
    else:
        turn_left()
