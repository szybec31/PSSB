from cmath import log10
import numpy as np
import cmath



def reflection(epsilon_r, sigma, f, theta):
    epsilon0 = 8.854*pow(10,-12)
    complex_permittivity = epsilon_r * np.exp(-1j *sigma/(epsilon0*2*cmath.pi*f))


def FSL(f,d):
    if d == 0:
        return 0
    res = -27.55+20*log10(f)+20*log10(d)
    return res


def delta_R(h_tx, h_rx, r):
    r_km = r   # Odległość między nadajnikiem a odbiornikiem r w [m]
    k = 4/3  # Współczynnik refrakcji
    r0 = 6375000  # Promień Ziemi r0 [m]

    re = k * r0  # Promień wyimaginowanej Ziemi
    re = round(re,2)

    p = (2/np.sqrt(3))*np.sqrt(re*(h_tx + h_rx)+(r_km**2)/4)
    p = round(p,2)
    ksi = np.asin((2 * re * r_km * (h_tx - h_rx)) / p**3)



    r1 = r_km / 2 - p * np.sin(ksi / 3)
    r2 = r_km - r1
    r1 = round(r1, 2)
    r2 = round(r2, 2)


    fi1 = r1 / re
    fi2 = r2 / re


    R1 = np.sqrt(h_rx ** 2 + 4 * re * (re + h_rx) * np.sin(fi1 / 2) ** 2)
    R2 = np.sqrt(h_tx ** 2 + 4 * re * (re + h_tx) * np.sin(fi2 / 2) ** 2)
    Rd = np.sqrt((h_tx - h_rx) ** 2 + 4 * (re + h_tx) * (re + h_rx) * np.sin((fi1 + fi2) / 2) ** 2)

    R1 = round(R1,2)
    R2 = round(R2, 2)
    Rd = round(Rd, 2)

    #print(r, R1, R2)
    x = h_tx / R1 - (R1 / (2 * re))
    #print(x)

    if x < -1:
        print(x, r)
        x = -1
    if x > 1:
        print(x, r)
        x = 1



    psi_g = np.asin(x)

    deltaR = 4 * R1 * R2 * (np.sin(psi_g)**2) / (R1 + R2 + Rd)
    return deltaR

def Val_F(f,h_tx, h_rx, r):
    lamb = 300 / f
    #print(r)
    deltaR = delta_R(h_tx, h_rx, r)

    deltaFI = 2 * cmath.pi / (lamb * deltaR)
    print(deltaR,deltaFI)

    F = abs(1 - np.exp(1j * deltaFI))
    #print(F)
    return F

def double_F_FSL(y,x,f):
    fsl = np.array([FSL(f,e) for e in x])
    ww_fsl = np.array([pow(10,x/10) for x in fsl])
    f_double = np.pow(y, 2)

    result = ww_fsl * f_double

    return result