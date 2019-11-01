import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from time import clock
for i in plt.rcParams.keys():
	if 'keymap.' in i:
		plt.rcParams[i]=[]
fig, ax = plt.subplots()
xball=[0,0.03]
xballs=[]
yballs=[]
balls,=plt.plot([],[],animated=True)
def press(event):
	if event.key == 'left':
		xball[0]-=1
	elif event.key == 'right':
		xball[0]+=1
	elif event.key == 'up':
		xball[1]+=0.01
	elif event.key == 'down':
		xball[1]-=0.01
fig.canvas.mpl_connect('key_press_event', press)
xdata, ydata = [], []
ln, = plt.plot([], [], animated=True)
ball, = plt.plot([xball[0]],[0],'o',animated=True)
def init():
	ax.set_xlim(0, 2*np.pi)
	ax.set_ylim(-1.5, 1.5)
	return ln,ball,balls
start=[clock()]
def update(frame):
	xdata[:]=np.linspace(frame,2*np.pi+frame,50)
	ydata[:]=np.sin(xdata)
	yballs[:]=np.cos(xdata)
	r=0.05
	xballs[:]=map(lambda x:x[0]-xball[1]*x[1]/np.sqrt(x[1]*x[1]+1),zip(xdata,yballs))
	yballs[:]=map(lambda x:x[0]+xball[1]/np.sqrt(x[1]*x[1]+1),zip(ydata,yballs))
	xdata[:]=map(lambda x:x-frame,xdata)
	xballs[:]=map(lambda x:x-frame,xballs)
	ln.set_data(xdata, ydata)
	x=xballs[xball[0]]
	s=np.sin(x+frame)
	c=np.cos(x+frame)
	x-=xball[1]*c/np.sqrt(c*c+1)
	s+=xball[1]/np.sqrt(c*c+1)
	ball.set_data(x,s)
	balls.set_data(xballs,yballs)
	ani.event_source.interval=5+15*abs(s+1.5)**0.5
	return ln,ball,balls

ani = FuncAnimation(fig, update, frames=np.linspace(0, 4*np.pi, 100),init_func=init, blit=True)
plt.show()