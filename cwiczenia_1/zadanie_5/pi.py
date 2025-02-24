import my_functions as my   
import sys
import matplotlib.pyplot as plt
import numpy as np

N = int(sys.argv[1])

values_pi = []
for n in range(1, N + 1):
    values_pi.append(my.estimate_pi(n))

plt.plot(range(1, N + 1), values_pi)
plt.axhline(y = np.pi, color = 'r', linestyle = '--')
plt.xlabel('Liczba iteracji')   
plt.ylabel('Wartość przybliżenia π')
plt.title(my.estimate_pi(N))
plt.savefig('pi.svg')
