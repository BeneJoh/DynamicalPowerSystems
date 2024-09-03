import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eig


def smib_eigenvals(M, D, P, K):
    A = np.array([[0, 1], [-K/M, -D/M]])
    eigvals, eigvecs = eig(A)
    return eigvals


# realistic
M = 0.4; D = 20; P = 5; K = 400.0

def fun(M, D, P, K): 
    return (-D/(2*M) - np.sqrt(0j+D**2 - 4*K*M)/(2*M), -D/(2*M) + np.sqrt(0j+D**2 - 4*K*M)/(2*M)) # stable
eigvals = smib_eigenvals(M, D, P, K)



Ds = np.linspace(0, 40, 200)

ls =[fun(M, D, P, K) for D in Ds]
l1s = [l[0] for l in ls]
l2s = [l[1] for l in ls]
plt.plot(np.real(l1s), np.imag(l1s), '1', color='red', label=r'$\lamba_1$') 
plt.plot(np.real(l2s), np.imag(l2s), '2', color='blue', label=r'$\lamba_2$')
plt.xlabel(r'Re $\lambda$')
plt.ylabel(r'Im $\lambda$')
plt.savefig('smib_eigenvals.png', dpi=300, bbox_inches='tight')
plt.show()