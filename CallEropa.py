import math
import numpy as np
import scipy.stats as st
sahamawal = 50
k = 50
r = 0.05
sigma = 0.3
T = 1
n = 250
deltaT = T/n

u = math.exp(sigma * math.sqrt(deltaT))
d = 1/u
p = (math.exp(r * deltaT) - d) / (u - d)
disc = math.exp(-r * deltaT)

def EuropeanCallTree(u, d , p, sahamawal , disc, k , n):
    #harga saham
    s = np.zeros(n+1)
    for j in range(0 , n+1):
        s[j] = sahamawal * u**j * d**(n-j)

    #opsi payoff
    c = np.zeros(n+1)
    for j in range(0 , n+1):
        c[j] = max(s[j] - k , 0)

    for i in np.arange(n , 0 , -1):
        for j in range(0 , i):
            c[j] = disc * (p * c[j+1] + (1-p) * c[j])

    return print(f'Harga Opsi dari metode binomial : {c[0]}')

def BlackScholesMerton(sahamawal , k , r, T, sigma ):
    d1 = (math.log(sahamawal / k) + (r + 0.5 * (sigma * sigma)) * T) / sigma * math.sqrt(T)
    d2 = d1 - sigma * math.sqrt(T)

    result = sahamawal * st.norm.cdf(d1) - k * math.exp(-r * T) * st.norm.cdf(d2) 

    return print(f'Harga Opsi dari metode Black-Scholes Merton : {result}')

EuropeanCallTree(u , d ,p, sahamawal , disc, k , n)
BlackScholesMerton(sahamawal , k , r , T , sigma)