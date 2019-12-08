from matplotlib import pyplot as plot
from math import *

x = input("Enter the equation with Variable n: ")

def X(n):
    return eval(x)
    
def Y(n):
    if n==0:
        y = -1.5*X(n) +2*X(n+1) -0.5*X(n+2);
        return y
    elif (0<n) and (n<=198):
        y = 0.5*X(n+1) - 0.5*X(n-1);
        return y
    elif n==199:
        y = 1.5*X(n)-2*X(n-1)+0.5*X(n-2);
        return y
    
nrange = list(range(200))
xWithValue = [X(n) for n in nrange]
yWithValue = [Y(n) for n in nrange]

plot.plot(nrange, xWithValue, label = 'x at n')
plot.plot(nrange, yWithValue, label = 'y at n')
plot.legend()
plot.show()