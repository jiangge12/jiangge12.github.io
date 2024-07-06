import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.animation as animation

p0=2
q0=2

fig=plt.figure()
plt.rcParams['axes.facecolor'] = 'black'
axs=fig.add_subplot(111)		#1*1的网格，第1个图
axs.grid()
axs.set(xlim=[-1.5,1.5],ylim=[-1.5,1.5],title='Lissajous-Figure')
theta=np.linspace(0,2*np.pi,1000)
x=np.sin(theta)
y=np.sin(theta)
Liss,=axs.plot(x,y,'lime',linewidth=3)

def updata(n):
    global p0,q0
    
    p0=p0+0.012
    p=int(p0)
    q0=q0+0.02
    q=int(q0)
    
    x=np.sin(p*theta)
    y=np.sin(q*theta+n*np.pi)
    Liss.set_data(x,y)
    return Liss
ani=animation.FuncAnimation(fig,updata,frames=np.linspace(0,2,100),interval=50)
ani.save('Liss.gif')
plt.show()


    
    
    