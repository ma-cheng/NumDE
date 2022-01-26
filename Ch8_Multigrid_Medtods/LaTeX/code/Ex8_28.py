import numpy as np
import matplotlib.pyplot as plt

def gen_A(n):
    A = np.zeros([n-1, n-1])
    for i in range(n-1):
        for j in range(n-1):
            if i == 0:
                A[i][0] = 2
                A[i][1] = -1
            elif i == n-2:
                A[i][i] = 2
                A[i][i-1] = -1
            else:
                A[i][i] = 2
                A[i][i-1] = A[i][i+1] = -1
    A = A * (n**2)
    return A

def Jacobi(n, w0, omega):
    A = np.eye(n-1) - gen_A(n) * (omega/(2*n**2))
    w0 = -w0
    err = np.linalg.norm(w0, ord=np.inf)
    for i in range(100):
        w0 = np.matmul(A, w0)
        if(np.linalg.norm(w0, ord=np.inf) < err/100):
            return i + 1
    return 100

def Fourier(n, k):
    w = []
    for i in range(1, n):
        w.append(np.sin(i/n*k*np.pi))
    return np.array(w)

k = [i for i in np.arange(1, 64, 1)]
iter_1 = [] # omega = 1
iter_2 = [] # omega = 2/3
for i in k:
    w0 = Fourier(64, i)
    iter_1.append(Jacobi(64, w0, 1))
    iter_2.append(Jacobi(64, w0, 2/3))
plt.figure()
plt.plot(k, iter_1)
plt.xlabel('wavenumber $k$')
plt.ylabel('Iterations')
plt.xticks(range(0,65,16))
plt.yticks(range(0,101,25))
plt.savefig('../media/Ex8_28_a')
plt.figure()
plt.plot(k, iter_2)
plt.xlabel('wavenumber $k$')
plt.ylabel('Iterations')
plt.xticks(range(0,65,16))
plt.yticks(range(0,101,25))
plt.savefig('../media/Ex8_28_b')
