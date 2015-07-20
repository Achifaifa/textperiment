#!/usr/bin/env python

import math, os, subprocess, sys, time, traceback
import effects as ef, engine
adjust=lambda x: int(math.floor(x))
c=engine.context()
startdate=time.time()*1000
beat=0
cycle=1
auxstep1=auxstep2=0
test=0

def loop(step):

  global auxstep1,auxstep2
  # DANGER ZONE

  if not test:
    # Intro
    if beat<47:
      ef.euskallogo(c,vscroll,int(math.floor(step/3)))
      if beat<18: 
        ef.scroll(c,"EUSKAL ENCOUNTER 23",5,"#",step)
      elif beat<30: 
        if beat==18: auxstep1=step
        ef.scroll(c,"STAGE7",5,"`",step-auxstep1)
      else: 
        if beat==30: auxstep2=step
        ef.scroll(c,"ACHIFAIFA",5,"`",step-auxstep2)
    # Presentation
    elif beat<79:
      ef.copperbars(c,step)
      c.text(10,3,"#","PRESENT")
      if beat>54:
        c.text(3,13,"#","TEXT")
        c.text(13,23,"#","PERIMENT")
      if beat>60: 
        if beat==61: auxstep1=step
        ef.scroll(c,"A REALTIME ASCII INTRO",32,"#",step-auxstep1)
    elif beat<110:
      if beat==79: auxstep1=step
      ef.starfield(c,step-auxstep1)
      ef.scroll(c,"you cant use python they say",32,"#",step-auxstep1)
    elif beat<141:
      if beat==110: auxstep1=step
      ef.meatballs(c,step)
      ef.scroll(c,"you cant fit it in 64k they say",32,"*",step-auxstep1)
    elif beat<156:
      if beat==141: auxstep1=step
      ef.threedcube(c,step/2)
      c.text(7,4,"#","oh noes")
      ef.scroll(c,"what can we do",32,"#",step-auxstep1)
    elif beat<173:
      if beat==156: auxstep1=step
      ef.parallax(c,step*3)
      ef.scroll(c,"to the batcave",32," ",step-auxstep1)
    elif beat<189:
      ef.plasma(c,step)
    elif beat<205:
      ef.moire(c,step)
    elif beat<220:
      c.text(2,4,"#","after much")
      c.text(2,12,"#","time")
    elif beat<236:
      ef.automaton(c,step)
      c.text(7,4,"x","and")
      c.text(2,12,"x","headaches")
    elif beat<251:
      c.text(7,4,"#","its ready")
    elif beat<266:
      ef.floppyrainbow(c,floppy,step)
      c.text(7,4,"#","behold")
    elif beat<282:
      c.text(1,2,"#","mwahahahahahahahahah")
    elif beat<298:
      c.text(5,4,"#","brilliant")
    elif beat<314:
      ef.fire(c)
      c.text(4,3,"#", "the compo")
      c.text(4,11,"#"," is ours")
    elif beat<329:
      c.text(7,4,"#","radar")
    elif beat<402:
      c.text(9,4,"#","credits")
    elif beat<450: 
      ef.euskallogo(c,vscroll,55)
    else: 1/0

    
def decode(string):
  counter="";out=""
  for i in string:
    if i.isdigit():counter+=i
    else: 
      if counter:out+=(int(counter)*i)
      else:out+=i
      counter=""
  return out

def decodefile(path):

  with open(path,"r") as rlein:
    return [decode(line.rstrip('\n')) for line in rlein]

def main():
  global cycle, beat
  os.system('clear')
  os.system("./midi2beep.py -o music.sh music.mid")
  subprocess.Popen(["bash","music.sh",])
  while 1:
    c.clear()
    beat=adjust((time.time()*1000-startdate)/326)
    print beat,"/",cycle
    loop(cycle)
    cycle=adjust((time.time()*1000-startdate)/25)
    c.draw()
    time.sleep(1/15)#30

if __name__=="__main__":
  vscroll=decodefile("./rlescroll")
  floppy=decodefile("./rlefloppy")
  try: main()
  except: 
    subprocess.call(["rm","music.sh","finalscroll"])
    subprocess.call(["killall","bash"])
    os.system('clear')
    traceback.print_exc()
