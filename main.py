#!/usr/bin/env python

import time
import effects, engine

c=engine.context()

def loop(step):
  effects.meatballs(c,step)

if __name__=="__main__":
  step=1
  while 1:
    c.clear()
    loop(step)
    step+=1
    c.draw()
    time.sleep(1/30)
