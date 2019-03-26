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
        direction = 0

        player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
        enemy_0 = EnemyCharacter('enemy.png', 20, 600, 50, 50)
        treasure = GameObject('treasure.png', 375, 50, 50, 50)

        # main game loop, used to update all gameplay such as movement, checks, graphics
        # runs until is_game_over = True
        while not is_game_over:

            # loop to get all of the events occuring at any given time
            # events are most often moue movement, mouse/button clicks, or exit events
            for event in pygame.event.get():
                # if we have a quite type event (exit out) then exit out of the game loop
                if event.type == pygame.QUIT:
                    is_game_over = True
                # detect when key is pressed down
                elif event.type == pygame.KEYDOWN:
                    # move up if up key pressed
                    if event.key == pygame.K_UP:
                        direction = 1
                    # move down if key pressed
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # detect when key is released
                elif event.type == pygame.KEYUP:
                    # stop movement when key no longer pressed
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
            print(event)

            # redraw the screen to be blank
            self.game_screen.fill(WHITE_COLOR)

            treasure.draw(self.game_screen)
            
            # update the player position
            player_character.move(direction, self.height)
            # draw the player at the new position
            player_character.draw(self.game_screen)

            # Move and draw the enemy character
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)


            # end game if collision between enemy and treasure
            if player_character.detect_collision(enemy_0):
                is_game_over = True
            elif player_character.detect_collision(treasure):
                is_game_over = True
                

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

# Pygame pt 5
# Implement game classes
# Implement generic game object class

class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        # scale the image up
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

# Pygame Pt 6
# Implement game classes
# Implement player character class and movement

# Class to represent the character controlled by the player
class PlayerCharacter(GameObject):

    # How many tiles the character moves per second
    SPEED = 10

    # Move function will move character up if direction > 0 and down if < 0
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function will move character up if direction > 0 and down if < 0
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        # Make sure the character never goes past the bottom of the screen
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40

# Pygame pt 8
# implement collision detection
# detect collisions with treasure and enemies
            

    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
            
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False
            
        return True



# Pygame pt 7
# Implement game classes
# Implement enemy character class and bounds checking


# Class to represent the enemy controlled by the player
class EnemyCharacter(GameObject):

    # How many tiles the enemy moves per second
    SPEED = 10

    # Move function will move enemy right once it hits the side of screen
    # then it moves left until it hits the other side
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # automating movement, controlling by checking location
    # Bounds checking, basically...
    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width -40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


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

# add new content by making a branch on Git, then upload file, then pull/merge

# edit on ATOM - try to save as branch - see what happens
