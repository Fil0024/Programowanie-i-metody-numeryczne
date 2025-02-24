import funkcje as f
import time
import sys

if __name__ == '__main__':
    n = int(sys.argv[1])

    start = time.perf_counter_ns()
    print(f.fibi(n))
    print(time.perf_counter_ns() - start)

    start = time.perf_counter_ns()
    print(f.fibr(n))
    print(time.perf_counter_ns() - start)

