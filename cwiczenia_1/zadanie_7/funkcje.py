def fibi(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a
    
def fibr(n):
    if n < 2:
        return n
    return fibr(n - 1) + fibr(n - 2)