"""
File: project.py
-----------------
This program is an empty program for your final project.  Update this comment
with a summary of your program!
"""
from graphics import Canvas
import random
import time
canvas = Canvas()
CANVAS_WIDTH = 420
CANVAS_HEIGHT = 600
# Radius of the star in pixels
STAR_RADIUS = 1

# Number of the star
STAR_NUMBER = 300

# Radius of the ball in pixels
BALL_RADIUS = 40

# The ball's minimum and maximum horizontal velocity; the bounds of the
# initial random velocity that you should choose (randomly +/-).
VELOCITY_Y_MIN = 6
VELOCITY_Y_MAX = 10

# The rocket's maximum velocity
ROCKET_VELOCITY_Y_MAX = 25

# Animation delay or pause time between ball moves (in seconds)
DELAY = 1 / 60

# Dimensions of the start button
START_BUTTON_WIDHT = 90
START_BUTTON_HEIGHT = 20

# Dimensions of the rocket
ROCKET_WIDTH = 5
ROCKET_HEIGHT = 20

# Dimensions of the paddle
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10

# Dimensions of the GAP
GAP = 30

# Dimensions of the starfighter
STARFIGHTER_WIDHT = 30
STARFIGHTER_HEIGHT = 50

# Dimensions of the images
IMAGE_WIDHT = 100
IMAGE_HEIGHT = 170

# Offset of the paddle up from the bottom
PADDLE_Y_OFFSET = 30

# Possibility number to create rockets with a certain probability
POSSIBILITY = 4

# Number of turns
NTURNS = 3



LIVES_LABEL_SIZE = 150

# list for star and starcraft 
starlist= []
starcraft = []


def create_initial_screen(canvas, w, h):
    """
    

    Parameters
    ----------
    canvas : TYPE
        .
    w : int
        It is our canvas width.
    h : int
        It is our canvas height.

    Returns
    -------
    screen : int
        Here this function creates the start screen.

    """
    screen = canvas.create_rectangle(0, 0, w, h)
    canvas.set_color(screen, "black")
    button = canvas.create_rectangle(w / 2 - START_BUTTON_WIDHT / 2, h / 2 - START_BUTTON_HEIGHT / 2,
                                     w / 2 + START_BUTTON_WIDHT / 2, h / 2 + START_BUTTON_HEIGHT / 2)
    canvas.set_color(button, "white")
    word = "START"
    canvas.create_text(w/2, h/2, word)
    canvas.set_font(word, "Courier", 20)
    canvas.set_color(word, "white")
    for i in range(STAR_NUMBER):
        make_star(canvas, w, h)
    return screen


def background(canvas, w, h):
    """
    creates the screen on which the game will be played
    
    """
    
    background = canvas.create_rectangle(0, 0, w, h)
    canvas.set_color(background, "black")
    return background



def make_star(canvas, w, h):
    """
    It creates stars in some screen which need those stars

    """
    x = random.randint(0, w - STAR_RADIUS)
    y = random.randint(0, h - STAR_RADIUS)
    star = canvas.create_oval(x, y, x + STAR_RADIUS, y + STAR_RADIUS)
    canvas.set_color(star, "white")
    starlist.append(star)
    
    
    
def create_enemy_starcraft(canvas, starcraft, w):
    """
    Parameters
    ----------
    
    starcraft : list
        
        Starcaft is a list and we put the meteors created in this list
        
    here this function creates meteors

    """
    x = random.randint(0, w - BALL_RADIUS)
    y = 0
    starcraft.append(canvas.create_image_with_size(x, y, BALL_RADIUS, BALL_RADIUS,"C:/Users/win10/Desktop/COD/GAMES/STAR WARS/FinalProject/son2.png"))
        
    
    
def animation_enemy_starcraft(canvas, starcraft, meteor_speed):
    """
    here this function animate all meteors in starcraft.
    """
    for craft in starcraft:
        canvas.move(craft, 0, meteor_speed)


def starfighter(canvas, w, h, choice):
    """
    

    Parameters
    ----------
    
    choice : int
        When the player click the run icon who will see three starfighter and
        will choose one. When player choose the starfighter choice take a value like 0,1,2.

    -------
    

    """
    starfighter = ["starfighter.png", "starfighter2.png", "starfighter3.png"]
    # here is the three starfighter in a list.
    # we create this all starfighter with different loop because all photos have different size.
    if choice == 0:
        paddle = canvas.create_image_with_size(w / 2 - PADDLE_WIDTH /2, h - 2 * PADDLE_Y_OFFSET - PADDLE_HEIGHT,
                                     STARFIGHTER_WIDHT, STARFIGHTER_HEIGHT , starfighter[choice])
    elif choice == 1:
        paddle = canvas.create_image_with_size(w / 2 - PADDLE_WIDTH /2, h - 2 * PADDLE_Y_OFFSET - PADDLE_HEIGHT,
                                     STARFIGHTER_WIDHT * 2, STARFIGHTER_HEIGHT , starfighter[choice])
    elif choice == 2:
        paddle = canvas.create_image_with_size(w / 2 - PADDLE_WIDTH /2, h - 3 * PADDLE_Y_OFFSET - PADDLE_HEIGHT,
                                     STARFIGHTER_WIDHT * 2 , STARFIGHTER_HEIGHT * 2, starfighter[choice])
    return paddle


def animation_starfighter(canvas, mouse_x, paddle):
    """
    Parameters
    ----------

    mouse_x : float
        Thanks to this, we know the points where the mouse is.
    paddle : int
        paddle is our startfighter.

    Returns
    -------
    This function animate the startfighter by fallow where the mouse_x is.

    """
    y = canvas.get_top_y(paddle)
    # y have to be constant because we don't want to move Y coordinate.
    canvas.moveto(paddle, mouse_x, y)
    
    
def create_rocket(canvas, rockets, paddle):
    """
    

    Parameters
    ----------
    rockets : list
    
    Here the rockets created by the starfighter are created to destroy meteorites.

    """
    color = ["red", "blue", "green", "magenta"]
    sayi = random.randint(0, 3)
    y = canvas.get_top_y(paddle)
    clicks = canvas.get_new_mouse_clicks()
    for click in clicks:
        rockets.append(canvas.create_rectangle(click.x, y - ROCKET_HEIGHT, click.x + ROCKET_WIDTH, y))
        canvas.set_color(rockets[-1], color[sayi])
        
        
def animation_rocket(canvas, rockets):
    for rocket in rockets:
        canvas.move(rocket, 0, -ROCKET_VELOCITY_Y_MAX)
        
        
def delete_enemy_spacecraft(canvas, rockets, paddle, background_x, score, score_label,screen,text,button,image_background, image_1,image_2,image_3, text_choice, sayac, w, h, lives_label, lives, level_screen, text_easy, button_easy , text_medium, button_medium, text_hard, button_hard, win_score, nturns):
    """
    

    Parameters
    ----------
    canvas : graphics.Canvas
    
    rockets : list
        Starfighter's rocket
    paddle : int
        It is our starfighter
    background_x : int
        Background of the game screen 
    score : int
        Counts how many meteors it destroyed by player
    score_label : int
        Shows how many meteors has destroyed by player
    screen : int
        Background of the screen with the start button
    text : int
        It creates start button's text
    button : int
        It is the start button
    image_background : int
        Background of the initial screen with the starfighter pictures.
    image_1 : int
    image_2 : int
    image_3 : int
        This three image name refer to photos of our starfighters.
    text_choice : int
        Creates the text that tells us to choose starfighter
    sayac : int
        To check how many lives the player has lost
    w : int
        Canvas Width
    h : int
        Canvas Height
    lives_label : int
        Shows how many lives the player has left
    lives : int
        Player's live


    """
    live = control_enemy_starcraft_location(canvas, starcraft, paddle, sayac, w, h, lives_label, lives, rockets, nturns)
    for rocket in rockets:
        ball_coords = canvas.coords(rocket)
        # This list gives us the coordinates of the vertices of the ball
        x_1 = ball_coords[0]
        y_1 = ball_coords[1]
        x_2 = ball_coords[2]
        y_2 = ball_coords[3]
        colliders = canvas.find_overlapping(x_1, y_1, x_2, y_2)
        for meteor in colliders:
            if meteor != rocket and meteor != paddle and meteor != background_x and meteor != score_label and meteor != text and meteor != button and meteor != screen and meteor != image_background and meteor != image_1 and meteor != image_2 and meteor != image_3 and meteor != text_choice and meteor != lives_label and meteor != level_screen and meteor != text_easy and meteor != button_easy and meteor != text_medium and meteor != button_medium and meteor != text_hard and meteor != button_hard and meteor not in starlist:
                # Thanks to the top we select only meteorites
                canvas.delete(meteor) 
                # When find a meteor then this code delete this meteor
                if live == 0:
                    break
                else:
                    starcraft.remove(meteor)
                    # We need to remove all destroyed meteorites from the list
                score += 1
                if score == win_score:
                    create_win_table(canvas, w, h)
                # score one increases when a meteor is deleted
            update_score_label(canvas, score_label, score)
    for rocket in rockets:
        if canvas.get_top_y(rocket) - ROCKET_HEIGHT < 0:
            rockets.remove(rocket)
            canvas.delete(rocket)
    return score




def add_score_label(canvas, score):
    """
    Score label to the top-left corner of the screen, displaying
    the initial score of 0.
    """
    label = canvas.create_text(0, 0, "")
    canvas.set_font(label, "Courier", 20)
    canvas.set_color(label, "white")
    update_score_label(canvas, label, score)
    return label


def update_score_label(canvas, score_label, score):
    """
    Updates the given score label to display the given score amount.
    """
    canvas.set_text(score_label, "Score: " + str(score))
    canvas.moveto(score_label, 0, 0)
    
    
def add_lives_label(canvas, lives):
    """
    lives label to the top-right corner of the screen, displaying
    the initial score of 3.
    """
    lives_label = canvas.create_text(CANVAS_WIDTH - LIVES_LABEL_SIZE , 0, "")
    canvas.set_font(lives_label, "Courier", 20)
    canvas.set_color(lives_label, "white")
    update_lives_label(canvas, lives_label, lives)
    return lives_label
 

def update_lives_label(canvas, lives_label, lives):
    """
    Updates the given lives label to display the given lives amount.
    """
    canvas.set_text(lives_label, "Lives: " + str(lives))
    canvas.moveto(lives_label, CANVAS_WIDTH - LIVES_LABEL_SIZE, 0)   
    
    
def control_enemy_starcraft_location(canvas, starcraft, paddle, sayac, w, h, lives_label, lives,rockets, nturns):
    """
    Here we check the positions of meteorites to check how many lives the player has left
    """
    for craft in starcraft:
        if canvas.get_top_y(craft) > canvas.get_top_y(paddle):
            sayac += 1
            lives -= 1
            update_lives_label(canvas, lives_label, lives)
            if sayac == nturns:
                create_game_over_table(canvas, w, h, rockets)
    return lives
            
            
def create_win_table(canvas, w, h):
    """
    When player's score is equals WIN_SCORE then, this function create win table.
    """
    starlist.clear()
    starcraft.clear()
    table_background = canvas.create_rectangle(0, 0, w, h)
    canvas.set_color(table_background, "black")
    sentence = "WIN!!"
    text = canvas.create_text(w/2, h/2, sentence)
    canvas.set_font(text, "Courier", 60)
    canvas.set_color(text, "white")
    sentence = "PRESS 'SPACE' FOR RESTART"
    text = canvas.create_text(w/2, h/2 + 50, sentence)
    canvas.set_font(text, "Courier", 17)
    canvas.set_color(text, "white")
    restart_game(canvas)
    canvas.update()

    
    
def create_game_over_table(canvas, w, h,rockets):
    """
    When player's lives is equals zero then, this function create game over table.
    """
    starlist.clear()
    starcraft.clear()
    table_background = canvas.create_rectangle(0, 0, w, h)
    canvas.set_color(table_background, "black")
    sentence = "GAME OVER!!!"
    text = canvas.create_text(w/2, h/2, sentence)
    canvas.set_font(text, "Courier", 30)
    canvas.set_color(text, "white")
    sentence = "PRESS 'SPACE' FOR RESTART"
    text = canvas.create_text(w/2, h/2 + 50, sentence)
    canvas.set_font(text, "Courier", 17)
    canvas.set_color(text, "white")
    restart_game(canvas)
    canvas.update()
    
def images(canvas, h, w):
    image_1 = canvas.create_image_with_size(GAP, h / 2 - GAP, IMAGE_WIDHT, IMAGE_HEIGHT, "C:/Users/win10/Desktop/COD/GAMES/STAR WARS/FinalProject/starfighter.png"  )
    image_2 = canvas.create_image_with_size(GAP * 2 + IMAGE_WIDHT, h / 2 - GAP, IMAGE_WIDHT, IMAGE_HEIGHT, "C:/Users/win10/Desktop/COD/GAMES/STAR WARS/FinalProject/starfighter2.png"  )
    image_3 = canvas.create_image_with_size(GAP * 3 + IMAGE_WIDHT * 2, h / 2 - GAP, IMAGE_WIDHT, IMAGE_HEIGHT, "C:/Users/win10/Desktop/COD/GAMES/STAR WARS/FinalProject/starfighter3.png"  )         
 
    return image_1, image_2, image_3
def restart_game(canvas):
    restartGame = 1
    while restartGame == 1:
        restart = canvas.get_new_key_presses()
        for press in restart:
            if press.keysym == "space":
                canvas.delete_all()
                restartGame = 0
                main()
            time.sleep(DELAY)
        time.sleep(DELAY)
        canvas.update()
        

def easy_medium_hard_option(canvas, w, h):
    level_screen = canvas.create_rectangle(0, 0, w, h)
    canvas.set_color(level_screen, "black")
    button_easy = canvas.create_rectangle(w / 2 - START_BUTTON_WIDHT / 2, h / 2 - START_BUTTON_HEIGHT / 2 - 50,
                                      w / 2 + START_BUTTON_WIDHT / 2, h / 2 + START_BUTTON_HEIGHT / 2 - 50)
    canvas.set_color(button_easy, "white")
    word = "EASY"
    text_easy = canvas.create_text(w/2, h / 2 - START_BUTTON_HEIGHT / 2 - 40 , word) # It creates start button's text
    canvas.set_font(word, "Courier", 20)
    canvas.set_color(word, "black")
    
    button_medium = canvas.create_rectangle(w / 2 - START_BUTTON_WIDHT / 2, h / 2 - START_BUTTON_HEIGHT / 2,
                                      w / 2 + START_BUTTON_WIDHT / 2, h / 2 + START_BUTTON_HEIGHT / 2)
    canvas.set_color(button_medium, "white")
    word_medium = "MEDIUM"
    text_medium = canvas.create_text(w/2, h/2, word_medium) # It creates start button's text
    canvas.set_font(word_medium, "Courier", 20)
    canvas.set_color(word_medium, "black")

    button_hard = canvas.create_rectangle(w / 2 - START_BUTTON_WIDHT / 2 , h / 2 - START_BUTTON_HEIGHT / 2 + 50,
                                      w / 2 + START_BUTTON_WIDHT / 2, h / 2 + START_BUTTON_HEIGHT / 2 + 50)
    canvas.set_color(button_hard, "white")
    word_hard = "HARD"
    text_hard = canvas.create_text(w/2, h / 2 + START_BUTTON_HEIGHT / 2 + 40, word_hard) # It creates start button's text
    canvas.set_font(word_hard, "Courier", 20)
    canvas.set_color(word_hard, "black")
    
    return level_screen, text_easy, button_easy , text_medium, button_medium, text_hard, button_hard


def information_about_levels(canvas, w, h):
    word = "EASY: \n Lives: 3 \n speed level: 1"
    text_easy = canvas.create_text(80, 50, word) # It creates start button's text
    canvas.set_font(text_easy, "Courier", 10)
    canvas.set_color(text_easy, "white")
    
    word_medium = "MEDIUM: \n Lives: 3 \n speed level: 2"
    text_medium = canvas.create_text(80, 100, word_medium) # It creates start button's text
    canvas.set_font(text_medium, "Courier", 10)
    canvas.set_color(text_medium, "white")
    
    word_hard = "HARD: \n Lives: 2 \n speed level: 3"
    text_hard = canvas.create_text(80, 150, word_hard) # It creates start button's text
    canvas.set_font(text_hard, "Courier", 10)
    canvas.set_color(text_hard, "white")
    
    return text_easy, text_medium, text_hard

def main():
    canvas.set_canvas_size(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Star Wars")
    sayac = 0 # To check how many lives the player has lost
    score = 0
    w = CANVAS_WIDTH
    h  = CANVAS_HEIGHT
    choice = 0
    # The part about the first screen starts here
    image_background = canvas.create_rectangle(0, 0, w, h) # Background of the initial screen with the starfighter pictures.
    canvas.set_color(image_background, "black")
    image_1, image_2, image_3 = images(canvas, h, w)
    sentence_for_choice = "CHOOSE YOUR STARFIGHTER"
    text_choice = canvas.create_text(GAP * 7, h/4, sentence_for_choice) # Creates the text that tells us to choose starfighter
    canvas.set_color(text_choice, "white")
    canvas.set_font(text_choice, "Courier", 20)
    while True:
           
        clicks = canvas.get_new_mouse_clicks()
        canvas.update()
        # Code that understands which starfighter the player has chosen
        for click in clicks:
            clicked_object = canvas.find_element_at(click.x, click.y)
            if (clicked_object == image_1 or clicked_object == image_2 or clicked_object == image_3  ) and clicked_object != text_choice:
                if clicked_object == image_1:
                    choice = 0
                elif clicked_object == image_2:
                    choice = 1
                elif clicked_object == image_3:
                    choice = 2
                # The part about the first screen ends here
                # The part about the second screen starts here
                level_screen, text_easy, button_easy , text_medium, button_medium, text_hard, button_hard = easy_medium_hard_option(canvas, w, h)
                inf_easy, inf_medium, inf_hard = information_about_levels(canvas, w, h)
                while True:
                    clicks = canvas.get_new_mouse_clicks()
                    canvas.update()
                    for click in clicks:
                        clicked_object = canvas.find_element_at(click.x, click.y)
                        if clicked_object == text_easy or clicked_object == button_easy or clicked_object == text_medium or clicked_object == button_medium or clicked_object == text_hard or button_hard:
                            if clicked_object == text_easy or clicked_object == button_easy:
                                nturns = 3
                                lives = 3
                                meteor_speed = 7
                                win_score = 100
                            elif clicked_object == text_medium or clicked_object == button_medium:
                                nturns = 3
                                lives = 3
                                meteor_speed = 11
                                win_score = 150
                            elif clicked_object == text_hard or clicked_object == button_hard:
                                nturns = 2
                                lives = 2
                                meteor_speed = 15
                                win_score = 200
                            canvas.delete(inf_easy)
                            canvas.delete(inf_medium)
                            canvas.delete(inf_hard)
                            screen = canvas.create_rectangle(0, 0, w, h) # Background of the screen with the start button
                            canvas.set_color(screen, "black")
                            button = canvas.create_rectangle(w / 2 - START_BUTTON_WIDHT / 2, h / 2 - START_BUTTON_HEIGHT / 2,
                                                              w / 2 + START_BUTTON_WIDHT / 2, h / 2 + START_BUTTON_HEIGHT / 2)
                            canvas.set_color(button, "white")
                            word = "START"
                            text = canvas.create_text(w/2, h/2, word) # It creates start button's text
                            canvas.set_font(word, "Courier", 20)
                            canvas.set_color(word, "black")
                            rockets = [] # List for rockets launched by Starfighter
                            for i in range(STAR_NUMBER):
                                make_star(canvas, w, h)
                            canvas.update()
                            time.sleep(DELAY) 
                            while True:
                                clicks = canvas.get_new_mouse_clicks()
                                canvas.update()
                                for click in clicks:
                                    clicked_object = canvas.find_element_at(click.x, click.y)
                                    if (clicked_object == button or clicked_object == text) and clicked_object != screen and click not in starlist:
                                        # Above, it is checked whether the player has pressed the start button or not.
                                        # The part about the second screen ends here
                                        # The part about the third screen starts here
                                        background_x = background(canvas, w, h) # Background of the game screen 
                                        canvas.update()
                                        paddle = starfighter(canvas, w, h, choice) # It is our starfihter
                                        canvas.update()
                                        score_label = add_score_label(canvas, score)
                                        lives_label = add_lives_label(canvas, lives)
                                        for i in range(STAR_NUMBER):
                                            make_star(canvas, w, h)
                                        canvas.update()
                                        time.sleep(DELAY)
                                    
                                        while score < win_score:
                                            mouse_x = canvas.get_mouse_x() - STARFIGHTER_WIDHT / 2
                                            possibility = random.randint(1, POSSIBILITY) # Possibility number to create rockets with a certain probability
                                            if possibility == 1:
                                                create_enemy_starcraft(canvas, starcraft, w)
                                            animation_enemy_starcraft(canvas, starcraft, meteor_speed)
                                            if mouse_x > 0 and mouse_x < canvas.get_canvas_width() - PADDLE_WIDTH:
                                                animation_starfighter(canvas, mouse_x, paddle)
                                            create_rocket(canvas, rockets, paddle)
                                            animation_rocket(canvas, rockets)
                                            score = delete_enemy_spacecraft(canvas, rockets, paddle, background_x, score, score_label,screen,text,button,image_background, image_1,image_2,image_3, text_choice, sayac, w, h, lives_label, lives, level_screen, text_easy, button_easy , text_medium, button_medium, text_hard, button_hard, win_score, nturns)
                                            
                                            control_enemy_starcraft_location(canvas, starcraft, paddle, sayac, w, h, lives_label, lives, rockets, nturns)
                                            canvas.update()
                                            time.sleep(DELAY)
                                
                                
    
                         
      
if __name__ == '__main__':
    main()