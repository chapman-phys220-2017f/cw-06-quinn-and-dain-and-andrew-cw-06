#!/usr/bin/env python3

import numpy as np
def derivative(a,b,n):
    deltax = (b-a)/(n-1)
    D = (np.eye(n)*(-2)+np.eye(n,n,1)+np.eye(n,n,-1))/(deltax**2)
    return D
