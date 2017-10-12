#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
def derivative(a,b,n):
    deltax = (b-a)/(n-1)
    D = (np.eye(n,n,1)-np.eye(n,n,-1)) #(np.eye(n)*(-2)+
    D[0][0] = -1
    D[-1][-1] = 1
    dub = np.eye(n)
    dub[0][0] = 2
    dub[-1][-1] = 2
    #print(dub)
    D = (dub@D)/(deltax*2)
    return D

def second_derivative(a,b,n):
    deltax = (b-a)/(n-1)
    D2 = (np.eye(n,n,1)+np.eye(n,n,-1)-2*np.eye(n))
    D2[0][0] = -1
    D2[-1][-1] = -1
    return (D2/(detax**2)

def plot(D,D2,x,f,title):
    """plot(D,x,f) takes four parameters:
    D = the matrix created by derivative(a,b,n)
    x = the x coordinates from a generate function
    f = the y coordinates form a generate function
    titale = string title"""
    dfdx = D @ f
    d2fdx2 = D2 @ f
    plt.plot(x,f)
    plt.plot(x,dfdx)
    plt.plot(x,d2fdx2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend([r'$f$',r'$dfdx$',r'$d^2fdx^2$'])
    #plt.show()

def gen_xsqr_array(a,b,n=1000):
    """gen_xsqr_array(a, b, n=1000)
    Generate a discrete approximation of a x^2 function, including its
    domain and range, stored as a pair of numpy arrays.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, g) : Pair of numpy arrays of float64
            x  : [a, ..., b] Array of n equally spaced float64 between a and b
            g  : [g(a), ..., g(b)] Array of x^2 values matched to x
    """
    def xsqr(x):
        return x**2
    x = np.array(np.linspace(a,b,n), dtype=np.float64)    #Uses linspace to make array of equally spaced coordinates
    fx = np.vectorize(xsqr)
    return (x,fx(x))

def gen_sin_array(a,b,n=1000):
    """gen_sin_array(a, b, n=1000)
    Generate a discrete approximation of a sin function, including its
    domain and range, stored as a pair of numpy arrays.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, g) : Pair of numpy arrays of float64
            x  : [a, ..., b] Array of n equally spaced float64 between a and b
            g  : [g(a), ..., g(b)] Array of sin values matched to x
    """
    def sin(x):
        return np.sin(x)
    x = np.array(np.linspace(a,b,n), dtype=np.float64)    #Uses linspace to make array of equally spaced coordinates
    fx = np.vectorize(sin)
    return (x,fx(x))

def gen_gaus_array(a,b,n=1000):
    """gen_gaus_array(a, b, n=1000)
    Generate a discrete approximation of a gaus function, including its
    domain and range, stored as a pair of numpy arrays.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, g) : Pair of numpy arrays of float64
            x  : [a, ..., b] Array of n equally spaced float64 between a and b
            g  : [g(a), ..., g(b)] Array of gaus values matched to x
    """
    def gaus(x):
        return ((-x**2/2)/(np.sqrt(2*np.pi)))
    x = np.array(np.linspace(a,b,n), dtype=np.float64)    #Uses linspace to make array of equally spaced coordinates
    fx = np.vectorize(gaus)
    return (x,fx(x))