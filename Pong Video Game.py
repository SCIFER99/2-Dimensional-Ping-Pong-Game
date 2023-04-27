# By: Tim Tarver (CryptoKeyPlayer)
# Pong Video Game Development

import pygame
import random
import sys
from pygame.locals import *

# Initiate the game

pygame.init()

# Create parameters for the game

frame_per_seconds = pygame.time.Clock()
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Global Variable Definitions

width = 600
height = 400
ball_radius = 20
pad_width = 8
pad_height = 80
half_pad_width = pad_width // 2
half_pad_height = pad_height // 2
paddle1_position1 = 0
paddle2_position2 = 0
ball_position = 0 
ball_velocity = 0
paddle1_velocity = 0
paddle2_velocity = 0



window = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("2Dimensional PING-PONG Game")

# Creates the functionality of the Ball

def ball_init(right):

    global ball_position, ball_velocity
    
    ball_position = [width // 2, height // 2]
    horizontal_motion = random.randrange(2, 4)
    vertical_motion = random.randrange(1, 3)

    if right == False:
        horizontal_motion =- horizontal_motion
        
    ball_velocity = [horizontal_motion, -vertical_motion]

# Draw a Canvas the game will be played on and
# create the motion portraits of the ball & paddles.

def draw(canvas):

    global paddle1_position1, paddle2_position2
    global ball_position, ball_velocity
    global left_score1, right_score1

    canvas.fill(black)
    pygame.draw.line(canvas, white, [width // 2, 0], [width // 2, height], 1)
    pygame.draw.line(canvas, white, [pad_width, 0], [pad_width, height], 1)
    pygame.draw.line(canvas, white, [width-pad_width, 0], [width-pad_width, height], 1)
    pygame.draw.circle(canvas, white, [width // 2, height // 2], 70, 1)

    # Motion of the Left Paddle

    if (paddle1_position1 > half_pad_height) and (paddle1_position1 < height-half_pad_height):
        paddle1_position1 += paddle1_velocity
    elif paddle1_position1 == half_pad_height and paddle1_velocity > 0:
        paddle1_position1 += paddle1_velocity
    elif paddle1_position1 == height - half_pad_height and paddle1_velocity < 0:
        paddle1_position1 += paddle1_velocity

    # Motion of the Right Paddle

    if paddle2_position2 > half_pad_height and paddle2_position2 < height-half_pad_height:
        paddle2_position2 += paddle2_velocity
    elif paddle2_position2 == half_pad_height and paddle2_velocity > 0:
        paddle2_position2 += paddle2_velocity
    elif paddle2_position2 == height - half_pad_height and paddle2_velocity < 0:
        paddle2_position2 += paddle2_velocity

    # Ball positioning
    
    ball_position += ball_velocity
    ball_position += ball_velocity

    # Draw Paddle 1

    pygame.draw.circle(canvas, red, (ball_velocity, ball_velocity), 20, 0)
    pygame.draw.polygon(canvas, green, [[paddle1_position1-half_pad_width,
                                         paddle1_position1-half_pad_height],
                                        [paddle1_position1-half_pad_width,
                                         paddle1_position1+half_pad_height],
                                        [paddle1_position1+half_pad_width,
                                         paddle1_position1-half_pad_height]], 0)
        
    # Draw Paddle 2

    pygame.draw.circle(canvas, red, (ball_velocity, ball_velocity), 20, 0)
    pygame.draw.polygon(canvas, green, [[paddle2_position2-half_pad_width,
                                         paddle2_position2-half_pad_height],
                                        [paddle2_position2-half_pad_width,
                                         paddle2_position2+half_pad_height],
                                        [paddle2_position2+half_pad_width,
                                         paddle2_position2-half_pad_height]], 0)

    # Detect the Ball Collision on both Paddles

    if ball_position <= ball_radius:
        ball_velocity = -ball_velocity

    if ball_position >= height + 1 - ball_radius:
        ball_velocity = -ball_velocity

    # Left Paddle motion    

    if ball_position <= ball_radius + pad_width and\
       ball_position in range(paddle1_position1-half_pad_height, paddle1_position1+half_pad_height, 1):
        ball_velocity = -ball_velocity
        ball_velocity *= 1.1
        ball_velocity *= 1.1

    elif ball_position <= ball_radius+pad_width:
        right_score += 1
        ball_init(True)

    # Right Paddle motion

    if ball_position >= width + 1 - ball_radius - pad_width and\
       ball_position in range(paddle2_position2 - half_pad_height,
                                      paddle2_position2 + half_pad_height, 1):
        ball_velocity = -ball_velocity
        ball_velocity *= 1.1
        ball_velocity *= 1.1

    elif ball_position >= width + 1 - ball_radius - pad_width:
        left_score += 1
        ball_init(False)

    # Create font for keeping score
    
    left_score = 0
    my_font = pygame.font.SysFont("Comic Sans  MS", 20)
    label = my_font.render("Score" + str(left_score), 0, (255, 255, 0))
    canvas.blit(label, (50, 50))
    
    right_score = 0
    my_font2 = pygame.font.SysFont("Comic Sans MS", 20)
    label2 = my_font2.render("Score" + str(right_score), 1, (255, 255, 0))
    canvas.blit(label2, (470, 20))

# Event Programming of the Paddles

def keydown(event):

    global paddle2_vel, paddle1_vel
    
    if event.key == K_UP:
        paddle2_vel = -8
    elif event.key == K_DOWN:
        paddle2_vel = 8
    elif event.key == K_w:
        paddle1_vel = -8
    elif event.key == K_s:
        paddle1_vel = 8

def keyup(event):

    global paddle1_vel1, paddle2_vel2

    if event.key in (K_w, K_s):
        paddle1_vel1 = 0
    elif event.key in (K_UP, K_DOWN):
        paddle2_vel2 = 0

# Initialize Positions for Paddles and Scoreboards 

def init():

    global paddle1_position1, paddle2_position2
    global paddle1_velocity, paddle2_velocity
    global left_score, right_score
    global score1, score2

    paddle1_position1 = [half_pad_width - 1, height // 2] # [3, 200]
    paddle2_position2 = [width + 1 - half_pad_width, height // 2] # [299, 200]
    left_score = 0
    right_score = 0
    
    if random.randrange(0, 2) == 0:
        ball_init(True)
    else:
        ball_init(False)

while True:
    
    draw(window)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    frame_per_seconds.tick(60)

    
