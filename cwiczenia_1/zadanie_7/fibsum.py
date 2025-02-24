import funkcje as f
import time

if __name__ == '__main__':  
    start = time.perf_counter_ns()
    n=1
    sum=0
    while f.fibi(n)<3*10**6:
        sum+=f.fibi(n)
        n+=1
    print(sum)
    print("czas wykonania: ",(time.perf_counter_ns() - start)/10**9,"s")

    start = time.perf_counter_ns()
    n=1
    sum=0
    while f.fibr(n)<3*10**6:
        sum+=f.fibr(n)
        n+=1
    print(sum)
    print("czas wykonania: ",(time.perf_counter_ns() - start)/10**9,"s")