import math, random

adjust=lambda x: int(math.floor(x))
meatt=1.4
meatgoo=0.95
def meatballs(context,step):

  meatang=3.14*step/150;
  meatballA=[40+math.cos(meatang*5)*35,20+math.sin(meatang*2)*15]
  meatballB=[40+math.sin(meatang*2.6)*35,20+math.cos(meatang*2.0)*15]
  meatballC=[40+math.sin((meatang*2)+100)*35,20+math.cos(meatang+50)*15]

  for i in range(40):
    for j in range(80):
      if (5/math.pow(math.sqrt(math.pow(meatballA[0]-j,2)+math.pow(meatballA[1]-i,2)),meatgoo))+ \
          (10/math.pow(math.sqrt(math.pow(meatballB[0]-j,2)+math.pow(meatballB[1]-i,2)),meatgoo))+ \
          (3/math.pow(math.sqrt(math.pow(meatballC[0]-j,2)+math.pow(meatballC[1]-i,2)),meatgoo))>meatt:
        context.putpixel(j,i,"#")

starsobj=[]
def starfield(context,step):

  def movestar(starobj):

    # Calculate X and Y coordinates
    starxsign=1 if math.cos(starobj["dir"])>=0 else -1
    starysign=1 if math.sin(starobj["dir"])>=0 else -1
    starymax=abs(20*math.sin(starobj["dir"])) if (2.355<starobj["dir"]<3.925 or 5.495<starobj["dir"]<7.075) else 20
    starxmax=abs(40*math.cos(starobj["dir"])) if (0.785<starobj["dir"]<2.355 or 3.925<starobj["dir"]<5.495) else 40
    starxpos=int(math.floor(40+((starxsign*starxmax*starobj["step"])/starobj["speed"]) ))
    starypos=int(math.floor(20+((starysign*starymax*starobj["step"])/starobj["speed"]) ))
    # Paint shit
    fillchar="*" if 0<starxpos<80 or 0<starypos<40 else " "
    try: context.putpixel(starxpos,starypos,fillchar)
    except: pass
    # Incerment star step, reset position and randomize direction if out of field
    if starobj["step"]<starobj["speed"]: starobj["step"]+=0.2
    else:
      starobj["speed"]=20+random.randrange(20);
      starobj["dir"]=random.random()*6.28;
      starobj["step"]=2

  # Create a pool of N stars in random positions
  global starsobj
  if step==1:
    for i in range(20): starsobj.append({"speed":1+random.randrange(10),"dir":random.random()*6.28,"step":3})
  for i in starsobj: movestar(i)

if __name__=="__main__":
  pass

def threedcube(context,step):

  # Position and size
  rotcubex=40;
  rotcubey=20;
  rotcubes=10;
  # Draw moving points
  cubepoint1=[adjust(rotcubex+math.cos(step*0.035)*15),       adjust(rotcubey-rotcubes*0.6+math.sin(step*0.035)*3)      ]
  cubepoint2=[adjust(rotcubex+math.cos((step+45)*0.035)*15),  adjust(rotcubey-rotcubes*0.6+math.sin((step+45)*0.035)*3) ]
  cubepoint3=[adjust(rotcubex+math.cos((step+90)*0.035)*15),  adjust(rotcubey-rotcubes*0.6+math.sin((step+90)*0.035)*3) ]
  cubepoint4=[adjust(rotcubex+math.cos((step+135)*0.035)*15), adjust(rotcubey-rotcubes*0.6+math.sin((step+135)*0.035)*3)]
  cubepoint5=[cubepoint1[0],cubepoint1[1]+10]
  cubepoint6=[cubepoint2[0],cubepoint2[1]+10]
  cubepoint7=[cubepoint3[0],cubepoint3[1]+10]
  cubepoint8=[cubepoint4[0],cubepoint4[1]+10]
  context.line(cubepoint1[0],cubepoint1[1],cubepoint2[0],cubepoint2[1],".")
  context.line(cubepoint2[0],cubepoint2[1],cubepoint3[0],cubepoint3[1],".")
  context.line(cubepoint3[0],cubepoint3[1],cubepoint4[0],cubepoint4[1],".")
  context.line(cubepoint4[0],cubepoint4[1],cubepoint1[0],cubepoint1[1],".")
  context.line(cubepoint5[0],cubepoint5[1],cubepoint6[0],cubepoint6[1],".")
  context.line(cubepoint6[0],cubepoint6[1],cubepoint7[0],cubepoint7[1],".")
  context.line(cubepoint7[0],cubepoint7[1],cubepoint8[0],cubepoint8[1],".")
  context.line(cubepoint8[0],cubepoint8[1],cubepoint5[0],cubepoint5[1],".")
  context.line(cubepoint1[0],cubepoint1[1],cubepoint5[0],cubepoint5[1],".")
  context.line(cubepoint2[0],cubepoint2[1],cubepoint6[0],cubepoint6[1],".")
  context.line(cubepoint3[0],cubepoint3[1],cubepoint7[0],cubepoint7[1],".")
  context.line(cubepoint4[0],cubepoint4[1],cubepoint8[0],cubepoint8[1],".")
