from cmath import log10
import numpy as np
import cmath


# epsilon_r, mi_r To są wartości względne

def reflection(epsilon_r, sigma, f, theta):
    theta = np.pi/2 - theta
    mi_r = 1
    epsilon0 = 8.854e-12     # przenikalność elektryczna próżni
    mi0 = 4 * cmath.pi * 1e-7    # przenikalność magnetyczna próżni
    n0 = 377 # impedancja falowa próżni

    omega = 2 * cmath.pi * (f * 1e6)   # pulsacja
    eps = epsilon0 * epsilon_r           # przenikalność elektryczna Ziemi
    mi = mi0 * mi_r                    # prenikalność magnetyczne Ziemi

    n1 = cmath.sqrt((1j*omega*mi)/(sigma + 1j * omega * eps))
    theta_t = np.asin(np.sqrt(1/(mi_r*epsilon_r))*np.sin(theta))

    wsp_odb = (n1*np.cos(theta_t)-n0*np.cos(theta))/(n1*np.cos(theta_t)+n0*np.cos(theta))
    print(abs(wsp_odb))

    return wsp_odb


def FSL(f,d):
    if d == 0:
        return 0
    res = -27.55+20*np.log10(f)+20*np.log10(d)
    #print(res)
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
        #print(x, r)
        x = -1
    if x > 1:
        #print(x, r)
        x = 1

    psi_g = np.asin(x)
    deltaR = 4 * R1 * R2 * (np.sin(psi_g)**2) / (R1 + R2 + Rd)
    return deltaR,psi_g,Rd

def Val_F(f,h_tx, h_rx, r,flag,epsilon_r,sigma):
    lamb = 300 / f
    #print(r)
    deltaR, psi_g, Rd = delta_R(h_tx, h_rx, r)

    deltaFI = 2 * cmath.pi / (lamb * deltaR)
    #print(deltaR,deltaFI)

    if flag == 1:
        F = abs(1 - np.exp(1j * deltaFI))
    elif flag == 2:
        wsp = reflection(epsilon_r, sigma, f, psi_g)
        print(wsp)
        F = abs(1 + wsp * np.exp(1j * deltaFI))
    return F, Rd

def double_F_FSL(y,Rd,f):
    fsl = np.array([FSL(f,e) for e in Rd])
    ww_fsl = np.array([pow(10,x/10) for x in fsl])
    f_double = np.pow(y, 2)

    result = ww_fsl * f_double
    result = 10*np.log10(result)
    print(result)
    return result, fsl