#!/usr/bin/env python

import math, os, subprocess, sys, time, traceback
import effects as ef, engine
adjust=lambda x: int(math.floor(x))
c=engine.context()
lastdate=time.time()*1000
beatpool=0
beat=0
cycle=subcycle=1

stagestep=achistep=0
test=0
def loop(step):

  global stagestep
  global achistep
  # DANGER ZONE
  # ef.meatballs(c,step)
  # c.text(1,10,".","   TEST")
  # ef.starfield(c,step)
  # ef.threedcube(c,step/2)
  # c.circle(40,20,10,"0")
  # ef.euskallogo(c,vscroll,int(math.floor(step/4)))
  # ef.fire(c)  
  # ef.parallax(c,cycle)
  # ef.scroll(c,"TEST",5,"#",(step)%150)
  # DEMO ZONE
  if not test:
    if beat<40:
      ef.euskallogo(c,vscroll,int(math.floor(step/3)))
      if beat<16: 
        ef.scroll(c,"EUSKAL ENCOUNTER 23",5,"#",step)
      elif beat<24: 
        ef.scroll(c,"STAGE7",5,"`",stagestep)
        stagestep+=1
      elif beat<34: 
        ef.scroll(c,"ACHIFAIFA",5,"*",achistep)
        achistep+=1
    elif beat<235:
      ef.meatballs(c,step)
      if beat%2==0: c.text(10,10,".","UNTZ")
      else: c.text(40,30,".","UNTZ")
    if beat==235:1/0

def updatebeat():
  
  global lastdate,beatpool,beat
  utime=time.time()*1000;
  beatpool=beatpool+(utime-lastdate);
  lastdate=utime;
  if beatpool>429:
    beatpool=0;
    beat=beat+1;
  # Remove this for release :D
  print beat,"/",cycle,"/",subcycle
  return beat

def decode(string):
  counter="";out=""
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
  with open("./finalscroll","r") as rles: return rles.readlines()

def main():
  global cycle
  os.system("./midi2beep.py -o music.sh music.mid")
  subprocess.Popen(["bash","music.sh",])
  while 1:
    c.clear()
    beat=updatebeat()
    loop(cycle)
    cycle+=1
    c.draw()
    time.sleep(1/15)#30

if __name__=="__main__":
  vscroll=decodescroll()
  try: main()
  except: 
    subprocess.call(["rm","music.sh","finalscroll"])
    subprocess.call(["killall","bash"])
    os.system('clear')
    traceback.print_exc()
