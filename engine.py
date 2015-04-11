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

  def line(self,x1,y1,x2,y2,char):
    """
    Draws a line from (x1,y1) to (x2,y2)
    """

    xdiff=abs(x2-x1)
    ydiff=abs(y2-y1)

    if xdiff>ydiff:
      if x2>x1:
        for i in range(xdiff):
      else:
        for i in range(xdiff):
    else:
      if y2>y1:
        for i in range(ydiff):
      else:
        for i in range(ydiff):

  def rectangle(self,x,y,xsize,ysize):
    """
    Draws a rectangle in (x,y)
    """

    pass

if __name__=="__main__":
  pass