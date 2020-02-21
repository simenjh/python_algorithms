import math as m

def guess_number(n):
    acc = 0
    for i in range(m.floor(m.log(n, 2))):
        acc += n - m.floor(n * (1 / (2**(i+1))))
    return acc
