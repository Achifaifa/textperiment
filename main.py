#!/usr/bin/env python

import time
import effects, engine

c=engine.context()

def loop(step):
  #effects.meatballs(c,step)
  effects.starfield(c,step)

def main():
  step=1
  while 1:
    c.clear()
    loop(step)
    step+=1
    c.draw()
    time.sleep(1/30)

if __name__=="__main__":
  try:
    main()
  except KeyboardInterrupt:
    exit()
