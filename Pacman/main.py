import pygame
from game import Game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

def main():
    # Initialize all imported pygame modules
    pygame.init()
    # Set the width and height of the screen [width, height]
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # Set the current window caption
    pygame.display.set_caption("PACMAN")
    #Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Create a game object
    game = Game()
