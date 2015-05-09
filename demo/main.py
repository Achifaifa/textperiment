#!/usr/bin/env python

import math, os, subprocess, time
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
  # c.circle(40,20,10,"0")
  ef.euskallogo(c,vscroll,int(math.floor(step/4)))
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
  # Remove this for release :D
  print beat,"/",cycle,"/",subcycle
  return beat

def decode(string):
  counter=""
  out=""
  for i in string:
    if i.isdigit():counter+=i
    else: 
      if counter:out+=(int(counter)*i)
      else:out+=i
      counter=""
  return out

def decodescroll():
  with open("./rlescroll","r") as scrollin:
    with open("./finalscroll","w+") as scrollout:
      for line in scrollin: scrollout.write(decode(line.rstrip('\n'))+'\n')

def main():
  global cycle
  if audio:
    path=os.getcwd()
    os.system("./midi2beep.py -o music.sh music.mid")
    subprocess.Popen(["bash","music.sh",])
  while 1:
    c.clear()
    beat=updatebeat()
    loop(cycle)
    cycle+=1
    c.draw()
    time.sleep(1/30)

dev=0
audio=0
if __name__=="__main__":
  decodescroll()
  with open("./finalscroll","r") as rles:
    vscroll=rles.readlines()
  if dev: main()
  else:
    try: main()
    except: subprocess.call(["rm","music.sh","finalscroll"]); os.system('clear')
