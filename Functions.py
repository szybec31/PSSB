from cmath import log10
import numpy as np
import cmath

def FSL(f,d):
    res = 32.44+20*log10(f)+20*log10(d)
    watt = 10**(res/10)
    return watt


def delta_R(h_tx, h_rx, r):
    r_km = r / 1000  # Odległość między nadajnikiem a odbiornikiem r w [km]
    k = 4/3  # Współczynnik refrakcji
    r0 = 6375  # Promień Ziemi r0 [km]

    re = k * r0  # Promień wyimaginowanej Ziemi

    p = (2/np.sqrt(3)*np.sqrt(re*(h_tx + h_rx)+(r_km**2)/4))
    ksi = np.asin(np.clip((2 * re * r_km * (h_tx - h_rx)) / p ** 3,-1, 1))

    r1 = r_km / 2 - p * np.sin(ksi / 3)

    r2 = r_km - r1

    fi1 = r1 / re
    fi2 = r2 / re

    R1 = np.sqrt(h_rx ** 2 + 4 * re * (re + h_rx) * np.sin(fi1 / 2) ** 2)
    R2 = np.sqrt(h_tx ** 2 + 4 * re * (re + h_tx) * np.sin(fi2 / 2) ** 2)
    Rd = np.sqrt((h_tx - h_rx) ** 2 + 4 * (re + h_tx) * (re + h_rx) * np.sin((fi1 + fi2) / 2) ** 2)

    #print(r, R1, R2)
    x = h_tx / R1 - (R1 / (2 * re))
    print(x)
    if x < -1:
        print(x, r)
        x = -1
    if x > 1:
        print(x, r)
        x = 1
    psi_g = np.asin(x)

    deltaR = 4 * R1 * R2 * (np.sin(psi_g)**2) / (R1 + R2 + Rd)

    #print(deltaR)
    return deltaR

def Val_F(f,h_tx, h_rx, r):
    lamb = 300 / f / 1000
    deltaR = delta_R(h_tx, h_rx, r)

    deltaFI = 2 * cmath.pi / lamb * deltaR
    #print(deltaFI)

    F = abs(1 - np.exp(1j * deltaFI))
    #print(F)
    return F