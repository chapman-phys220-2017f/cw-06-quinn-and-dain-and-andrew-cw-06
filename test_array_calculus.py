#!/usr/bin/env python3

import numpy as np
import array_calculus as ac
def test_derivative():
    """Tests derivative(a,b,n) with following tests:
        - derivative(0,9,10) multiplied by f = [0,1,2,3,4,5,6,7,8,9]
    """
    actual = [1,1,1,1,1,1,1,1,1,1]
    trial = ac.derivative(0,9,10)@[0,1,2,3,4,5,6,7,8,9]
    print("Testing: actual ?= trial: ",actual," += ",trial)
    np.testing.assert_almost_equal(actual,trial)
