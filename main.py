#!/usr/bin/env python

import os, time
import effects, engine

c=engine.context()

def loop(step):
  effects.meatballs(c,step)
  c.text(1,10,".","   TEST")
  # effects.starfield(c,step)
  # effects.threedcube(c,step)

def main():
  step=1
  while 1:
    c.clear()
    loop(step)
    step+=0.3
    c.draw()
    time.sleep(1/30)

if __name__=="__main__":
  try:
    os.system('clear')
    main()
  except KeyboardInterrupt:
    os.system('clear')
    exit()
