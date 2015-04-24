#!/usr/bin/env python

import math, os

class context:

  def __init__(self,x,y):
    """
    Initializes a work area
    """

    self.grid=[[" " for i in range(x)] for i in range(y)]
    self.xsize=x
    self.ysize=y

  def clear(self):
    """
    Clears the area
    """

    self.grid=[[" " for i in range(self.xsize)] for i in range(self.ysize)]

  def draw(self):
    """
    Prints the area in console
    """

    os.system('clear')
    for i in self.grid: print "".join(i)

  def line(self,x0,y0,x1,y1,char):
    """
    Stole this shit from wikipedia

    https://en.wikipedia.org/wiki/Bresenham's_line_algorithm#Line_equation
    """

    sign=lambda x: cmp(x,0)
    deltax=x1-x0
    deltay=y1-y0
    error=0
    try:
      deltaerr=abs(deltay/deltax)  #Assume deltax != 0 (line is not vertical),
      y=y0
      for x in range(x0,x1+1):
        self.grid[y][x]=char
        error+=deltaerr
        while error>=0.5:
          self.grid[y][x]=char
          y+=sign(y1-y0)
          error-=1
    except ZeroDivisionError:
      for i in range(abs(deltay)): self.grid[y0+(i*sign(y1-y0))][x0]=char

  def putpixel(self,x,y,char):
    self.grid[y][x]=char

  def rectangle(self,x,y,xsize,ysize,char):

    self.line(x,y,x+xsize,y,char)
    self.line(x,y,x,y+ysize,char)
    self.line(x+xsize,y,x+xsize,y+ysize,char)
    self.line(x,y+ysize,x+ysize,y+ysize,char)

if __name__=="__main__":
  pass