from processing import *

import random

SCREEN_WIDTH  = 400
SCREEN_HEIGHT = 400
COLORS = [
	(255, 0, 0),   #RED
	(0, 255, 0),   #GREEN
	(0, 0, 255),   #BLUE
	(255, 255, 0), #YELLOW
	(255, 0, 255), #MAGENTA
	(0, 255, 255)  #CYAN
]

class Square:
  def __init__(self, x=0, y=0, size=0):
    self.x = x
    self.y = y
    self.size = size
    self.randomize_color()
  
  def __eq__(self, other):
    return self.color == other.color

  def draw(self):
    fill(*self.color)
    rect(self.x * self.size, self.y * self.size, self.size, self.size)
  
  def randomize_color(self):
    self.color = random.choice(COLORS)

def flood_fill(grid, x, y, value, replace):
  if (x < 0 or x >= len(grid[0]) or
      y < 0 or y >= len(grid) or
      grid[y][x].color != replace or
      grid[y][x] == value):
    return
  
  grid[y][x].color = value.color

  flood_fill(grid, x + 1, y, value, replace)
  flood_fill(grid, x - 1, y, value, replace)
  flood_fill(grid, x, y + 1, value, replace)
  flood_fill(grid, x, y - 1, value, replace)

def setup():
  global grid
  size(SCREEN_WIDTH, SCREEN_HEIGHT)
  noStroke()
  grid = [[Square(x, y, 20) for x in range(SCREEN_WIDTH // 20)] for y in range(SCREEN_HEIGHT // 20)]

def draw():
  global grid
  background(255)
  for row in grid:
    for square in row:
      square.draw()

def mouseClicked():
  global grid
  x = mouseX // 20
  y = mouseY // 20
  to_replace = grid[y][x].color
  flood_fill(grid, x, y, Square(), to_replace)
