import numpy as sp
from scipy.integrate import odeint
import matplotlib.pylab as plt


 # Datos
theta = (7.27* 10**-5)*3600
G = (6.67*10**-11)*(3600**2)*(1000**-3)
mt = 5.972*10**24
r = (6371+700)
rt = 6371

def R(t):
    r0= sp.array([[sp.cos(theta*t),-sp.sin(theta*t)],[sp.sin(theta*t),sp.cos(theta*t)]])
    return r0

def Rt(t):
    rt = sp.array([[sp.cos(theta*t),sp.sin(theta*t)],[-sp.sin(theta*t),sp.cos(theta*t)]])
    return rt

def Rp(t):
    rp = theta * (sp.array([[-sp.sin(theta*t),-sp.cos(theta*t)],[sp.cos(theta*t),-sp.sin(theta*t)]]))
    return rp

def Rpp(t):
    rpp = (theta**2) * (sp.array([[-sp.cos(theta*t),sp.sin(theta*t)],[-sp.sin(theta*t),-sp.cos(theta*t)]]))
    return rpp

 # Funcion a integrar
 # z es el vector de estado
 # z = [x, y, vx, vy]

def satelite(z,t):
    zp = sp.zeros(4)
    zp[0:2] = z[2:4]
    zp[2:4] = -(G * mt / r**3) * z[0:2] - Rt(t) @ (( Rpp(t) @ z[0:2]) + 2 * (Rp(t) @ z[2:4]))

    return zp

# vector de tiempo
t = sp.linspace(0,3.528,1001)
angulo = sp.linspace(0,2*sp.pi,1001)

# condiciones iniciales
vt = 24500

z0 = sp.array([r, 0, 0, vt ])

sol = odeint(satelite, z0, t)

x = sol[:,0]
y = sol[:,1]


plt.figure(1)
plt.plot(x,y)
plt.plot(6371*sp.cos(angulo),6371*sp.sin(angulo),"brown")
plt.show()

