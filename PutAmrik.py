import math
import numpy as np
sahamawal = 100
k = 100
r = 0.04
sigma = 0.35
T = 0.5
n = 2
deltaT = T/n

akardeltaT = math.sqrt(deltaT)

u = math.exp(sigma * akardeltaT)
d = 1/u
p = (math.exp(r * deltaT) - d) / (u - d)
disc = math.exp(-r * deltaT)

#bangun pohonnya
def AmericanPutTree(u , d , p , disc , sahamawal, k , n):
    #harga saham
    s = np.zeros(n+1)

    for j in range(0, n+1):
        s[j] = sahamawal * u**j * d**(n-j)

    #opsi payoff
    c = np.zeros(n+1)
    for j in range(0,n+1):
        c[j] = max(k - s[j], 0)

    for i in np.arange(n-1 , -1 , -1):
        for j in range(0 , i+1):
            s = sahamawal * u**j * d**(i-j)
            c[j] = disc * (p * c[j+1] + (1-p) * c[j])

            c[j] = max(c[j], k - s)


    return print(f'Harga Opsi dari metode binommial : {c[0]}')

AmericanPutTree(u,d,p,disc,sahamawal,k,50)