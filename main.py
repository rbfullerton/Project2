import pygame
from sys import exit
from random import choice
import Player as Player
import Obstacle as Obstacle
# Displays current score
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

# detects any colision with an ememy
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

# initalizes game and start up screen
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Cave In!')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.mp3')
bg_music.play(loops=-1)

player = pygame.sprite.GroupSingle()

# calls player file
player.add(Player.Player())

obstacle_group = pygame.sprite.Group()
back_surface = pygame.image.load('graphics/Back.png').convert()

ground_surface = pygame.image.load('graphics/ground.png').convert()

# start screen and player sprite
player_stand = pygame.image.load('graphics/player/player_stand1.png').convert_alpha()

player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Cave In!', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press space to Begin!', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 330))

# Timer/score
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# starts up game / random enemy encounters
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle.Obstacle(choice(['bat', 'hand', 'hand', 'hand'])))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(back_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(game_name, game_name_rect)

        score_high = test_font.render(f'High Score is: {score}', False, (111, 196, 169))
        score_high_rect = score_high.get_rect(center=(600, 330))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(100)