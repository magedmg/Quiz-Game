import pygame
import random
import time

print('')
print('')
print("Welcome to Maged's higher or lower game, the objective is to get 800 points or ")
time.sleep(3)
print("more to win. Each question you get right you will get 100 points, but the longeryou take to answer,the less points you'll get.")
time.sleep(2)
print('')
print('GLHF')
time.sleep(2)


pygame.init()
pygame.mixer.init()
#MUSIC WAS EARRAPE AND SO I CHANGED THE VOLUME OF ALL THE MUSIC PLAYING INSIDE PYGAME
pygame.mixer.music.set_volume(0.1)

# dictionary for the game with peoples names on the left, and their amount of followers on the right
popularity = {
    "Miss Hocking": 99999999999999999999999999999,
    "XQC": 5500000,
    "Pewdiepie": 120000000,
    "Among Us": 100000000,
    "Maged": 1,
    "Fortnite": 250000000,
    "Valorant": 70000000,
    "John Cena": 16187915,
    'The Rock': 200000000,
    'Cardi B': 108938709,
    'Mr Beast': 30000000,
    'Kylie Jenner': 202000000
}

# button positions
button_positions = [[300, 320], [600, 320]]

class Text():
    def __init__(self, text):
        self.x = 0
        self.y = 0
        self.size = 20
        self.colour = WHITE
        self.font = pygame.font.SysFont("Ubuntu", self.size)
        self.text = text
        self.textsurface = self.font.render(self.text, True, self.colour)
    def draw(self, screen):
        screen.blit(self.textsurface, (self.x, self.y))
    def update_text(self, text):
        self.text = text
        self.textsurface = self.font.render(self.text, True, self.colour)
    def update_colour(self, colour):
        self.colour = colour
        self.textsurface = self.font.render(self.text, True, self.colour)
    def update_size(self, size):
        self.size = size
        self.font = pygame.font.SysFont("Ubuntu", self.size)
        self.textsurface = self.font.render(self.text, True, self.colour)        
#buttons
button_path="C:/Users/maged/OneDrive/Documents/Coding/Python/button.png"
class Button():
    
    def __init__(self, text, x, y, option):
        self.x = x
        self.y = y
        self.height = 75
        self.width = 150
        self.text = text
        self.text_draw = Text(self.text)
        self.text_draw.update_colour(RED)
        # text position relative to the button
        self.text_draw.x = self.x + self.width/10
        self.text_draw.y = self.y + self.height/2 - self.text_draw.size/2
        self.image = pygame.transform.scale(pygame.image.load(button_path), (self.width, self.height))

        # offset the text x and y to make it on the button
        self.option = option
    def draw(self, screen):
        # button image
        screen.blit(self.image, (self.x, self.y))
        # text
        self.text_draw.draw(screen)
    def pressed_on(self, x, y):
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            # if the x and y coordinates of the mouse click are within the boundaries of the button
            return True

class Question():
    def __init__(self, text, option_1, option_2):
        global button_positions
        global popularity
        self.question = text
        self.question_draw = Text(self.question)
        # updating look and position of the text
        self.question_draw.update_colour(WHITE)
        self.question_draw.update_size(50)
        self.question_draw.x = 325
        self.question_draw.y = 200
        self.correct_option = 0
        if popularity[option_1] > popularity[option_2]:
            self.correct_option = 1
        else:
            self.correct_option = 2
        self.points_awarded = 100
        self.options_buttons = []
        # creates both buttons and notes their locations
        self.options_buttons.append(Button(option_1, button_positions[0][0], button_positions[0][1], 1))
        self.options_buttons.append(Button(option_2, button_positions[1][0], button_positions[1][1], 2))
        
    def draw(self, screen):
        # question
        self.question_draw.draw(screen)
        # buttons
        for button in self.options_buttons:
            button.draw(screen)
        
##### Colours #####
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)

##### Screen Initialisation #####
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Higher Or Lower Game")
image_path = "C:/Users/maged/OneDrive/Documents/Coding/Python/tv2.png"
background_image = pygame.transform.scale(pygame.image.load(image_path),(SCREEN_WIDTH, SCREEN_HEIGHT))

done = False              
clock = pygame.time.Clock()
'''test question'''
# parameters are the question text, the possible options, and the correct option
# eg. XQC, Joe
new_question = True
option_1 = random.choice(list(popularity.items()))[0]
while 1:
    option_2 = random.choice(list(popularity.items()))[0]
    if option_2 != option_1:
        break
question = Question("Who is more popular:", option_1, option_2)
'''timer'''
pygame.time.set_timer(pygame.USEREVENT, 1000)
'''score'''
total_score = 0
score_text = Text("Score: " + str(total_score))
score_text.x = 400
'''text'''
winner_text = Text("")
winner_text.y = SCREEN_HEIGHT/2 - 25
winner_text.x = SCREEN_WIDTH/2 - 100
loser_text = Text("wrong! no points awarded")
loser_text.y = SCREEN_HEIGHT/2
loser_text.x = SCREEN_WIDTH/2 - 100
# 0 = not answered yet 1 = won, 2 = lost
question_won = 0
'''win/lose'''
questions_left = 10
questions_left_text = Text("Questions left: " + str(questions_left))
questions_left_text.x = 500
score_needed = 800
winner_end_text = Text("You win! You got over " + str(score_needed) + " points within " + str(questions_left) + " questions!")
winner_end_text.update_colour(WHITE)
winner_end_text.update_size(30)
winner_end_text.x = 150
winner_end_text.y = SCREEN_HEIGHT/2
lose_end_text = Text("You lose! You did not get over " + str(score_needed) + " points within " + str(questions_left) + " questions!")
lose_end_text.update_colour(BLACK)
lose_end_text.update_size(30)
lose_end_text.x = 150
lose_end_text.y = SCREEN_HEIGHT/2 + 100
final_score = Text("")
final_score.update_colour(WHITE)
final_score.update_size(30)
final_score.x = SCREEN_WIDTH/2 - 100
final_score.y = SCREEN_HEIGHT/2 + 50
lost_change_music = True
'''music'''
pygame.mixer.music.load("MUSIC.ogg")
pygame.mixer.music.play(-1)
##### Main Program Loop #####
while not done:
    ##### Events Loop #####
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.USEREVENT:
            if question.points_awarded > 70:
                question.points_awarded -= 1
        elif event.type == pygame.USEREVENT + 1:
            question_won = 0
        elif event.type == pygame.USEREVENT + 2:
            print("L")
            pygame.mixer.music.load("loser.ogg")
            pygame.mixer.music.play(-1)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and questions_left > 0:
                # if the primary mouse button is clicked
                mouse_coordinates = pygame.mouse.get_pos()
                for button in question.options_buttons:
                    # button will check if it has been clicked
                    if button.pressed_on(mouse_coordinates[0], mouse_coordinates[1]) == True:
                        questions_left -= 1
                        if question.correct_option == button.option:
                            question_won = 1
                            total_score += question.points_awarded
                            score_text.update_text("Score: " + str(total_score))
                            winner_text.update_text("correct! + " + str(question.points_awarded) + " points!")
                            final_score.update_text("Final Score: " + str(total_score))
                        else:
                            question_won = 2
                        questions_left_text.update_text("Questions left: " + str(questions_left))
                        # updating question
                        option_1 = random.choice(list(popularity.items()))[0]
                        while 1:
                            option_2 = random.choice(list(popularity.items()))[0]
                            if option_2 != option_1:
                                break
                        question = Question("Who is more popular:", option_1, option_2)

    ##### Game logic #####
    
    ##### Drawing code #####
    screen.fill(BLACK)
    screen.blit(background_image,[0,0])
    if questions_left > 0:
        question.draw(screen)
        if question_won == 1:
            winner_text.draw(screen)
            pygame.time.set_timer(pygame.USEREVENT + 1, 500, True)
        elif question_won == 2:
            loser_text.draw(screen)
            pygame.time.set_timer(pygame.USEREVENT + 1, 500, True)
        score_text.draw(screen)
        questions_left_text.draw(screen)
    else:
        # win
        if total_score > score_needed:
            winner_end_text.draw(screen)
            final_score.draw(screen)
        else:
        # lose
            background_image = pygame.transform.scale(pygame.image.load("loser.png"),(SCREEN_WIDTH, SCREEN_HEIGHT))
            lose_end_text.draw(screen)
            final_score.update_colour(BLACK)
            final_score.y = SCREEN_HEIGHT/2 + 175
            final_score.draw(screen)
            # change music
            if lost_change_music:
                pygame.time.set_timer(pygame.USEREVENT + 2, 10, True)
                lost_change_music = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
#the end
