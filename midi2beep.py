#!/usr/bin/python
import midi,math,sys,os,getopt

mult=3.0
split=15
mn=0
comp=0.9
havetoclose=0
execute=0
chord=99
mint=0
try:
	opts,args=getopt.getopt(sys.argv[1:], 'het:k:c:m:s:n:o:', ['help','execute','time=','kill=','compensation=', 'multiplier=','split=','minimum=','output='])
except getopt.GetoptError:
	sys.stdout=sys.stderr
	print "Invalid options"
	usage()
	sys.exit(2)
for o,a in opts:
	if o in ("-h","--help"):
		sys.stdout=sys.stderr
		usage()
		sys.exit(0)
	if o in ("-c","--compensation"): comp=float(a)
	if o in ("-k","--kill"): chord=int(a)
	if o in ("-m","--multiplier"): mult=float(a)
	if o in ("-s","--split"): split=int(a)
	if o in ("-n","--minimum"): mn=int(a)
	if o in ("-o","--output"):
		sys.stdout=file(a,"w")
		havetoclose=1
	if o in ("-e","--execute"):
			execute=1
if len(args) < 1:
	sys.stdout=sys.stderr
	print "No input MIDI file"
	usage()
	sys.exit(1)

m = midi.MidiFile()
m.open(args[0])
m.read()
m.close()

ctime=0

if len(args) == 1:
	tcks=range(len(m.tracks))
else:
	tcks=args[1:]

xt=list()

ntk=0

for i in tcks:
	xt=xt+m.tracks[int(i)].events
	ntk=max(ntk,int(i))

for e in xt:
	if e.type=="NOTE_OFF":
		e.time += 5
		pass

concnotes=[0]
	
for i in range(ntk):
	concnotes.append(0)


def mnf_calc(n):
	base_a4=440
	if (n>=0) and (n<=119):
		return int(base_a4*pow(2,(n-57.0)/12.0))
	else:
		return -1
### END MNF_CALC

def xprint(text):
	if execute==1:
		if os.system(text) != 0:
			sys.exit(1)
	else:
		print text


mnf_d=dict()

for i in range(120):
	mnf_d[i]=mnf_calc(i)

def mnf(n):
	if (n>=0) and (n<=119):
		return mnf_d[n-12]
	else:
		return -1
### END MNF

cnotes=list()

xt.sort(lambda x, y: x.time-y.time)

nfpause=0

def fixup(s):
	s2=""
	for i in range(len(s)):
		if s[i]=="'":
			s2 = s2+"'"
		elif s[i]=="\r":
			s2 = s2+"\\n"
		else:
			s2 = s2 + s[i]
	return s2

print "#!/bin/sh"
print "set -e"


for j in xt:
	if j.time>(ctime):
		c2x=cnotes
		c2=list()
		
		for i in range(len(c2x)):
			(np,tn)=c2x[i]
			if concnotes[tn]<=chord:
				c2.append(np)
		
				
		xtxt="echo 'Tracks: "
		for i in tcks:
			xtxt=xtxt+str(int(i))+"["+str(concnotes[int(i)])+"]"
			if concnotes[int(i)]>chord:
				xtxt=xtxt+'* '
			else:
				xtxt=xtxt+'  '
		xprint(xtxt+"'")
		
		c2.sort()
		
		for i in range(len(c2)-1):
			if c2[i]==c2[i+1]:
				c2[i]=-1
			if c2[i]<mn:
				c2[i]=-1
		nf=1
		ln=0
		
		
		
		
		for i in c2:
			if i!=(-1):
				ln=ln+1
				if nf==1:
					fn=i
					nf=0
		if ln==0:
			if nfpause:
				xprint("beep -f 1 -l 0 -D "+str(int((j.time-ctime)*mult)))
		elif ln==1:
			xprint("beep -f "+str(mnf(fn))+" -l "+str((j.time-ctime)*mult))
			nfpause=1
		else:
			nfpause=1
			cmd=""
			xlen=int(((j.time-ctime)*mult)*comp)
			nnew=1
			while xlen>0:
				for i in c2:
					if i==(-1):
						continue
					if not nnew:
						cmd=cmd+"-n "
					if xlen>=split:
						cmd=cmd+"-f "+str(mnf(i))+" -l "+str(split)+" "
						xlen=xlen-split
					else:
						cmd=cmd+"-f "+str(mnf(i))+" -l "+str(xlen)+" "
						xlen=0
					nnew=0
			xprint("beep "+cmd)
		ctime=j.time
	if j.type=="LYRIC":
		xprint("echo -ne \""+fixup(str(j.data))+"\"")
	if j.type=="TEXT_EVENT":
		xprint("echo "+j.type+" "+str(j.data))
	if j.type=="NOTE_ON" and j.velocity>0:
		print "#NON: "+str(j.pitch)+" "+str(j.track.index)
		cnotes.append((j.pitch,j.track.index))
		concnotes[j.track.index]=concnotes[j.track.index]+1
		
	if j.type=="NOTE_OFF" or (j.velocity==0 and j.type=="NOTE_ON"):
		print "#NOFF: "+str(j.pitch)+" "+str(j.track.index)
		cnotes.remove((j.pitch,j.track.index))
		concnotes[j.track.index]=concnotes[j.track.index]-1

if havetoclose:
	sys.stdout.close()

