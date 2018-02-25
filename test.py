import pygame
import OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

print "imported"

class Cube:
	def __init__(self):
		self.vertices = [(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,1),(1,1,1),(-1,-1,1),(-1,1,1)] # coord
		self.edges = [(0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7)] # fusion two position of vertices tuple
		self.colors = [(1,0,0),(1,1,0),(1,0,1),(0.5,0.1,0),(0,1,1),(1,1,1)]
		self.surface = [(0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)]
	def set_color(self):
		glBegin(GL_QUADS)
		for my_surface in self.surface:
			x = 0
			for vertex in my_surface:
				x += 1
				glColor3fv(self.colors[x])
				glVertex3fv(self.vertices[vertex])

		glEnd()
	def draw(self):
		self.set_color()

		glBegin(GL_LINES) # notifies GL that it will be a line-drawing code
		for my_edge in self.edges:
			for vertex in my_edge:
				glVertex3fv(self.vertices[vertex]) # ex: glVertex3fv((1,-1,-1)), glVertex3fv((1,1,-1)),...
		glEnd()
	"""def move(self,x,y,z):
		for point in range(len(self.vertices)):
			coord = self.vertices[point]
			new_coord = (coord[0] + x, coord[1] + y, coord[2] + z)
			self.vertices[point] = new_coord"""
	def move(self,x,y,z):
		glTranslatef(x,y,z)

	def check(self,direction,rotate):
		if direction == "left":
			self.move(-0.01,0,0)
		if direction == "right":
			self.move(0.01,0,0)
		if direction == "up":
			self.move(0,0.01,0)
		if direction == "down":
			self.move(0,-0.01,0)

		if rotate == "right":
			glRotate(1,0,1,0)
		if rotate == "left":
			glRotate(1,0,-1,0)
		if rotate == "up":
			glRotate(1,-1,0,0)
		if rotate == "down":
			glRotate(1,1,0,0)

def main():
	pygame.init() # initialize pygame
	display = (800,600) # res
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL) # notifie pygame that we will add opengl into as well as double buffer
	gluPerspective(45,(display[0]/display[1]),0.1,50.0) # gluPerspective(angle, ratio, znear, zfar)
	glTranslatef(0.0,0.0,-5) # move the you (the camera)
	my_cube = Cube()

	my_dir = False
	my_angle = False
	print "finished to setting up"

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == KEYDOWN:
				if event.key == K_a:
					my_dir = "left"
				if event.key == K_d:
					my_dir = "right"
				if event.key == K_s:
					my_dir = "down"
				if event.key == K_w:
					my_dir = "up"

				if event.key == K_LEFT:
					my_angle = "left"
				if event.key == K_RIGHT:
					my_angle = "right"
				if event.key == K_DOWN:
					my_angle = "down"
				if event.key == K_UP:
					my_angle = "up"
			if event.type == KEYUP:
				if event.key in [K_a,K_d,K_s,K_w]:
					my_dir = False
				if event.key in[K_UP,K_DOWN,K_LEFT,K_RIGHT]:
					my_angle = False

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # clear stuff
		my_cube.check(my_dir,my_angle)
		my_cube.draw()
		pygame.display.flip() # update gui

main()	
