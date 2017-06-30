import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

#Pygame variables
pygame.init()
windowWidth = 800
windowHeight = 500

surface = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("Pygame Keyboard!")

#Square variables
playerSize = 20
playerX = (windowWidth / 2) - (playerSize / 2)
playerY = windowHeight - playerSize
playerVX = 1.0
playerVY = 0.0
jumpHeight = 25.0
moveSpeed = 1.0
maxSpeed = 10.0
gravity = 1.0

#keyboard variables
leftDown = False
rightDown = False
haveJumped = False

def move():
	global playerX, playerY, playerVX, playerVY, haveJumped, gravity

	#move left
	if leftDown:
		#If we're already moving to the right,
		#reset the moving speed and invert the direction
		if playerVX > 0.0:
			playerVX = moveSpeed
			playerVX = -playerVX
		#Make sure our square doesn't leave our window
		#to the left.
		if playerX > 0:
			playerX += playerVX
	#move right
	if rightDown:
		#If we're already moving to the left, reset
		#the moving speed again
		if playerVX < 0.0:
			playerVX = moveSpeed
		#Make sure that our square doesn't leave
		#our window to the right
		if playerX + playerSize < windowWidth:
			playerX += playerVX

	if playerVY > 1.0:
		playerVY = playerVY * 0.9
	else:
		playerVY = 0.0
		haveJumped = False

	#Is our square in the air? 
	#Better add some gravity to bring it back to the ground
	if playerY < windowHeight - playerSize:
		playerY += gravity
		gravity = gravity * 1.1
	else:
		playerY = windowHeight - playerSize
		gravity = 1.0
	
	playerY -= playerVY

	if (playerVX > 0.0 and playerVX < maxSpeed) or (playerVX < 0.0 and playerVX > -maxSpeed):
		if not haveJumped and(leftDown or rightDown):
			playerVX = playerVX * 1.1

def quitGame():
	pygame.quit()
	sys.exit()

while True:
	surface.fill((0,0,0))

	pygame.draw.rect(surface,(255,0,0), (playerX, playerY, playerSize, playerSize))

	#Get a list of all events that happened
	#since the last draw
	for event in GAME_EVENTS.get():

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LEFT:
				leftDown = True
			if event.key == pygame.K_RIGHT:
				rightDown = True
			if event.key == pygame.K_UP:
				if not haveJumped:
					haveJumped = True
					playerVY += jumpHeight

			if event.key == pygame.K_ESCAPE:
				quitGame()

		if event.type == pygame.KEYUP:
			if event.key ==pygame.K_LEFT:
				leftDown = False
				playerVX = moveSpeed
			if event.key == pygame.K_RIGHT:
				rightDown = False
				playerVX = moveSpeed
		if event.type == GAME_GLOBALS.QUIT:
			quitGame()

	move()
	#Limit the frame rate on sys faster than RPis
	#clock.tick(60)
	pygame.display.update()
