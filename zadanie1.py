import numpy as np
import pandas as pd
from scipy.integrate import trapezoid, simpson, fixed_quad

def main():
    integrals = [
        {
            "name": r"$\int_0^1 e^{-x^2}\,dx$",
            "func": lambda x: np.exp(-x**2),
            "a": 0.0,
            "b": 1.0,
            "exact": 0.7468241328124271
        },
        {
            "name": r"$\int_0^{\pi} \sin(x)\,dx$",
            "func": np.sin,
            "a": 0.0,
            "b": np.pi,
            "exact": 2.0
        },
        {
            "name": r"$\int_1^2 \ln(x)\,dx$",
            "func": np.log,
            "a": 1.0,
            "b": 2.0,
            "exact": 2*np.log(2) - 1
        }
    ]

    N = 1000        
    n_gauss = 5     

    records = []
    for I in integrals:
        f, a, b, exact = I["func"], I["a"], I["b"], I["exact"]
        x = np.linspace(a, b, N+1)
        y = f(x)

        # trapezów: scipy.integrate.trapezoid
        I_trap   = trapezoid(y, x)
        # Simpsona 1/3
        I_simp   = simpson(y, x)
        # Gauss–Legendre
        I_gauss, _ = fixed_quad(f, a, b, n=n_gauss)

        records.append({
            "Całka": I["name"],
            "Dokładna": exact,
            "Trapezoid": I_trap,
            "Błąd (trapezoid)": abs(I_trap - exact),
            "Simpson": I_simp,
            "Błąd (Simpson)": abs(I_simp - exact),
            f"Gauss (n={n_gauss})": I_gauss,
            f"Błąd (Gauss)": abs(I_gauss - exact)
        })

    # --- Wyświetlenie wyników ---
    df = pd.DataFrame(records)
    pd.set_option('display.float_format', '{:12.8f}'.format)
    print("\nPorównanie metod kwadratury dla wybranych całek:\n")
    print(df.to_string(index=False))

if __name__ == "__main__":
    main()
