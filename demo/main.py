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
  # ef.transition(c,step)
  # c.circle(40,20,10,"0")
  # ef.fire(c)  
  # ef.parallax(c,cycle*3)
  # ef.scroll(c,"TEST",5,"#",(step)%150)

  if not test:
    # Intro
    if beat<47:
      ef.euskallogo(c,vscroll,int(math.floor(step/3)))
      if beat<20: 
        ef.scroll(c,"EUSKAL ENCOUNTER 23",5,"#",step)
      elif beat<30: 
        ef.scroll(c,"STAGE7",5,"`",auxstep1)
        auxstep1+=1
      else: 
        ef.scroll(c,"ACHIFAIFA",5,"`",auxstep2)
        auxstep2+=1
    # Presentation
    elif beat<79:
      ef.copperbars(c,step)
      c.text(10,3,"#","PRESENT")
      if beat>54:
        c.text(3,13,"#","TEXT")
        c.text(13,23,"#","PERIMENT")
      if beat>60: 
        if beat==61: auxstep1=0
        ef.scroll(c,"A REALTIME ASCII INTRO",32,"#",auxstep1*3)
        auxstep1+=1
    # EF1
    elif beat<110:
      if beat==79: auxstep1=0
      ef.starfield(c,auxstep1*2)
      ef.scroll(c,"you cant use python they said",32,"#",auxstep1)
      auxstep1+=1
    # EF2
    elif beat<141:
      if beat==110: auxstep1=0
      ef.meatballs(c,step)
      ef.scroll(c,"you cant fit it in 64k they said",32,"*",auxstep1*3)
      auxstep1+=1
    # Oh noes...
    elif beat<156:
      if beat==141: auxstep1=0
      ef.threedcube(c,step/2)
      c.text(7,4,"#","oh noes")
      ef.scroll(c,"what can we do",32,"#",auxstep1)
      auxstep1+=1
    # Aha
    elif beat<173:
      if beat==156: auxstep1=0
      ef.parallax(c,step*3)
      ef.scroll(c,"to the batcave",32,"#",auxstep1*2)
      auxstep1+=1
    elif beat<190:
      ef.plasma(c,step)
    elif beat<205:
      c.text(7,4,"#","a")
    elif beat<220:
      c.text(7,4,"#","b")
    elif beat<235:
      c.text(7,4,"#","c")
    elif beat<250:
      c.text(7,4,"#","d")
    elif beat<266:
      c.text(7,4,"#","e")
    else:
      c.text(7,4,"#","f")

    
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
  global cycle, beat
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
  vscroll=decodescroll()
  try: main()
  except: 
    subprocess.call(["rm","music.sh","finalscroll"])
    subprocess.call(["killall","bash"])
    os.system('clear')
    traceback.print_exc()
