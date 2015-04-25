#!/usr/bin/env python

import font
import math, os

adjust=lambda x: int(math.floor(x))

class context:

  def __init__(self):
    """
    Initializes a work area
    """

    x,y=80,40
    self.grid=[[" " for i in range(x)] for i in range(y)]
    self.xsize=x
    self.ysize=y

  def draw(self):

    print "\x1B[1;1H"
    for i in self.grid: print "".join(i)

  def line(self,x0,y0,x1,y1,char):
    """
    Stole this shit from wikipedia

    https://en.wikipedia.org/wiki/Bresenham's_line_algorithm#Line_equation
    """

    sign=lambda x: cmp(x,0) #Python doesn't have this and that's dumb
    
    deltax=x1-x0
    deltay=y1-y0
    error=0
    if x0>x1: x0,y0,x1,y1=x1,y1,x0,y0
    try:
      deltaerr=abs(deltay/deltax)
      y=y0
      for x in range(x0,x1+1):
        self.grid[y][x]=char
        error+=deltaerr
        while error>=0.5:
          self.grid[y][x]=char
          y+=sign(y1-y0)
          error-=1
    #And then added this for vertical lines
    except ZeroDivisionError:
      for i in range(abs(deltay)): self.grid[y0+(i*sign(y1-y0))][x0]=char
    # if deltax>deltay:
    #   if x0>x1: x0,y0,x1,y1=x1,y1,x0,y0
    #   if y1>y0:
    #     for i in range(1,deltax+1): self.grid[adjust(y0+deltay*(i/deltax))][x0+i]=char
    #   else:
    #     for i in range(1,deltax+1): self.grid[adjust(y0-deltay*(i/deltax))][x0+i]=char
    # else:
    #   if y0>y1: x0,y0,x1,y1=x1,y1,x0,y0
    #   if x1>x0:
    #     for i in range(1,deltay+1): self.grid[y0+i][adjust(x0+deltax*(i/deltay))]=char
    #   else:
    #     for i in range(1,deltay+1): self.grid[y0+i][adjust(x0-deltax*(i/deltay))]=char

  def putpixel(self,x,y,char):

    self.grid[y][x]=char

  def rectangle(self,x,y,xsize,ysize,char):

    self.line(x,y,x+xsize,y,char)
    self.line(x,y,x,y+ysize,char)
    self.line(x+xsize,y,x+xsize,y+ysize,char)
    self.line(x,y+ysize,x+xsize,y+ysize,char)

  def text(self,x,y,string):

    for i in range(7): #Height of the font
      line="".join([eval("font."+letter+"[i]") for letter in string.lower().replace(" ","_")])
      for j in range(79-x): #total space left
        try:
          self.putpixel(x+j,y+i,line[j])
        except: 
          pass

  def clear(self):

    self.grid=[[" " for i in range(self.xsize)] for i in range(self.ysize)]
    self.rectangle(0,0,79,39,"#")

if __name__=="__main__":
  pass
