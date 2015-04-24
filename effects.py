import math

meatt=1.4
meatgoo=0.95
def meatballs(context,step):
  """
  meatball effect

  step: clock signal
  """

  meatang=3.14*step/150;
  meatballA=[40+math.cos(meatang*2.5)*35,20+math.sin(meatang*2)*15];
  meatballB=[40+math.sin(meatang*1.8)*35,20+math.cos(meatang*2.0)*15];
  meatballC=[40+math.sin(meatang+100)*35,20+math.cos(meatang+50)*15];

  for i in range(40):
    for j in range(80):
      if (5/math.pow(math.sqrt(math.pow(meatballA[0]-j,2)+math.pow(meatballA[1]-i,2)),meatgoo))+ \
          (10/math.pow(math.sqrt(math.pow(meatballB[0]-j,2)+math.pow(meatballB[1]-i,2)),meatgoo))+ \
          (3/math.pow(math.sqrt(math.pow(meatballC[0]-j,2)+math.pow(meatballC[1]-i,2)),meatgoo))>meatt:
        context.putpixel(j,i,"#")
