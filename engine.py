#!/usr/bin/env python

import os

class context:

  def __init__(self,x,y):
    self.grid=[[" " for i in range(x)] for i in range(y)]
    self.xsize=x
    self.ysize=y

  def clear(self):
    self.grid=[[" " for i in range(self.xsize)] for i in range(self.ysize)]

  def draw(self):
    os.system('clear')
    for i in self.grid: print "".join(i)
