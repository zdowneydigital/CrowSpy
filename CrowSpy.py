# Pygame
# setting up the display

import pygame

# pt 4 below


# add title to top of game screen
SCREEN_TITLE = 'Crow Spy'
# size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# colors according to RGB codes
WHITE_COLOR = (197, 222, 232)
BLACK_COLOR = (0, 0, 0)
# clock used to update game events and frames
clock = pygame.time.Clock()

class Game:

    # typical rate of 60, equivalent to FPS
    TICK_RATE = 60


    # Initializer for the game class to set up the width, height, and title
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # create the window of specified size in white to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        #set the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        # this next line is what actually puts the screen-title in the window (at top)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False

        # main game loop, used to update all gameplay such as movement, checks, graphics
        # runs until is_game_over = True
        while not is_game_over:

            # loop to get all of the events occuring at any given time
            # events are most often moue movement, mouse/button clicks, or exit events
            for event in pygame.event.get():

                # if we have a quite type event (exit out) then exit out of the game loop
                if event.type == pygame.QUIT:
                    is_game_over = True
                print(event)

            # draw a rectangle on top of the game screen canvas (x, y, width, height)
            # commenting line below out
            # pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
            # commenting line below out
            # draw a circle on top of the game screen (x, y, radius)
            # commenting line below out
            # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

            # more of pt 3 here:
            # draw the player image on top of the screen at (x, y) position
            # PT 4 COMMENTED OUT game_screen.blit(player_image, (375, 375))


            # update all game graphics
            pygame.display.update()

            # tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)
        
# adding next line in part 2 of tutorial
pygame.init()

# pt 4 below

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()


# more of part 2 below here

# load the player image from the file directory
# PT 4 COMMENTED OUT player_image = pygame.image.load('player.png')
# scale the image up
# PT 4 COMMENTED OUT player_image = pygame.transform.scale(player_image, (50, 50))

# Testing out branches on GitHub here

# online edit test - will it appear locally?

# yes, online edits are now showing up in local version after Fetch Origin function in GitHub Explorer

# one more test to see if this is working the way I expect

# now trying to use ATOM as a text editor - check to see if all versions update

# yes - a change in ATOM updated in the local file after Git & Atom logged out

# online edit again - save as 'new branch' and see how it appears in Git Explorer

# and now yet another test - this with Atom again

# back to the Zenva tutorial - additions below

# in a minute, that is - now making edit to master on Git - see if can show locally, then in Atom

# quick edit in Atom - being used instead of IDLE on local machine - how easily will it save?

# Pygame pt 2

# Set up game loop to render graphics

# added clock, tick-rate, is-game-over variable above, but continuing below...



# quit pygame and the program
pygame.quit()
quit()

# Pygame pt 3

# draw object to the screen

# load images into objects

# adding this code up above, actually - just below the print(event) line

# still trying to get Git & Atom to work properly

# Pygame pt 4 - like pt. 3, code being added above

# making code object oriented by introducing classes and objects
