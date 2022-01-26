import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return np.sin(3*np.pi*x)
def f2(x):
    return np.sin(9*np.pi*x)

x = np.arange(0, 1.001, 1/6)
value1 = []
value2 = [] 
for t in x:
    value1.append(f1(t))
    value2.append(f2(t))
plt.figure().set_size_inches(10,6)
plt.plot(x, value1, label='$k=3$')
plt.plot(x, value2, label='$k=9$')
plt.legend()
plt.savefig('../media/Ex8_15.png', bbox_inches='tight')