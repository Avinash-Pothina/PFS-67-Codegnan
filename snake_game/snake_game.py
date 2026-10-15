import csv
import random
import turtle

# Game settings
STEP = 20
START_DELAY_MS = 150
MIN_DELAY_MS = 50
SPEEDUP_MS = 2
TOP_PLAY_LIMIT = 220  # Keep the snake and food below the score display
BOTTOM_LIMIT = -280

# Keep the score file beside this Python script.
SCORE_FILE ="snake_high_score.csv"

score = 0
delay_ms = START_DELAY_MS
segments = []
game_over = False
paused = False


def load_high_score():
    """Read the saved high score, or use zero if no valid score exists yet."""
    try:
        with open(SCORE_FILE,"r", newline="", encoding="utf-8") as file:
            row = next(csv.DictReader(file), None)
            return max(0, int(row["high_score"])) if row else 0
    except (OSError, ValueError, KeyError, StopIteration):
        return 0



def save_high_score(value):
    """Write the high score as a small CSV file."""
    with open(SCORE_FILE,"w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["high_score"])
        writer.writeheader()
        writer.writerow({"high_score": value})


high_score = load_high_score()

# Screen
screen = turtle.Screen()
screen.title("Classic Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)   #it prevents from reloading the screen update

# Snake head
head = turtle.Turtle()
head.speed(0)  #sets animation speed of the snake
head.shape("triangle")
head.color("yellow")
head.penup()  #it prevents from drawing line while moving
head.goto(0, 0)  #sets snake in the middel of the screen
head.direction=None  #it prevents snake from moving at teh starting of the game. 
head.setheading(0)  #it sets the snakes direction while startign a new game if 0=right,90=up,180=left,270=down

# Food
food = turtle.Turtle()
food.speed(0)  #sets animation speed of the food
food.shape("circle")
food.color("red")
food.penup()

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


def update_score():
    pen.clear()
    pen.goto(0, 260)
    pen.write(
        f"Score: {score}  High Score: {high_score}",
        align="center",
        font=("Courier", 18, "normal"),
    )


def random_food_position():
    """Choose an unoccupied cell on the playable grid."""
    occupied = {(int(head.xcor()), int(head.ycor()))}
    occupied.update((int(part.xcor()), int(part.ycor())) for part in segments)
    available = [
        (x, y)
        for x in range(-280, 281, STEP)
        for y in range(BOTTOM_LIMIT, TOP_PLAY_LIMIT + 1, STEP)
        if (x, y) not in occupied
    ]
    if available:
        food.goto(random.choice(available))


def set_direction(direction):
    """Prevent an immediate 180-degree turn."""
    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
    if direction != opposites.get(head.direction):
        head.direction = direction
        headings = {"up": 90, "right": 0, "down": 270, "left": 180}
        head.setheading(headings[direction])


def go_up():
    set_direction("up")


def go_down():
    set_direction("down")


def go_left():
    set_direction("left")


def go_right():
    set_direction("right")


def move():
    if head.direction == "up":
        head.sety(head.ycor() + STEP)
    elif head.direction == "down":
        head.sety(head.ycor() - STEP)
    elif head.direction == "left":
        head.setx(head.xcor() - STEP)
    elif head.direction == "right":
        head.setx(head.xcor() + STEP)


def wrap_at_edges():
    """Reappear at the opposite edge after crossing the screen boundary."""
    if head.xcor() > 280:
        head.setx(-280)
    elif head.xcor() < -280:
        head.setx(280)

    if head.ycor() > TOP_PLAY_LIMIT:
        head.sety(BOTTOM_LIMIT)
    elif head.ycor() < BOTTOM_LIMIT:
        head.sety(TOP_PLAY_LIMIT)


def end_game():
    """Stop the round and show the final score and choices clearly."""
    global game_over, paused
    game_over = True
    paused = False

    # Hide the moving objects so they cannot cover the game-over message.
    head.hideturtle()
    food.hideturtle()
    for segment in segments:
        segment.hideturtle()

    pen.clear()
    pen.goto(0, 60)
    pen.write("GAME OVER - Snake bit itself", align="center", font=("Courier", 20, "bold"))
    pen.goto(0, 20)
    pen.write(f"Score: {score}    High Score: {high_score}", align="center", font=("Courier", 18, "normal"))
    pen.goto(0, -25)
    pen.write("Press R to replay or Q to exit", align="center", font=("Courier", 16, "normal"))
    screen.update()


def toggle_pause():
    """Pause or resume the round when P is pressed."""
    global paused
    if game_over:
        return

    paused = not paused
    if paused:
        # Hide the snake and food behind the pause message for readability.
        head.hideturtle()
        food.hideturtle()
        for segment in segments:
            segment.hideturtle()
        pen.clear()
        pen.goto(0, 25)
        pen.write("PAUSED", align="center", font=("Courier", 22, "bold"))
        pen.goto(0, -15)
        pen.write("Press P to continue", align="center", font=("Courier", 16, "normal"))
    else:
        head.showturtle()
        food.showturtle()
        for segment in segments:
            segment.showturtle()
        update_score()
    screen.update()


def replay_game():
    """Reset the round and start again, keeping the saved high score."""
    global score, delay_ms, game_over
    if not game_over:
        return

    for segment in segments:
        segment.hideturtle()
    segments.clear()
    head.showturtle()
    food.showturtle()
    head.goto(0, 0)
    head.direction = "stop"
    head.setheading(90)
    score = 0
    delay_ms = START_DELAY_MS
    game_over = False
    pen.clear()
    random_food_position()
    update_score()
    screen.update()
    screen.ontimer(game_loop, delay_ms)


def exit_game():
    screen.bye()


def game_loop():
    global score, high_score, delay_ms

    if game_over:
        return
    if paused:
        screen.update()
        screen.ontimer(game_loop, delay_ms)
        return

    # Move the body from tail to head so each part follows the one ahead.
    for index in range(len(segments) - 1, 0, -1):
        segments[index].goto(segments[index - 1].xcor(), segments[index - 1].ycor())
        segments[index].showturtle()
    if segments:
        segments[0].goto(head.xcor(), head.ycor())
        segments[0].showturtle()

    move()
    wrap_at_edges()

    # The game ends only when the head touches the snake's body.
    if any(head.distance(segment) < STEP / 2 for segment in segments):
        end_game()
        return

    if head.distance(food) < STEP:
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lime")
        new_segment.penup()
        new_segment.hideturtle()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score
            try:
                save_high_score(high_score)
            except OSError as error:
                print(f"Could not save high score to {SCORE_FILE}: {error}")
        delay_ms = max(MIN_DELAY_MS, delay_ms - SPEEDUP_MS)

        random_food_position()
        update_score()

    screen.update()
    screen.ontimer(game_loop, delay_ms)


# Keyboard controls
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")
screen.onkeypress(replay_game, "r")
screen.onkeypress(exit_game, "q")
screen.onkeypress(toggle_pause, "p")

random_food_position()
update_score()
game_loop()
screen.mainloop()