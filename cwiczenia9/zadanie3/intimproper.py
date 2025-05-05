import argparse
import numpy as np
import scipy.integrate as integrate

# Dodanie parsera argumentów
parser = argparse.ArgumentParser(description="Obliczanie całek niewłaściwych za pomocą różnych metod")
parser.add_argument("K", type=int, help="Liczba punktów w kwadraturze Gaussa")
parser.add_argument("N", type=int, help="Liczba podprzedziałów dla metody Simpsona")
parser.add_argument("r", type=float, help="Wykładnik r dla pierwszej całki")

args = parser.parse_args()
K = args.K
N = args.N
r = args.r

if N % 2 == 1:
    N += 1  # Simpson needs even
# I1
a1, b1 = 0.0, 1.0
x1 = np.linspace(a1, b1, N + 1)
f1 = lambda x: np.where(x == 0, 0.0, x ** r * np.log(1 / x))
y1 = f1(x1)
I1_simpson = integrate.simpson(y1, x1)
I1_exact = 1.0 / (1.0 + r)
d1 = I1_simpson - I1_exact

# I2: transform x = tan(t), t in (-pi/2, pi/2)
f2_orig = lambda x: np.exp(-x - x ** 2)
t2 = np.linspace(-np.pi / 2, np.pi / 2, N + 1)
x2 = np.tan(t2)
y2 = f2_orig(x2) * (1 / np.cos(t2) ** 2)
I2_simpson = integrate.simpson(y2, t2)
I2_exact = np.sqrt(np.pi) * np.exp(0.25)
# K‑point Gauss on same interval
nodes, weights = np.polynomial.legendre.leggauss(K)
# map [-1,1] -> [-pi/2, pi/2]
t2g = 0.5 * (nodes + 1) * (np.pi) - np.pi / 2
I2_gauss = np.sum(weights * f2_orig(np.tan(t2g)) / np.cos(t2g) ** 2) * (np.pi / 2)

d2_s = I2_simpson - I2_exact
d2_g = I2_gauss - I2_exact

# I3: transform x = tan(t), t in (0, pi/2)
f3_orig = lambda x: np.log(x) / (1 + 100 * x ** 2)
t3 = np.linspace(0, np.pi / 2, N + 1)
x3 = np.tan(t3)
y3 = f3_orig(x3) * (1 / np.cos(t3) ** 2)
I3_simpson = integrate.simpson(y3, t3)
I3_exact = -np.log(10) / 20
# K‑point Gauss on same interval (0,pi/2)
nodes, weights = np.polynomial.legendre.leggauss(K)
t3g = 0.5 * (nodes + 1) * (np.pi / 2)
I3_gauss = np.sum(weights * f3_orig(np.tan(t3g)) / np.cos(t3g) ** 2) * (np.pi / 4)

d3_s = I3_simpson - I3_exact
d3_g = I3_gauss - I3_exact

print(f'*I1 Simpson: {I1_simpson:.10f}, exact: {I1_exact:.10f}, diff: {d1:.2e}')
print(f'*I2 Simpson: {I2_simpson:.10f}, Gauss: {I2_gauss:.10f}, exact: {I2_exact:.10f}')
print(f'   diff Simpson: {d2_s:.2e}, diff Gauss: {d2_g:.2e}')
print(f'*I3 Simpson: {I3_simpson:.10f}, Gauss: {I3_gauss:.10f}, exact: {I3_exact:.10f}')
print(f'   diff Simpson: {d3_s:.2e}, diff Gauss: {d3_g:.2e}')


