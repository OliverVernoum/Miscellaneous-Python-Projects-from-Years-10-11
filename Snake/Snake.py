import turtle as t
import random
import time
import os
import re
score = 0
#Loads high score from a file
def load_high_score(filename="highscore.txt"):
    try:
        # Normalize the filename and ensure it exists
        filename = os.path.expanduser(str(filename))
        if not os.path.isfile(filename):
            return 0
        # Read file safely with encoding and ignore bad bytes
        with open(filename, "r", encoding="utf-8", errors="ignore") as file:
            contents = file.read().strip()
            if not contents:
                return 0
            # Try direct int conversion first, then extract the first integer if needed
            try:
                return int(contents)
            except ValueError:
                m = re.search(r'-?\d+', contents)
                if m:
                    return int(m.group())
                return 0
    except OSError:
        # Catch OS-related errors (including invalid arguments) and return 0 as fallback
        return 0

high_score = load_high_score()  # Load high score from file

# Saves high score to a file
def save_high_score(score, filename="highscore.txt"):
    high_score = load_high_score(filename)
    if score > high_score:
        with open(filename, "w") as file:
            file.write(str(score))
# Function to update the score display
def update_score():
    global score, high_score
    score_display.clear()
    if score > high_score:
        high_score = score
    score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Pixelify Sans", 24, "normal"))




window=t.Screen() #Creates the screen
window.title("Snake") #Titles the window
window.bgcolor("Green") #Sets the background colour of the window
window.setup(width=800,height=600) #Sets the window's parameters
window.tracer(0) #Turns off the screen updates
window.listen()#Makes the window listen for key presses

# Create a turtle object for the score display
score_display = t.Turtle()  # Create a turtle object for the score display
score_display.speed(0)  # Set the animation speed to the fastest
score_display.color("Black")  # Set the color of the score display to white
score_display.penup()  # Disable drawing when the score display moves
score_display.hideturtle()  # Hide the turtle cursor
score_display.goto(0, 260)  # Position the score display at the top of the screen
score_display.write("Score: 0 High Score={}".format(high_score), align="center", font=('Comic Sans',24, 'normal'))  # Display the initial score

# Create a turtle object for the food
food=t.Turtle()  # Create a turtle object for the food
food.speed(0)
food.shape("square")  # Set the shape of the food to a square
food.color('Black')  # Set the color of the food to black
food.penup()
def gen_x_coord():
    return random.randint(-390, 390)  # Generate a random x-coordinate within the screen boundaries
def gen_y_coord():
    return random.randint(-290, 290)  # Generate a random y-coordinate within the screen boundaries
food.goto(gen_x_coord(), gen_y_coord())  # Place the food at a random position on the screen
food.showturtle()  # Show the food turtle
segments = []


# Snake head
head = t.Turtle()  # Create a turtle object for the snake's head
head.speed(0)  # Set the animation speed to the fastest
head.shape("square")  # Set the shape of the snake's head to a square
head.color("Dark Green")  # Set the color of the snake's head to black
head.penup()  # Disable drawing when the snake moves
head.goto(0, 0)  # Place the snake's head at the center of the screen
head.direction = "stop"  # Initialize the direction of the snake as stopped
head.shapesize(stretch_wid=1, stretch_len=1)  # Set the size of the head

# Functions to change direction
def go_up():
    if head.direction != "down":  # Prevent the snake from reversing direction
        head.direction = "up"  # Change the direction to up

def go_down():
    if head.direction != "up":  # Prevent the snake from reversing direction
        head.direction = "down"  # Change the direction to down

def go_left():
    if head.direction != "right":  # Prevent the snake from reversing direction
        head.direction = "left"  # Change the direction to left

def go_right():
    if head.direction != "left":  # Prevent the snake from reversing direction
        head.direction = "right"  # Change the direction to right

# Function to move the snake
def move():
    if head.direction == "up":  # If the direction is up
        y = head.ycor()  # Get the current y-coordinate of the head
        head.sety(y + 20)  # Move the head 20 units upward
    if head.direction == "down":  # If the direction is down
        y = head.ycor()  # Get the current y-coordinate of the head
        head.sety(y - 20)  # Move the head 20 units downward
    if head.direction == "left":  # If the direction is left
        x = head.xcor()  # Get the current x-coordinate of the head
        head.setx(x - 20)  # Move the head 20 units to the left
    if head.direction == "right":  # If the direction is right
        x = head.xcor()  # Get the current x-coordinate of the head
        head.setx(x + 20)  # Move the head 20 units to the right

# Keyboard bindings
window.onkey(go_up, "w")  # Bind the "w" key to the go_up function
window.onkey(go_down, "s")  # Bind the "s" key to the go_down function
window.onkey(go_left, "a")  # Bind the "a" key to the go_left function
window.onkey(go_right, "d")  # Bind the "d" key to the go_right function
window.onkey(go_up, "Up")  # Bind the Up arrow key to the go_up function
window.onkey(go_down, "Down")  # Bind the Down arrow key to the go_down function
window.onkey(go_left, "Left")  # Bind the Left arrow key to the go_left function
window.onkey(go_right, "Right")  # Bind the Right arrow key to the go_right function




# Main game loop
def game_loop():
    global score
    global high_score
    update_score()  # Update the score display
    
    

    window.update()  # Refresh the screen
    move()


    # Check for collision with itself 
    for segment in segments:
        if segment.distance(head) < 20:  # If the snake collides with itself
            time.sleep(1)  # Pause for a moment
            head.goto(0, 0)
            head.direction = "stop"
            # Clear the segments properly after collision
            for segment in segments:
                segment.goto(1000, 1000)  # Hide segments
            segments.clear()  # Clear the segment list
            save_high_score(score)  # Save high score
            score = 0  # Reset score after collision
            update_score()  # Update the score display
            score_display.write("Score: 0 High Score={}".format(high_score), align="center", font=('Pixelify Sans',24, 'normal'))  # Display the initial score
            

    # Check for border collision
    if head.ycor() > 290 or head.ycor() < -290 or head.xcor() > 390 or head.xcor() < -390:
        head.goto(0, 0)
        head.direction = "stop"
        save_high_score(score)  # Save high score
        score = 0  # Reset score after collision
        update_score()  # Update the score display
        score_display.write("Score: 0 High Score={}".format(high_score), align="center", font=('Pixelify Sans',24, 'normal'))  # Display the initial score
        

        # Hide and clear segments after border collision
        for segment in segments:
            segment.goto(1000, 1000)  # Move segments out of view
        segments.clear()  # Clear the segment list

    # Check for food collision
    if head.distance(food) < 20:
        food.goto(gen_x_coord(), gen_y_coord())  # Relocate food

        # Add new segment to the snake
        new_segment = t.Turtle()
        new_segment.speed(0)
        new_segment.color("black")
        new_segment.shape("square")
        new_segment.penup()
        segments.append(new_segment)
        score += 1
        update_score()  # Update the score display

    # Move the snake's body segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move the first segment to the head's position
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    
    window.update()  # Refresh the screen
    update_score()  # Update the score display
    window.ontimer(game_loop, 100)  # Call game_loop function again after 100 milliseconds
game_loop()
t.done()



