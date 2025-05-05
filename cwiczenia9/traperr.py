import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid, simpson

def composite_trapezoid(f, a, b, N):
    """Złożona reguła trapezów na N podprzedziałach."""
    x = np.linspace(a, b, N+1)
    y = f(x)
    return trapezoid(y, x)

def composite_simpson(f, a, b, N):
    """Złożona reguła Simpsona na N podprzedziałach (N musi być parzyste)."""
    if N % 2 != 0:
        raise ValueError(f"Simpson wymaga, by N było parzyste, a dostałem N={N}")
    x = np.linspace(a, b, N+1)
    y = f(x)
    return simpson(y, x)

def main():
    # --- Wczytanie argumentu K ---
    parser = argparse.ArgumentParser(description="Sprawdzenie estymatora błędu trapezów")
    parser.add_argument("K", type=int, help="maksymalna liczba podprzedziałów N")
    args = parser.parse_args()
    K = args.K

    # --- Definicje całek ---
    integrals = [
        {
            "name": r"$\int_0^1 e^{-x^2}\,dx$",
            "f": lambda x: np.exp(-x**2),
            "a": 0.0, "b": 1.0,
            "exact": 0.7468241328124271
        },
        {
            "name": r"$\int_0^{\pi}\sin(x)\,dx$",
            "f": np.sin,
            "a": 0.0, "b": np.pi,
            "exact": 2.0
        },
        {
            "name": r"$\int_1^2 \ln(x)\,dx$",
            "f": np.log,
            "a": 1.0, "b": 2.0,
            "exact": 2*np.log(2) - 1
        }
    ]

    for I in integrals:
        f, a, b, Iexact = I["f"], I["a"], I["b"], I["exact"]
        Ns = np.arange(1, K+1)
        E = np.full_like(Ns, fill_value=np.nan, dtype=float)
        epsT = np.full_like(Ns, fill_value=np.nan, dtype=float)

        for idx, N in enumerate(Ns):
            S_T = composite_trapezoid(f, a, b, N)
            epsT[idx] = abs(Iexact - S_T)

            if N % 2 == 0:
                S_S = composite_simpson(f, a, b, N)
                E[idx] = abs(S_S - S_T)

        delta = E - epsT

        plt.figure()
        plt.plot(Ns, delta, marker='o', linestyle='-')
        plt.axhline(0, color='k', linewidth=0.8)
        plt.title(r"$\delta(N) = E_N - \varepsilon_N^T$ dla " + I['name'])
        plt.xlabel("Liczba podprzedziałów N")
        plt.ylabel(r"$\delta(N)$")
        plt.grid(True)
        plt.tight_layout()

    # --- pokaz wszystkie wykresy ---
    plt.show()

if __name__ == "__main__":
    main()
