#!/usr/bin/env python
# coding: utf-8

# # TAREA 5

# ### Ejercicio 1: Diferenciación numérica

# In[2]:


import math
from numpy import arange
from matplotlib.pyplot import figure, show

def f(x):
    return 1 + 0.5 * math.tanh(2 * x)

def central_diff(x):
    return (f(x + 0.1) - f(x - 0.1)) / 0.2

def analytic(x):
    return 1 - math.pow(math.tanh(2 * x), 2)

x = arange(-2.0, 2.0, 0.01)

y = []
z = []

for x1 in x:
    y.append(central_diff(x1))
    z.append(analytic(x1))

fig = figure(1)

ax1 = fig.add_subplot(211)
ax1.plot(x, y, dashes=[30, 5, 10, 5])
ax1.grid(True)
ax1.set_ylim((0, 1))
ax1.set_title('Diferencias Centrales')

ax2 = fig.add_subplot(212)
ax2.plot(x, z)
ax2.grid(True)
ax2.set_ylim((0, 1))
ax2.set_title('Método Analítico')

show()


# ### Ejercicio 2 Campo el ́ectrico de una distribuci ́on de cargas.

# Incisos a y b

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def Potencial(carga, posicion, x, y, k=1):
    den = np.hypot(x - posicion[0], y - posicion[1])
    return k * carga / (den + 0.001)

nx, ny = 100, 100
x = np.linspace(-50, 50, nx)
y = np.linspace(-50, 50, ny)
X, Y = np.meshgrid(x, y)

cargas = [(-1, (5, 0)), (1, (-5, 0))]
V = np.zeros((ny, nx))
for carga in cargas:
    ev = Potencial(*carga, x=X, y=Y)
    V += ev

figura = plt.figure(figsize=(7, 7))
plt.contourf(X, Y, V, 20, cmap='RdGy')
plt.colorbar()

Ey, Ex = np.gradient(V, x, y)

figura = plt.figure(figsize=(8, 8))
eje = figura.add_subplot(111)
color = np.log(np.hypot(Ex, Ey))
eje.streamplot(X, Y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
               density=1, arrowstyle='->', arrowsize=1.5)
colores_cargas = {True: '#aa0000', False: '#0000aa'}
for carga, posicion in cargas:
    eje.add_artist(Circle(posicion, 1, color=colores_cargas[carga > 0]))

plt.show()


# Inciso c

# In[17]:


import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


L = 0.1  
q0 = 100  
N = 100 
ϵ = 1e-10 

x = np.linspace(-L/2, L/2, N)
y = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, y)


def sigma(x, y):
    return q0 * np.sin(2 * np.pi * (x + L/2) / L) * np.sin(2 * np.pi * (y + L/2) / L)


Φ = np.zeros((N, N))


for i in tqdm(range(N)):
    for j in range(N):
    
        for u in np.linspace(-L/2, L/2, 100):  
            for v in np.linspace(-L/2, L/2, 100):  
                r = np.sqrt((X[i, j] - u)**2 + (Y[i, j] - v)**2) + ϵ
                Φ[i, j] += sigma(u, v) / r * (L / 100) * (L / 100)  

Ex, Ey = np.gradient(-Φ, x, y)

plt.figure(figsize=(14, 6))

# Mapa de calor del potencial
plt.subplot(1, 2, 1)
plt.imshow(Φ, extent=[-L/2, L/2, -L/2, L/2], origin='lower', cmap='hot', interpolation='bilinear')
plt.colorbar(label='Potencial (Φ)')
plt.title('Potencial Eléctrico')
plt.xlabel('x (m)')
plt.ylabel('y (m)')

# Campo eléctrico
plt.subplot(1, 2, 2)
plt.quiver(X, Y, Ex, Ey, color='blue', scale=5)
plt.title('Campo Eléctrico')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.axis('equal')

plt.tight_layout()
plt.show()


# ### Ejercicio 3

# In[26]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

try:
    datos_altitud = np.loadtxt('altitudes2.txt')
    datos_stm = np.loadtxt('stm.txt')
except Exception as e:
    print(f"No se cargaron los datos: {e}")
    exit(1)

h_altitud = 30000
h_stm = 2.5
phi_altitud = 45

def calcular_derivadas(datos, h):
    dx = np.gradient(datos, h, axis=1)
    dy = np.gradient(datos, h, axis=0)
    return dx, dy

# Explica qué método utilizaste y porqué.
# Definimos la  función calcular_derivadas que utilizó np.gradient para
#calcular las derivadas parciales.
#Usamos np.gradient, que calcula la tasa de cambio en cada punto del arre
#glo.

# Usé el método de las diferencias finitas, ya que se basa en la idea de 
#que la derivada en un punto puede aprximarse usando los valores de la fun
#ción en puntos cercanos.
#Este metodo es más simple y sirve mejor para datos discretos como los presentados


def calcular_intensidad(dx, dy, phi):
    return np.sqrt(dx**2 + dy**2) * np.cos(np.radians(phi))

def graficar_densidad(datos, intensidad, titulo):
    plt.imshow(intensidad, cmap='hot', interpolation='nearest')
    plt.title(titulo)
    plt.colorbar()
    plt.show()

dx_altitud, dy_altitud = calcular_derivadas(datos_altitud, h_altitud)
intensidad_altitud = calcular_intensidad(dx_altitud, dy_altitud, phi_altitud)
graficar_densidad(datos_altitud, intensidad_altitud, 'Mapa de Intensidad - Datos de Altitud')

X = np.arange(datos_stm.shape[1])
Y = np.arange(datos_stm.shape[0])
X, Y = np.meshgrid(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, datos_stm, cmap='viridis')

ax.set_title('Superficie de Silicio (STM)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Altura')
plt.show()


# In[ ]:




