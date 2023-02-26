import numpy as np
import matplotlib.pyplot as plt

#declare some arrays to work with
#declare some arrays to work with
N  = 101
L  = 2.0 
dx = L/(N-1)
x  = np.linspace(0,L,N)
u    = np.zeros(N)
u_dt = np.zeros(N)

#set the convection speed
A = 1
timespan = 1

#set the time step based on the cfl number
Nstep = 49
dt = 1/Nstep
#Nstep = int(timespan/dt)
c = dt/dx



def timestep():
  for i in range(1,N):
    u_dt[i] = u[i] - u[i]* c *(u[i]-u[i-1])
  u[1:] = u_dt[1:]           
  return


#set an intial condition
u0      = np.ones(N)
u0[0:10] = 2
u[:]    = u0[:]
ans = [u0.copy()]
T = [0]

for k in range(0,Nstep):
    timestep()
    #the lines below simply store a copy of the solution 
    #after each time step so that it can be plotted and animated
    ans.append(u.copy())
    T.append(k*dt)

####################
#Create a simple plot of the results    
####################
plt.plot(x,u0)
plt.plot(x,u)
plt.legend(['Initial condition', "Solution at t = {} s".format(timespan)])
plt.xlabel('x')
plt.ylabel('u');

###########
#The code below creates an animation NOT EXAMINABLE!
###########
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

fig,ax = plt.subplots()
ax.plot(x,u0)
ax.set_title('c = {}, A = {}'.format(c,A))
ax.set_xlabel('x')
ax.set_ylabel('u');
uline=ax.plot([],[])[0]
def anim(i):
    uline.set_data(x,ans[i])
    plt.legend(['Initial condition', "Solution at t = {:.2f} s".format(T[i])])
ani = FuncAnimation(fig, anim, frames=range(0,len(ans)),interval=200)    

plt.show()

