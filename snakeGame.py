# Snake Game!
# by Parv Jain

# our game imports
import pygame 
import sys
import random
import time

# initialize pygame
# check for imitilizing errors
check_errors = pygame.init()
# init() output format (6,0) i.e. (success,errors) 
if check_errors[1] > 0:
	print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
	sys.exit(-1)
else:
	print("(+) PyGame successfully initialized!")


# Play surface - to create window to play
playSurface = pygame.display.set_mode((720, 460))

# To change title of window (playSurface)
pygame.display.set_caption('Snake game!')

# time.sleep(5)

# Colors
red = pygame.Color(255, 0, 0) # game over
green = pygame.Color(0, 255, 0) # snake
black = pygame.Color(0, 0, 0) # score
white = pygame.Color(255, 255, 255) # background
brown = pygame.Color(165, 42, 42) # food

# FPS controller
fpsController = pygame.time.Clock()

# Important variables
snakePos = [100,50] # coordinates of snake head at start of game
snakeBody = [[100,50], [90,50], [80,50]] # initial snake body coordinates at start of game

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

score = 0

# Game over function
def gameOver():
	# define font type and size
	myFont = pygame.font.SysFont('monaco', 72)
	# define Game Over Surface render text onto it i.e render(text, antialiasing, color)
	GOsurf = myFont.render('Game over!', True, red)
	# define Game Over rectangle containing Game Over Surface
	GOrect = GOsurf.get_rect()
	# position for display a rectangle containing Game Over Surface
	GOrect.midtop = (360, 15)
	# display Game Over Surface on Play Surface
	playSurface.blit(GOsurf,GOrect)
	# show score in middle after game over
	showScore(0)
	# to refresh frame so that message is displayed (update display screen)
	pygame.display.flip()
	# exit after 4 second
	time.sleep(4)
	pygame.quit() #pygame exit
	sys.exit() #console exit

def showScore(choice = 1):
	sFont = pygame.font.SysFont('monaco', 24)
	Ssurf = sFont.render('Score: {0}'.format(score), True, black)
	Srect = Ssurf.get_rect()
	if choice == 1:
		Srect.midtop = (80, 10)
	else:
		Srect.midtop = (360,120)
	playSurface.blit(Ssurf,Srect)
	
# events are special occassion where something actually happens
# whenever user hit a button on keyboard it's like invoking three main events: 
# 1. hit 
# 2. sustain period- how long user hold that button
# 3. release time period- taking away user hand out of button

# Main logic of the game
while True:
	# pygame.event.get() returns list of all events that are inside pygame event
	for event in pygame.event.get():	
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				changeto = 'LEFT'
			if event.key == pygame.K_UP or event.key == ord('w'):
				changeto = 'UP'
			if event.key == pygame.K_DOWN or event.key == ord('s'):
				changeto = 'DOWN'
			if event.key == pygame.K_ESCAPE:
				# post(EventType) is used to create event in pygame
				pygame.event.post(pygame.event.Event(pygame.QUIT))

	# validation of direction
	if changeto == 'RIGHT' and not direction == 'LEFT':
		direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'
	if changeto == 'UP' and not direction == 'DOWN':
		direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP':
		direction = 'DOWN'

	# update snake position [x,y]	
	if direction == 'RIGHT':
		snakePos[0] += 10
	if direction == 'LEFT':
		snakePos[0] -= 10
	if direction == 'UP':
		snakePos[1] -= 10
	if direction == 'DOWN':
		snakePos[1] += 10

	# snake body mechanism
	# insert function of list to add coordinates of current snakePos to snakeBody
	snakeBody.insert(0, list(snakePos))
	if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
		# food is eaten
		score += 1
		foodSpawn = False
	else:
		# pop from snakeBody as snake is moved without eating a food
		snakeBody.pop()

	#Food Spawn
	if foodSpawn == False:
		# if food is eaten place food at new random position
		foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
	foodSpawn = True

	# fill background (playSurface) with white color
	playSurface.fill(white)
	
	# Draw snake
	for pos in snakeBody:
		# pygame.Rect(x,y,sizex,sizey)
		pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1],10,10))

	# Draw food
	pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))

	# Check for boundaries
	if snakePos[0] > 710 or snakePos[0] < 0:
		gameOver()
	if snakePos[1] > 450 or snakePos[1] < 0:
		gameOver()

	# Check if any of block in Body of snake hit by snake head
	for block in snakeBody[1:]:
		if snakePos[0] == block[0] and snakePos[1] == block[1]:
			gameOver()

	# showScore
	showScore()
	
	# update display
	pygame.display.flip() # can also use pygame.display.update() to update display changes
	# set frames per seconds
	fpsController.tick(20)

# improvements
# Adding menu (settings, help, resume, pause, play)
# Adding sounds, images to food body
# Change icon of game
# pyinstaller to create executables instead of script