#!/usr/bin/env python

import os, subprocess, time
import effects as ef, engine

c=engine.context()
lastdate=time.time()*1000
beatpool=0
beat=0
cycle=subcycle=1


def loop(step):

  # DANGER ZONE
  # ef.meatballs(c,step)
  # c.text(1,10,".","   TEST")
  # ef.starfield(c,step)
  # ef.threedcube(c,step/3)
  # ef.scroll(c,"TEST",5,"#",step*2)
  c.circle(40,20,10,"0")
  # DEMO ZONE
  if beat==235:1/0

def updatebeat():
  
  global lastdate,beatpool,beat
  utime=time.time()*1000;
  beatpool=beatpool+(utime-lastdate);
  lastdate=utime;
  if beatpool>363:
    beatpool=0;
    beat=beat+1;
  # Beat printing for syncing and debugging
  # Remove for release pl0x
  print beat,"/",cycle,"/",subcycle
  return beat

def main():

  global cycle
  # path=os.getcwd()
  # os.system("./midi2beep.py -o flea.sh music.mid 1 2 6 7")
  # subprocess.Popen(["bash","flea.sh",])
  while 1:
    c.clear()
    beat=updatebeat()
    loop(cycle)
    cycle+=1
    c.draw()
    time.sleep(1/30)

if __name__=="__main__":
  main()
  #try: main()
  #except: subprocess.call(["rm","flea.sh"]); os.system('clear')
