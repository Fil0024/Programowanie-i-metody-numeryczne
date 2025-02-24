import numpy as np

def arctg(x, K):
    if np.abs(x) > 1:
        print("BŁĄD: |x| >= 1")
        return 0
    wynik = 0
    for n in range(K):
        wynik += (-1)**n * x**(2*n +1) / (2*n + 1)
    return 4*wynik

def estimate_pi(K):
    wynik = 4 * arctg(1/5, K) - arctg(1/239, K)
    return wynik
