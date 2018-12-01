#Name: ZHOU Jingwen
#STD:  20493253


# Lab 7 - The Pacman Game
#
import turtle
import math
import random


# Setup the turtle window
turtle.setup(800, 700)
turtle.title("COMP1021 - Pacman")
turtle.bgcolor("black")

# Setup the turtle
turtle.speed(0)
turtle.up()
turtle.hideturtle()
turtle.tracer(False)


# Define the game timing (30 frames per second)
frame_time = 1000 // 30

# Define the maze information
maze_x       = -300
maze_y       = -270
maze_columns = 21
maze_rows    = 19

# Define the ghost information
ghost_size = 30
ghost_speed = 6
ghost_start_x = 0
ghost_start_y = 0
ghosts = []

# Define the tile information
tile_size = 30

# Define the food information
food_size  = 10
food_count = 0
# Define the pacman information
pacman_size  = 30
pacman_speed = 6
pacman_x     = 0
pacman_y     = 0

# Create the variables for the pacman movement
current_move = ""   # This is the current movement
next_move = ""      # This is the next movement


# Maze of the game
#   + : wall
#   . : food
#   o : power food
#   P : starting position of pacman
#   G : starting position of ghosts
maze = [
    #012345678901234567890 - total 21 columns
    "+++++ +++++++++++++++", # 0
    "+o.................o+", # 1
    "+.++++++....+++++++.+", # 2
    "+......+.......+....+", # 3
    "+....+....o....+....+", # 4
    "+..+...........+....+", # 5
    "+.++++++....++++....+", # 6
    "+...................+", # 7
    "+..++....+++....++..+", # 8
    "+.o.++..++.++..++.o.+", # 9
    "+....++++...++++....+", # 10
    "+...................+", # 11
    "+++++.+++   +++.+++++", # 12
    "     .+...G...+.     ", # 13
    "+++++.+++++++++.+++++", # 14
    "+.........P.........+", # 15
    "+.+++.+++++++++.+++.+", # 16
    "+o....+       +....o+", # 17
    "+++++ +       +++++++"  # 18 - total 19 rows
]


#
# Task 1 - Draw the maze
#
for col in range(maze_columns):
    for row in range(maze_rows):
        # Get the tile
        tile = maze[row][col]

        # Task 1.1 - Locate the tile and move to the tile position
        #
        # - Find the x, y position of the tile in the turtle window
        tile_x = maze_x + col*tile_size
        tile_y = maze_y + (maze_rows - row -1)* tile_size
        # - Put the turtle to the tile position
        turtle.goto( tile_x, tile_y)
        # Task 1.2 - Draw the tiles according to the tile symbol
        #
        # - Draw the tiles for walls, food and power food
        if tile == "+":   # wall
            turtle.shape("square")
            turtle.shapesize( tile_size/20 , tile_size/20 ) # 1 denote 20 pixels
            turtle.color("blue", "black")
            turtle.stamp()
        elif tile == ".": # food
            turtle.color("yellow")
            turtle.dot( food_size/2)

            food_count += 1
        elif tile == "o": # power food
            turtle.color("white")
            turtle.dot( food_size )
            food_count += 1
            
        elif tile == "P": # pacman
        # - Initialize the position of pacman
            pacman_x = tile_x
            pacman_y = tile_y
        elif tile == "G": # ghost
        # - Initialize the position of ghost
            ghost_start_x = tile_x
            ghost_start_y = tile_y
#————————————————————————————————————————————————
# Assign 2.1 - Drawing the ghost
#####################################
def draw_ghost(ghost, move):
    #Save the original color of each ghost, i.e. cyan, blue, orange, pink
    ghostColor1,ghostColor2 = ghost.color()
    ghost.clear()
    # clear the ghost prev. image, redraw in the following
    #get the ghost position   by using ghost.xcor()  ghost.ycor()
    ghost_x = ghost.xcor()
    ghost_y = ghost.ycor()
    # Draw the ghost body
    ghost.hideturtle()
    #draw ghosts with their original colors i.e. cyan, blue, orange, pink
    ghost.color(ghostColor1)
    ghost.begin_fill()
    ghost.left(90)
    ghost.circle(15, 180)
    ghost.forward(15)
    ghost.up()
    ghost.left(90)
    ghost.forward(3.75)
    ghost.down()
    ghost.color(ghostColor1)
    ghost.dot(7.5)
    ghost.up()
    ghost.forward(7.5)
    ghost.down()
    ghost.dot(7.5)
    ghost.up()
    ghost.forward(7.5)
    ghost.down()
    ghost.dot(7.5)
    ghost.up()
    ghost.forward(7.5)
    ghost.down()
    ghost.dot(7.5)
    ghost.forward(3.75)
    ghost.left(90)
    ghost.forward(15)
    ghost.end_fill()
    # Draw the ghost eyes

    # get the ghost moving direction from "move" (the 2nd param. in the function)
    ghost_move = move
            
    # make the eyes "looking" towards the direction of movement
    if ghost_move == "left":
        ghost.up()
        ghost.left(90)
        ghost.forward(7.5)
        ghost.color("white")
        ghost.dot(7.5)
        ghost.forward(3.75)
        ghost.color("black")
        ghost.dot(3.75)
        ghost.forward(11.25)
        ghost.color("white")
        ghost.dot(7.5)
        ghost.forward(3.75)
        ghost.color("black")
        ghost.dot(3.75)
        ghost.left(180)
    elif ghost_move == "right":
        ghost.up()
        ghost.left(90)
        ghost.forward(7.5)
        ghost.color("white")
        ghost.dot(7.5)
        ghost.backward(3.75)
        ghost.color("black")
        ghost.dot(3.75)
        ghost.forward(15)
        ghost.color("white")
        ghost.dot(7.5)
        ghost.backward(3.75)
        ghost.color("black")
        ghost.dot(3.75)
        ghost.left(180)
    elif ghost_move == "down":
        ghost.up()
        ghost.left(90)
        ghost.forward(7.5)
        ghost.color("white")
        ghost.dot(7.5)
        ghost.left(90)
        ghost.forward(3.75)
        ghost.color("black")
        ghost.dot(3.75)
        ghost.backward(3.75)
        ghost.right(90)
        ghost.forward(15)
        ghost.color("white")
        ghost.dot(7.5)
        ghost.left(90)
        ghost.forward(3.75)
        ghost.color("black")
        ghost.dot(3.75)
        ghost.backward(3.75)
        ghost.right(90)
        ghost.left(180)
    else:
        ghost.up()
        ghost.left(90)
        ghost.forward(7.5)
        ghost.color("white")
        ghost.dot(7.5)
        ghost.right(90)
        ghost.forward(3.75)
        ghost.color("black")
        ghost.dot(3.75)
        ghost.backward(3.75)
        ghost.left(90)
        ghost.forward(15)
        ghost.color("white")
        ghost.dot(7.5)
        ghost.right(90)
        ghost.forward(3.75)
        ghost.color("black")
        ghost.dot(3.75)
        ghost.backward(3.75)
        ghost.left(90)
        ghost.left(180)
    #After drawing eyes, restore the original ghost color to the ghost turtle
    ghost.color(ghostColor1,ghostColor1)
    ghost.goto(ghost_x,ghost_y)
        
#---------------------------------------------
# Assign 2.2 - Drawing the pacman
#########################################
pacman_mouth_open = 40  # max mouth open angle
pacman_mouth_change = -8 # it can be either -8  or +8 
def draw_pacman():
    global pacman_mouth_open, pacman_mouth_change, mouth_angle,n, motion
 
    pacman.clear()
    # set the pacman heading dir. (i.e. =current_move),
    #so that pacman's mouth is facing that dir.

    pacman_mouth_direction = current_move
    
    if pacman_mouth_direction == "right":
        pacman.setheading(0)
    elif pacman_mouth_direction == "left":
        pacman.setheading(180)
    elif pacman_mouth_direction == "down":
        pacman.setheading(270)
    elif pacman_mouth_direction == "up":
        pacman.setheading(90)
    else:
        pacman.setheading(0)
	# ...
	# Draw the Pacman with mouth
       

    pacman.left(pacman_mouth_open)
    pacman.begin_fill()
    pacman.forward(15)
    pacman.left(90)
    pacman.circle(15,360 - 2*pacman_mouth_open)
    pacman.left(90)
    pacman.forward(15)
    pacman.left(pacman_mouth_open)
    pacman.end_fill()
    # update the mouth movement angle for the next movement
    if pacman_mouth_open == 40:
        pacman_mouth_change = -8
    elif pacman_mouth_open == 0:
        pacman_mouth_change = 8

    pacman_mouth_open = pacman_mouth_open + pacman_mouth_change
    
    
# Task 2.1 - Create the pacman turtle
#
# - Use turtle.Turtle() to make your pacman

# - Make a yellow turtle circle shape as your pacman
# - Put your pacman at the starting position
pacman = turtle.Turtle( )
pacman.color( "yellow" )
pacman.up()
pacman.goto( pacman_x, pacman_y )
pacman.hideturtle()
draw_pacman()
# Task 2.2 - Handle the movement keys
#
# - Complete the down, left and right movement keys for the pacman
#   (the up movement has been given to you)

# Handle the "Up" key for moving up
#---------------------------------------------------------------------------------

def move_up():
    global next_move
    next_move = "up"
def move_down():
    global next_move
    next_move = "down"
def move_right():
    global next_move
    next_move = "right"
def move_left():
    global next_move
    next_move = "left"

# Set up the key press events
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_down, "Down")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_left, "Left")

# Need to use listen for key events to work
turtle.listen()


#------------------------------------------------------
# Assign 2.1 - Create 4 ghosts of different colors
for color in ["red", "pink", "cyan", "orange"]:
    ghost = turtle.Turtle( )
    ghost.shape("circle")
    ghost.shapesize( ghost_size/20, ghost_size/20 ) # 1 unit=20
    ghost.color(color)
    ghost.up()
    ghost.goto( ghost_start_x, ghost_start_y )
    ghosts.append( {"turtle":ghost, "move": "left"})

###############Assign 2 - cheat mode
#-----------------------------
protect_mode = False

def protect_mode():
    global protect_mode
    if protect_mode == False:
        protect_mode = True
        pacman.color("yellow")
        
    else:
        pacman.color("green")
        protect_mode = False

     


turtle.onkeypress(protect_mode,"c")
turtle.listen()








###### Assign 2 - score
#---------------------------
score = 0
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.color ("white")
score_turtle.up()
score_turtle.goto(-310,300)
turtle.down()
score_turtle.write("Score = "+ str(score), align="left", \
                   font=("Arial", 20, "normal"))
turtle.up()







# This is the game main loop, which is mainly used to:
#
# - Determine the movement of pacman
# - Determine if pacman hits a wall or food

def game_loop():
    global current_move, next_move
    global pacman_x, pacman_y
    global food_count

    # Task 2.4 - Handle the pacman next move
    #
    # - Update the condition of the following if statement so that
    #   pacman can only move along the rows and columns of the maze
    if  (pacman_x - maze_x) % tile_size == 0  and \
        (pacman_y - maze_y) % tile_size == 0  and \
        next_move != "":   # refined 
        current_move = next_move
        next_move = ""


    # Task 2.3 - Find the pacman new position
    #
    # - Complete the down, left and right moves
    #   (the up move has been given to you)
   
    if current_move == "up":
        new_x = pacman_x
        new_y = pacman_y + pacman_speed
    elif current_move == "down":
        new_x = pacman_x
        new_y = pacman_y - pacman_speed
    elif current_move == "right":
        new_x = pacman_x + pacman_speed
        new_y = pacman_y
    elif current_move == "left":
        new_x = pacman_x - pacman_speed
        new_y = pacman_y 
    else:
        new_x = pacman_x
        new_y = pacman_y

    # Lab 8 - Tunneling
    #Pacman going out of the Left Right borader
    if new_x < maze_x: # left boarder
        new_x = maze_x + (maze_columns - 1) * tile_size
    elif new_x > (maze_x + (maze_columns-1)*tile_size):
        new_x = maze_x
        
    # handle going out of the Top, bottom gameboard
    if new_y < maze_y: # bottom boarder
        new_y = maze_y+ (maze_rows-1) * tile_size
    elif new_y > (maze_y + (maze_rows-1)*tile_size):
        new_y = maze_y
        
    # new_x, new_y now contains the intended position the pacman
    #wants to goto, BUT not take effect yet.
    #(until it pass the collision)

    #
    # Task 3 - Handle the collision of pacman, food and walls
    #
    for i in range(maze_columns):
        for j in range(maze_rows):
            # Get the tile
            tile = maze[j][i]

            # Task 3.1 - Locate the tile and calculate the distance
            #
            # - Find the x, y position of the tile in the turtle window
            tile_x = maze_x + i*tile_size
            tile_y = maze_y + (maze_rows - j -1)* tile_size
            # - Find the distance between pacman and the tile in dx, dy
            dx = math.fabs( new_x - tile_x )
            dy = math.fabs( new_y - tile_y )

            # Task 3.2 - Collision detection
            #
            # - If pacman collides with any wall, stop pacman from moving
            if dx < (pacman_size + tile_size) / 2 and \
               dy < (pacman_size + tile_size) / 2 and \
               tile == "+":  # reset the new_x, new_y back to the curr. pacman position
                new_x = pacman_x
                new_y = pacman_y
                break;
                
            # - normal food, eat the food 
            elif dx < (pacman_size + food_size) / 2 and \
               dy < (pacman_size + food_size) / 2 and \
               tile == ".":
                global score
                score= score + 1
                score_turtle.clear()
                score_turtle.down()
                score_turtle.write("Score = "+ str(score), align="left",\
                                   font=("Arial", 20, "normal"))
                score_turtle.up()



            # remove the food from the window and the maze list
                turtle.goto( tile_x, tile_y )
                turtle.color("black")
                turtle.dot( food_size/2 )
                # rebui9ld the whole string in maze[j]
                maze[j] = maze[j][:i] + " " + maze[j][i+1:]
                food_count -= 1
                
            # - power food, eat the food 
            elif dx < (pacman_size + food_size) / 2 and \
               dy < (pacman_size + food_size) / 2 and \
               tile == "o":
                score= score + 5
                score_turtle.clear()
                score_turtle.down()
                score_turtle.write("Score = "+ str(score), align="left", \
                                   font=("Arial", 20, "normal"))
                score_turtle.up()
            # remove the food from the window and the maze list
                turtle.goto( tile_x, tile_y )
                turtle.color("black")
                turtle.dot( food_size)
                # rebui9ld the whole string in maze[j]
                maze[j] = maze[j][:i] + " " + maze[j][i+1:]
                food_count -= 1
                
        # Task 2.3 - Move the pacman
        #
        # - Move pacman to the new position
        # - Update pacman_x and pacman_y
        
    pacman.goto(new_x, new_y)
    pacman_x = new_x
    pacman_y = new_y
    draw_pacman()
    turtle.update()
#--------------------------Above is pacman code--------------------------------
    ## lab 8 2.1 move the ghost
    #------------Add inj the ghost code--------------
    for ghost_item in ghosts:
        ghost = ghost_item["turtle"]
        ghost_move = ghost_item["move"]

        ghost_x = ghost.xcor()
        ghost_y = ghost.ycor()

        if (ghost_x - maze_x) % tile_size == 0 and \
           (ghost_y - maze_y) % tile_size == 0:
            ## given the ghost x, y it returns the i (col#), j (row#)
            i = int((ghost_x - maze_x) / tile_size)
            j = (maze_rows - 1) - int((ghost_y - maze_y) / tile_size)

            moves=[] # a list to store the valid moving dir. for the ghost
            #check the content of the surrounding 4 tiles
            if j > 0 and maze[j - 1][i] != "+":
                moves.append("up")
            if j < maze_rows-1 and maze[j + 1][i] != "+":
                moves.append("down")
            if i < maze_columns - 1 and maze[j][i+1] != "+":
                moves.append("right")
            if i > 0 and maze[j][i-1] != "+":
                moves.append("left")

            ## avoid moving around
            if len(moves) >1:
                if ghost_move == "up" and "down" in moves:
                    moves.remove( "down" )
                if ghost_move == "down" and "up" in moves:
                    moves.remove( "up" )
                if ghost_move == "right" and "left" in moves:
                    moves.remove( "left" )
                if ghost_move == "left" and "right" in moves:
                    moves.remove( "right" )
                
                
            print ( moves )
            ghost_item["move"] = random.choice(moves)
            ghost_move = ghost_item["move"]
            
    # process the NEW ghost movement   
        if ghost_move == "up":
            ghost_x = ghost_x
            ghost_y = ghost_y + ghost_speed
        elif ghost_move == "down":
            ghost_x = ghost_x
            ghost_y = ghost_y - ghost_speed
        elif ghost_move == "right":
            ghost_x = ghost_x + ghost_speed
            ghost_y = ghost_y
        elif ghost_move == "left":
            ghost_x = ghost_x - ghost_speed
            ghost_y = ghost_y 
        else:
            ghost_x = ghost_x
            ghost_y = ghost_y

            # current ghost position 
        ghost.goto( ghost_x, ghost_y )
    # assign 2 draw the ghost
        draw_ghost(ghost, ghost_move)



# Exited the above FOR LOOP, after process the movement of all ghosts
# ---------------- the above code is the movement of one ghost------------------
    # the for loop above will process one ghost at a time
    # collision checking between pacman and any ghosts
    for ghost_item in ghosts:
        ghost = ghost_item["turtle"]
        ghost_move = ghost_item["move"]
        ghost_x = ghost.xcor()
        ghost_y = ghost.ycor()
    # find dx, dy between pacman and ghost
        dx = math.fabs( pacman_x - ghost_x )
        dy = math.fabs( pacman_y - ghost_y )
    # Game over massage
        if dx < (pacman_size + tile_size) / 2 and \
           dy < (pacman_size + tile_size) / 2 and protect_mode != False:
            turtle.goto(0,-20)
            turtle.color("White")
            turtle.write("Game Over:[", font=("Arial", 50, "bold"),
                         align="center")
            return   # exit the game

            

    #--you win end game proc.------------------
    #eat all of the food, you win  message
    #global food count; 
        if food_count == 0:
            turtle.goto(0,-20)
            turtle.color("white")
            turtle.write("You win :0", font=("Arial", 50, "bold"),
                         align="center")
            return   # exit the game
        
    # Update the window content
    turtle.update()
    
    # Keep on running the game loop
    turtle.ontimer(game_loop, frame_time)
#-------------------------------------------------------------------------------------------
# Start the game loop
game_loop()

turtle.done()

""" def draw_ghost (,)
need to have two eyes, eyebow looking at the moving direction"""




