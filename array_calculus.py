#!/usr/bin/env python3

import numpy as np
def derivative(a,b,n):
    deltax = (b-a)/(n-1)
    D = (np.eye(n,n,1)-np.eye(n,n,-1)) #(np.eye(n)*(-2)+
    D[0][0] = -1
    D[-1][-1] = 1
    dub = np.eye(n)
    dub[0][0] = 2
    dub[-1][-1] = 2
    print(dub)
    D = (dub@D)/(deltax*2)
    return D
