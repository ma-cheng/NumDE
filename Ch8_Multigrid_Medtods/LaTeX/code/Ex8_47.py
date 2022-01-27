import numpy as np
import matplotlib.pyplot as plt

class TG:
    def __init__(self, n, omega):
        self.n = n
        self.omega = omega
        
    def s(self, k):
        return (np.sin(k*np.pi/2/self.n))**2

    def c(self, k):
        return 1 - self.s(k)

    def lamb(self, k):
        return 1 - 2*self.omega*self.s(k)

    def plot(self, v1, v2):
        k1 = np.arange(0, self.n/2, 0.1)
        k2 = np.arange(self.n/2, self.n, 0.1)
        c1, c2, c3, c4 = [], [], [], []
        for k in k1:
            c1.append(np.power(self.lamb(k), v1+v2)*self.s(k))
            c3.append(np.power(self.lamb(self.n-k), v1)*np.power(self.lamb(k), v2)*self.c(k))
        for k in k2:
            c2.append(np.power(self.lamb(k), v1+v2)*self.s(k))
            c4.append(np.power(self.lamb(self.n-k), v1)*np.power(self.lamb(k), v2)*self.c(k))
        plt.figure()
        plt.title("$\\nu_1 = {v1},\ \\nu_2 = {v2}$".format(v1 = str(v1), v2 = str(v2)), fontsize = 15)
        plt.plot(k1, c1, k2, c2, k1, c3, k2, c4)
        plt.legend(['$c_1$', '$c_2$', '$c_3$', '$c_4$'], fontsize = 10)
        return plt.gcf()

def main():
    myTG = TG(64, 2/3)
    myTG.plot(0, 0)
    plt.savefig('../media/Ex8_47_00')
    myTG.plot(0, 2)
    plt.savefig('../media/Ex8_47_02')
    myTG.plot(1, 1)
    plt.savefig('../media/Ex8_47_11')
    myTG.plot(2, 0)
    plt.savefig('../media/Ex8_47_20')
    myTG.plot(2, 2)
    plt.savefig('../media/Ex8_47_22')
    myTG.plot(4, 0)
    plt.savefig('../media/Ex8_47_40')

if __name__ == '__main__':
    main()