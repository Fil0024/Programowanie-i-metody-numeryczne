"""
Należy podać dwa argumenty wywołąnia: N - liczba przedziałów, r - rzeczywisty parametr w całkach.
"""

import argparse
import numpy as np
from scipy.integrate import trapezoid, simpson

def int_trap_ad(f, a, b, N, tol=1e-6):

    if N % 2 != 0:
        N += 1

    x = np.linspace(a, b, N+1)
    y = f(x)

    T = trapezoid(y, x)
    
    S = simpson(y, x)

    E = abs(S - T)

    if E < tol:
        return T, E

    m = 0.5 * (a + b)
    I1, E1 = int_trap_ad(f, a,   m, N//2, tol/2)
    I2, E2 = int_trap_ad(f, m,   b, N//2, tol/2)

    return I1 + I2, E1 + E2


def main():
    parser = argparse.ArgumentParser(
        description="Adaptive composite trapezoid using E_N estimator"
    )
    parser.add_argument("N", type=int, help="początkowa liczba podprzedziałów")
    parser.add_argument("r", type=float, help="parametr r w całkach")
    args = parser.parse_args()
    N, r = args.N, args.r


    integrals = [
        ("I1 = ∫_0^1 cos(r x) dx",
         lambda x: np.cos(r * x), 0.0, 1.0,
         np.sin(r) / r if r != 0 else 1.0),
        ("I2 = ∫_-1^1 r x² dx",
         lambda x: r * x**2,      -1.0, 1.0,
         2 * r / 3),
        ("I3 = ∫_0^1 e^{r x} dx",
         lambda x: np.exp(r * x), 0.0, 1.0,
         (np.exp(r) - 1) / r if r != 0 else 1.0),
    ]

    print(f"\ntrapad: adaptacyjna reguła trapezów z estymatorem E_N")
    print(f"parametry: N = {N}, r = {r}\n")
    print(f"{'Całka':<25} {'I_true':>12} {'I_num':>12} {'E_est':>12} {'ε_true':>12}")
    print("-"*65)

    for name, f, a, b, I_true in integrals:
        I_num, E_est = int_trap_ad(f, a, b, N)
        eps_true = abs(I_true - I_num)
        print(f"{name:<25} "
              f"{I_true:12.8f} "
              f"{I_num:12.8f} "
              f"{E_est:12.2e} "
              f"{eps_true:12.2e}")

if __name__ == "__main__":
    main()
