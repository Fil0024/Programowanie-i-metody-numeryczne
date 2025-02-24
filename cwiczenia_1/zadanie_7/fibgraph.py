import funkcje as f
import time
import sys
import matplotlib.pyplot as plt    

if __name__ == '__main__':
    N = int(sys.argv[1])

    times_fibi = []
    times_fibr = []
    values_fibi = []
    values_fibr = []
    
    for n in range(N + 1):
        start = time.perf_counter_ns()
        values_fibi.append(f.fibi(n))
        times_fibi.append(time.perf_counter_ns() - start)

        start = time.perf_counter_ns()
        values_fibr.append(f.fibr(n))
        times_fibr.append(time.perf_counter_ns() - start)

    plt.plot(range(N + 1), times_fibi, label='fibi')
    plt.plot(range(N + 1), times_fibr, label='fibr')
    plt.xlabel('Numer wyrazu ciągu Fibonacciego')
    plt.ylabel('Czas obliczeń (ns)')
    plt.title('Zależność czasu obliczeń od numeru wyrazu ciągu Fibonacciego')
    plt.legend()
    plt.savefig('fibtime.svg')
