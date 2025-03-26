from Functions import *
import numpy as np
import matplotlib.pyplot as plt
import cmath
f = 500 #float(input("Podaj częstotliwość sygnału f [MHz]: "))
h_tx = 55#float(input("Wysokość anteny nadawczej h_tx [m]: "))
h_rx = 500#float(input("Wysokość anteny odbiorczej 'Drona' h_tx [m]: "))
r = 10000#float(input("Podaj odległość między nadajnikiem a odbiornikiem r [m]: "))
flag = int(input("Czy pomiar wykonac dla idealnej {1}, czy dla zwyklej ziemi {2}?: "))

epsilon_r = 0
sigma = 0

if flag == 2:
    print("Podaj parametry gruntu")
    epsilon_r = float(input("Podaj epsilon_r: "))
    sigma = float(input("Podaj sigma: "))


#x = np.linspace(0, k, int(r))
x = np.linspace(0, r, r)
x = np.round(x,2)
#print(x)
res = np.array([Val_F(f, h_tx, h_rx, e,flag,epsilon_r,sigma) for e in x])
y = res[:,0]
Rd = res[:,1]
#y = np.round(y,5)
print(x)
print("")
print(y)

plt.figure(figsize=(12,6))
plt.plot(x,y)
plt.title('F(d)')
plt.xlabel('Odległość r [m]')
plt.ylabel('Współczynnik propagacji F')
plt.grid()
plt.savefig('img/chart1.png')


y2, fsl = double_F_FSL(y,Rd,f)
y2 = np.abs(y2)
plt.figure(1)
plt.figure(figsize=(12,6))
plt.plot(x,y2,label = "Two-ray model")
plt.plot(x,fsl, label = "Free space model")
plt.title('Porównanie modeli propagacyjnych')
plt.xlabel('Odległość r [m]')
plt.ylabel('Straty propagacyjne [dB]')
plt.legend()
plt.grid()
plt.savefig('img/chart2.png')

plt.show()