# Pygame
# setting up the display

import pygame

# adding next line in part 2 of tutorial
pygame.init()

# size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# add title to top of game screen
SCREEN_TITLE = 'Crow Spy'
# colors according to RGB codes
WHITE_COLOR = (197, 222, 232)
BLACK_COLOR = (0, 0, 0)
# clock used to update game events and frames
clock = pygame.time.Clock()
# typical rate of 60, equivalent to FPS
TICK_RATE = 60
is_game_over = False


# create the window of specified size in white to display the game
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#set the game window color to white
game_screen.fill(WHITE_COLOR)
# this next line is what actually puts the screen-title in the window (at top)
pygame.display.set_caption(SCREEN_TITLE)


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

    # update all game graphics
    pygame.display.update()

    # tick the clock to update everything within the game
    clock.tick(TICK_RATE)

# quit pygame and the program
pygame.quit()
quit()


