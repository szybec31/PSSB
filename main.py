from Functions import *
import numpy as np
import matplotlib.pyplot as plt
import cmath
f = 100 #float(input("Podaj częstotliwość sygnału f [MHz]: "))
h_tx = 1#float(input("Wysokość anteny nadawczej h_tx [km]: "))
h_rx = 1#float(input("Wysokość anteny odbiorczej 'Drona' h_tx [km]: "))
r = 10000#float(input("Podaj odległość między nadajnikiem a odbiornikiem r [m]: "))

k = r/1e3

x = np.linspace(0, k, int(r))

#print(x)
y = [Val_F(f, h_tx, h_rx, e) for e in x]


plt.plot(x,y,'o')
#plt.savefig('img/w 1000m.png')
plt.show()
