from Functions import *
import numpy as np
import matplotlib.pyplot as plt
import cmath
f = 100 #float(input("Podaj częstotliwość sygnału f [MHz]: "))
h_tx = 35#float(input("Wysokość anteny nadawczej h_tx [m]: "))
h_rx = 500#float(input("Wysokość anteny odbiorczej 'Drona' h_tx [m]: "))
r = 10000#float(input("Podaj odległość między nadajnikiem a odbiornikiem r [m]: "))


#x = np.linspace(0, k, int(r))
x = np.linspace(0, r, r)
x = np.round(x,2)
#print(x)
y = np.array([Val_F(f, h_tx, h_rx, e) for e in x])


#y = np.round(y,5)
print(x)
print("")
print(y)

plt.figure(figsize=(12,6))
plt.plot(x,y)
plt.title('')
plt.xlabel('Odległość r [m]')
plt.ylabel('F')
#plt.savefig('img/w 1000m.png')


y2 = double_F_FSL(y,x,f)
y2 = np.abs(y2)
plt.figure(1)
plt.figure(figsize=(12,6))
plt.plot(x,y2)
plt.title('')
plt.xlabel('Odległość r [m]')
plt.ylabel('F^2 * FSL')

plt.show()