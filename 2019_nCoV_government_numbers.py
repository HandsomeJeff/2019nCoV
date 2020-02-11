# predicted "official" infected and death numbers

from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


# sigmoid for infection
def sigmoid(x, L, x0, k, b):
    y = L / (1 + np.exp(-k*(x-x0))) + b
    return y

yglobal = [282, 314, 581, 846, 1320, 2014, 2798,
           4593, 6965, 7818, 9826, 11953, 14557,
           17391, 20630, 24554, 28276, 31481, 
           34886, 37558, 40554]
ychina = [278, 309, 571, 830, 1297, 1985, 2741,
          4537, 5997, 7736, 9720, 11821, 14411,
          17238, 20471, 24363, 28060, 31211,
          34598, 37251, 40235]


xdata = [x for x in range(21)]

p0 = [max(ychina), np.median(xdata), 1, min(ychina)]


popt, pcov = curve_fit(sigmoid, xdata, ychina, p0, method='dogbox')


L, x0, k, b = popt

print(L, x0, k, b)


# quadratice equation

def f1(x):
    x2 = 123.31
    x1 = -545.83
    c = 905.5

    r = 0.020875

    infected = x2 * x * x + x1 * x + c
    death = infected * r
    
    return death

def f2(x):
    y = L / (1 + np.exp(-k*(x-x0))) + b
    return y

xlist = [i for i in range(30)]
ilist = []
dlist = []

# numbers
for n in xlist:
    if 21 + n <= 31:
        day = (21 + n) % 32
        month = ' January\t'
    else:
        day = (21 + n) % 31
        month = ' February\t'
    infected, deaths = f2(n), f1(n) 
    ilist.append(infected)
    dlist.append(deaths)
    print(str(day) + month + str(infected) + " infected, " + str(deaths) + " dead")
    
# plot
plt.plot(xlist, ilist)
plt.title('days after 21 January')  
plt.show()

plt.plot(xlist, dlist)
plt.title('days after 21 January')  
plt.show()


