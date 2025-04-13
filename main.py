from Functions import *
import numpy as np
import matplotlib.pyplot as plt
import cmath
print("Szymon Bęczkowski 273179 - Temat 5.")
print("Model dwupromieniowy dla kulisej Ziemi")
f = float(input("Podaj częstotliwość sygnału f [MHz]: "))                       # 500 MHz
h_tx = float(input("Wysokość anteny nadawczej h_tx [m]: "))                     # 55 m
h_rx = float(input("Wysokość anteny odbiorczej 'Drona' h_tx [m]: "))            # 500 m
r = int(input("Podaj odległość między nadajnikiem a odbiornikiem r [m]: "))     # 10000 m
flag = int(input("Czy pomiar wykonac dla idealnej {1}, czy dla zwyklej ziemi {2}?: "))

epsilon_r = 0
sigma = 0

if flag == 2:
    print("Podaj parametry gruntu:")
    epsilon_r = float(input("Podaj epsilon_r [F/m]: "))       # 15
    sigma = float(input("Podaj sigma [S/m]: "))               # 0.01


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
plt.title('Wartość współczynnika propagacji F w zależności od odległości r')
plt.xlabel('Odległość r [m]')
plt.ylabel('Współczynnik propagacji F')
plt.grid()
plt.savefig('wykres1_wsp.png')


y2, fsl = double_F_FSL(y,Rd,f)
#y2 = np.abs(y2)
plt.figure(1)
plt.figure(figsize=(12,6))
plt.plot(x,y2,label = "Two-ray model")
plt.plot(x,-fsl, label = "Free space model")
plt.title('Porównanie modeli propagacyjnych')
plt.xlabel('Odległość r [m]')
plt.ylabel('Poziom Sygnału [dB]')
plt.legend()
plt.grid()
plt.savefig('wykres2_straty.png')

plt.show()