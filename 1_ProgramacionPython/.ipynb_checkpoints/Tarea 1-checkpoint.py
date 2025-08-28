#!/usr/bin/env python
# coding: utf-8

# # Programación Básica para la física computacional
# ### Luis Daniel Amador Islas

# ## 1. Altitud de un satélite: 
# Se va a lanzar un satélite en una órbita circular alrededor de la tierra de modo que orbite el planeta una vez cada T segundos

# _a)_ Demuestre que la altitud $h$ sobre la superficie de la Tierra que debe tener el satélite es: 
# $$
# h = \left( \frac{GM T^2}{4 \pi^2} \right)^{1/3} - R,
# $$
# donde $G = 6.67 \times 10^{-11}\text{m}^3\text{kg}^{-1}\text{s}^{-2}$ es la constante gravitatoria de Newton, $M = 5.97 \times 10^{24}\text{kg}$ es la mas de la Tierra y $R = 6371 \text{km}$ es su radio.

# RESPUESTA
# ---
# Un satélite en órbita circular cumple que la fuerza gravitacional actúa como fuerza centrípeta:
# 
# $$
# F_g = F_c
# $$
# 
# ---
# $$
# F_g = \frac{GMm}{(R+h)^2}
# $$
# 
# donde:
# - $G$ = constante gravitatoria universal,
# - $M$ = masa de la Tierra,
# - $R$ = radio de la Tierra,
# - $h$ = altura sobre la superficie.
# 
# ---
# 
# $$
# F_c = m \frac{v^2}{R+h}
# $$
# 
# La velocidad en órbita circular de radio \(R+h\) es:
# 
# $$
# v = \frac{2\pi (R+h)}{T}
# $$
# 
# Elevando al cuadrado:
# 
# $$
# v^2 = \frac{4\pi^2 (R+h)^2}{T^2}
# $$
# 
# $$
# F_c = m \frac{v^2}{R+h}
# = m \frac{\tfrac{4\pi^2 (R+h)^2}{T^2}}{R+h}
# $$
# 
# $$
# F_c = m \frac{4\pi^2 (R+h)}{T^2}
# $$
# 
# $$
# \frac{GMm}{(R+h)^2} = m \frac{4\pi^2 (R+h)}{T^2}
# $$
# 
# Cancelamos $m$
# 
# $$
# \frac{GM}{(R+h)^2} = \frac{4\pi^2 (R+h)}{T^2}
# $$
# 
# $$
# GM = \frac{4\pi^2 (R+h)^3}{T^2}
# $$
# 
# $$
# (R+h)^3 = \frac{GM T^2}{4\pi^2}
# $$
# 
# $$
# R+h = \left(\frac{GM T^2}{4\pi^2}\right)^{1/3}
# $$
# 
# $$
# \therefore \boxed{\quad h = \left(\frac{GM T^2}{4\pi^2}\right)^{1/3} - R}
# $$
# 

# _b)_ Escribe un programa que le pida al usuario que ingrese el valor deseado de T y luego calcula e imprima la altitud correcta en metros.

# In[14]:


#Constantes
G = 6.67e-11  # Constante gravitacional
M = 5.97e24   # Masa de la Tierra
R = 6371000   # Radio de la Tierra en metros

# Pedir el período orbital al usuario
T = float(input("Ingresa el período orbital T en segundos: "))

# Calcular el radio orbital
r = ((G * M * T**2) / (4 * 3.1416**2))**(1/3)

# Calcular la altitud
h = r - R

# Resultados
print(f"Período orbital: {T} segundos")
print(f"Radio orbital: {r:,.0f} metros")
print(f"Altitud sobre la Tierra: {h:,.0f} metros")
print(f"Altitud en kilómetros: {h/1000:,.0f} km")


# c) Utiliza tu programa para calcular las altitudes de los satélites que orbitan la Tiera una vez al día (la llamada órbita _geoestacionaria_), una vez cada **90 minutos** y una vez cada **45 minutos**. ¿Qué concluyes de este último cálculo?

# ### 90 minutos
# - Período orbital: 5400.0 segundos 
# - Radio orbital: 6,650,311 metros 
# - Altitud sobre la Tierra: 279,311 metros
# - Altitud en kilómetros: 279 km 

# ### 45 minutos
# - Período orbital: 2700.0 segundos
# - Radio orbital: 4,189,434 metros
# - Altitud sobre la Tierra: -2,181,566 metros
# - Altitud en kilómetros: -2,182 km

# El satélite con período orbital de 45 minutos tiene una altitud negativa, lo cual es físicamente imposible, ya que un satélite no puede orbitar debajo de la superficie terrestre, violando de leyes físicas pues la orbita requeriría un radio menor que el de la Tierra misma. Por lo que el período es demasiado corto, para una órbita circular estable alrededor de la Tierra.
# Esto demuestra que no todos los períodos orbitales son físicamente posibles, deben cumplir con la condición de que el radio orbital sea mayor o igual al radio terrestre.
# 

# ## 2. Paso de potencial cuántico:
# Un conocido problema de mecánica cuántica involucra una partícula de masa _m_ que encuentra un paso de potencial unidimensional, como este:

# In[2]:


from IPython.display import Image
Image(filename= 'C:/Users/DANROK/Fisica_Computacional/Repositorio_Fisica_Computacional/1_ProgramacionPython/Diagrama_T1_E2.jpg')


# La partícula con energía cinética inicial _E_ y vector de onda $k_1 = \sqrt{2mE}/\hbar$ entra por la izquierda y encuentra un salto repentino en la energía potencial de altura _V_ en la posicion $x = 0$. Resolviendo la ecuación de Scrödinger, se puede demostrar que cuando $E > V$ la partícula puede

# _a_) Pasar el escalón, en cuyo caso tiene una energía cinética menor a $E - V$ en el otro lado y un vector de onda correspondiente menor a $k_2 = \sqrt{2m(E - V)}/\hbar$, o bien

# RESPUESTA
# ---
# Para E > V, la función de onda tiene la forma:
# $$ ψ₁(x) =  Ae^{(ik₁x)} + Be^{(-ik₁x)}$$ 
# en la region (x < 0)
# 
# Y $$ψ₂(x) = Ce^{(ik₂x)}$$ en la region (x ≥ 0)
# 
# Aplicando condiciones de continuidad en x = 0:
# $$ ψ₁(0) = ψ₂(0) ⇒ A + B = C $$
# $$ \frac{dψ₁}{dx(0)} = \frac{dψ₂}{dx(0)} ⇒ ik₁(A - B) = ik₂C$$
# 
# $$
# \therefore \boxed{T = \frac{4k_1k_2}{(k_1 + k_2)^2}}
# $$

# _b_) Reflejarse, manteniendo toda su energía cinética y un vector de onda sin cambios, pero moviéndose en la dirección opuesta. Las probabilidades _T_ y _R_ de transmisión y reflexión están dadas por:
# $$
# T = \frac{4k_1k_2}{(k_1 + k_2)^2} \, , R= \left(\frac{k_1 - k_2}{k_1 + k_2} \right)^2.
# $$

# RESPUESTA
# ---
# Para que se cumpla que T + R = 1 lo que garantiza la conservación de la probabilidad. Demostramos que $ T + R = 1 $ cuando $ E > V $ usando que:
# 
# $$
# T + R = \frac{4k_1k_2}{(k_1 + k_2)^2} + \left( \frac{k_1 - k_2}{k_1 + k_2} \right)^2
# $$
# 
# Escribimos ambos términos con denominador común $(k_1 + k_2)^2$
# $$
# ⇒T + R = \frac{4k_1k_2}{(k_1 + k_2)^2} + \frac{(k_1 - k_2)^2}{(k_1 + k_2)^2}
# $$
# 
# $$
# ⇒T + R = \frac{4k_1k_2 + (k_1 - k_2)^2}{(k_1 + k_2)^2}
# $$
# 
# $$
# ⇒(k_1 - k_2)^2 = k_1^2 - 2k_1k_2 + k_2^2
# $$
# $$
# ⇒4k_1k_2 + (k_1 - k_2)^2 = 4k_1k_2 + k_1^2 - 2k_1k_2 + k_2^2 = k_1^2 + 2k_1k_2 + k_2^2
# $$
# 
# $$
# ⇒k_1^2 + 2k_1k_2 + k_2^2 = (k_1 + k_2)^2
# $$
# 
# $$
# \therefore \boxed{T + R = \frac{(k_1 + k_2)^2}{(k_1 + k_2)^2} = 1}
# $$
# 
# Esto significa que toda partícula incidente debe ser transmitida o reflejada, sin pérdida de probabilidad.

# Supongamos que tenemos una partícula con una masa igual a la masa del electrón. $m = 9.11 \times 10^{-31} \text{kg}$ y energía de $10 \text{eV}$, al encontrar un escalón de potencial de altura $9\text{eV}$. Escribe un programa en <tt>Python</tt> para calcular e imprimir las probabilidades de transmisíon y reflexión utilizando las fórmulas anteriores.

# In[2]:


# Constantes físicas
m = 9.11e-31  # kg (masa del electrón)
E = 10.0      # eV (energía)
V = 9.0       # eV (altura del potencial)
hbar = 6.582e-16  # ħ en eV·s

# Calcular vectores de onda
import math
k1 = math.sqrt(2 * m * E) / hbar
k2 = math.sqrt(2 * m * (E - V)) / hbar

# Calcular probabilidades
T = (4 * k1 * k2) / ((k1 + k2)**2)
R = ((k1 - k2) / (k1 + k2))**2

# Mostrar resultados
print(f"Vector de onda k₁: {k1:.3e} m⁻¹")
print(f"Vector de onda k₂: {k2:.3e} m⁻¹")
print()
print(f"Probabilidad de transmisión T: {T:.6f}")
print(f"Probabilidad de reflexión R: {R:.6f}")
print(f"Suma T + R: {T + R:.6f}")


# ## 3. Órbitas Planetarias:
# En el espacio, la órbita de un cuerpo alrededor de otro (como un planeta alrededor del Sol), no necesariamente es circular. En general, toma la forma de una elipse, con el cuerpo a veces más cerca y otras más lejos. Si tenemos la distancia $\ell$ de máxima aproximación de un planeta al Sol (su <i>perihelio</i>), y su velocidad lineal $v_1$ en el perihelio, entonces cualquier otra propiedad de la órbita se puede calcular a partir de estas dos cantidades de la siguiente manera:

# _a_) La segunda le de Kepler nos dice que la distancia $\ell_2$ y la velocidad $v_2$ del planeta en su punto más distante, o <i>afelio</i>, satisfacen que $\ell_2v_2 = \ell_1v_1$. Al mismo tiempo. la energía total, cinética más la gravitatoria, de un planeta con velocidad $v$ y distancia $r$ del Sol está dada por:
# $$
# E = \frac{1}{2}mv^2 - G\frac{mM}{r},
# $$
# donde $m$ es la masa del planeta, $M = 1.9891 \times 10^30 \text{kg}$ es la masa del Sol y $G = 6.6738 \times 10^{-11}\text{m}^3\text{kg}^{-1}\text{s}^{-2}$ es la constante gravitatoria de Newton. Dado que la energía debe conservarse, demuestra que $v_2$ es la raíz más pequeña de la ecuación cuadrática:
# $$
# v^2_2 - \frac{2GM}{v_1\ell_1}v_2 - \left[ v_1 - \frac{2GM}{\ell_1} \right] = 0
# $$
# Una vez que tenemos $v_2$ podemos calcular $\ell_2$ usando la relación $\ell_2 = \ell_1v_1/v_2$.

# RESPUESTA
# ---
# Utilizando la conservación de la energía y la segunda ley de Kepler.
# - En el perihelio: distancia $ \ell_1 $, velocidad $ v_1 $
# - En el afelio: distancia $ \ell_2 $, velocidad $ v_2 $
# - Segunda ley de Kepler: $ \ell_1 v_1 = \ell_2 v_2 $  (conservación del momento angular)
# - Conservación de la energía:
#   $$
#   E = \frac{1}{2} m v_1^2 - G \frac{m M}{\ell_1} = \frac{1}{2} m v_2^2 - G \frac{m M}{\ell_2}
#   $$
# 
# 
# De la segunda ley de Kepler expresamos $ \ell_2 $ en términos de $ v_2 $
# $$
# \ell_2 = \frac{\ell_1 v_1}{v_2}
# $$
# 
# E igualamos las energías en perihelio y afelio
# $$
# \frac{1}{2} v_1^2 - G \frac{M}{\ell_1} = \frac{1}{2} v_2^2 - G \frac{M}{\ell_2}
# $$
# $$
# ⇒\frac{1}{2} v_1^2 - G \frac{M}{\ell_1} = \frac{1}{2} v_2^2 - G \frac{M}{\frac{\ell_1 v_1}{v_2}}
# $$
# $$
# ⇒G \frac{M}{\ell_2} = G \frac{M v_2}{\ell_1 v_1}
# $$
# $$
# ⇒\frac{1}{2} v_1^2 - G \frac{M}{\ell_1} = \frac{1}{2} v_2^2 - G \frac{M v_2}{\ell_1 v_1}
# $$
# 
# Reorganizando  la ecuación
# $$
# ⇒ v_1^2 - \frac{2 G M}{\ell_1} = v_2^2 - \frac{2 G M v_2}{\ell_1 v_1}
# $$
# $$
# ⇒ v_2^2 - \frac{2 G M v_2}{\ell_1 v_1} - v_1^2 + \frac{2 G M}{\ell_1} = 0
# $$
# $$
# ⇒ v_2^2 - \frac{2 G M}{\ell_1 v_1} v_2 - \left( v_1^2 - \frac{2 G M}{\ell_1} \right) = 0
# $$
# 
# Esta es una ecuación cuadrática en $ v_2 $:
# $$
# ⇒v_2^2 - \left( \frac{2 G M}{\ell_1 v_1} \right) v_2 - \left( v_1^2 - \frac{2 G M}{\ell_1} \right) = 0
# $$
# Que coincide con la forma dada:
# $$
# v_2^2 - \frac{2 G M}{v_1 \ell_1} v_2 - \left[ v_1^2 - \frac{2 G M}{\ell_1} \right] = 0
# $$
# 
# $$
# ⇒v_2^2 - A v_2 - B = 0
# $$
# donde
#  $$ A = \frac{2 G M}{v_1 \ell_1} $$ y
#  $$ B = v_1^2 - \frac{2 G M}{\ell_1} $$
# 
# Las raíces son:
# $$
# v_2 = \frac{A \pm \sqrt{A^2 + 4B}}{2}
# $$
# 
# Dado que $ v_2 $ debe ser menor que $ v_1 $ (en el afelio la velocidad es mínima), tomamos la raíz más pequeña.
# $$
# ⇒\ell_2 = \frac{\ell_1 v_1}{v_2}
# $$
# 

# _b_) Dados los valores de $v_1$, $\ell_1$, y $\ell_2$; otros parámetros de la órbita se obtienen mendiante fórmulas simples que pueden derivarse de las leyes de Kepler y del hecho de que la órbita es una elipse:
# $$
# \text{Semieje mayor:} \, a = \frac{1}{2}(\ell_1 + \ell_2),
# $$
# $$
# \text{Semieje menor:} \, b = \sqrt{\ell_1\ell_2},
# $$
# $$
# \text{Período orbital:} \, T = \frac{2\pi ab}{\ell_1v_1},
# $$
# $$
# \text{Excentricidad orbital:} \, e = \frac{\ell_2 - \ell_1}{\ell_2 + \ell_1}.
# $$
# Escribe un programa que le pida al usuario que ingrese la distancia al Sol y la velocidad en el perihelio; para que calcule e imprima las cantidades $\ell_2$, $v_2$, $T$ y $e$.

# In[25]:


# Constantes
G = 6.6738e-11       # Constante gravitacional
M_sol = 1.9891e30    # Masa del Sol

# Pedir datos al usuario
l1 = float(input("Distancia al Sol en el perihelio (m): "))
v1 = float(input("Velocidad en el perihelio (m/s): "))

# Calcular velocidad y distancia en el afelio
A = (2 * G * M_sol) / (v1 * l1)
B = v1**2 - (2 * G * M_sol) / l1

import math
discriminante = A**2 + 4 * B
v2 = (A - math.sqrt(discriminante)) / 2
l2 = (l1 * v1) / v2

# Calcular parámetros orbitales
a = 0.5 * (l1 + l2)                   # Semieje mayor
b = math.sqrt(l1 * l2)                 # Semieje menor
T = (2 * math.pi * a * b) / (l1 * v1)  # Período orbital (segundos)
e = (l2 - l1) / (l2 + l1)             # Excentricidad

# Convertir período a días
T_dias = T / 86400

# Resultados
print(f"Distancia en afelio (l2): {l2:.3e} m")
print(f"Velocidad en afelio (v2): {v2:.3e} m/s")
print(f"Semieje mayor (a): {a:.3e} m")
print(f"Semieje menor (b): {b:.3e} m")
print(f"Período orbital: {T_dias:.2f} días")
print(f"Excentricidad (e): {e:.6f}")


# _c_) Prueba tu programa haciendo que calcule las propiedades de las órbitas de la Tierra (para las cuales $\ell_1 = 1.4710 \times 10^{11} \text{m}$ y $v_1 = 3.0287 \times 10^4 \text{ms}^{-1}$) y del cometa Halley ($\ell_1 = 8.7830 \times 10^{10} \text{m}$ y $v_1 = 5.4529 \times 10^4 \text{ms}^{-1}$). Entre otras cosas, deberías enontrar que el período orbital de la Tierra es de un año y el del cometa Halley es de unos 76 años.

# ### Tierra
# - Distancia al Sol en el perihelio (m):  1.4710e11
# - Velocidad en el perihelio (m/s):  3.0287e4
# - Distancia en afelio (l2): 1.520e+11 m
# - Velocidad en afelio (v2): 2.931e+04 m/s
# - Semieje mayor (a): 1.496e+11 m
# - Semieje menor (b): 1.495e+11 m
# - Período orbital: 365.08 días
# - Excentricidad (e): 0.016472

# ### Halley 
# - Distancia al Sol en el perihelio (m):  8.7830e10
# - Velocidad en el perihelio (m/s):  5.4529e4
# - Distancia en afelio (l2): 5.282e+12 m
# - Velocidad en afelio (v2): 9.067e+02 m/s
# - Semieje mayor (a): 2.685e+12 m
# - Semieje menor (b): 6.811e+11 m
# - Período orbital: 27769.82 días
# - Excentricidad (e): 0.967289
