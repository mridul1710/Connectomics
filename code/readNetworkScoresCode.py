#### Author: Bisakha Ray, Javier Orlandi and Olav Stetter.


import numpy as np
import scipy

from numpy import *
from scipy import sparse
import scipy.io as sio




def readNetworkScores(filename):
    #% Read the network architecture from the original format as a sparse nxn matrix, 
    #% whose (i,j)th entry indicates neuron i is connected to neuron j 
    #% with a certain strength.
    #% N is the dimension of the scores matrix....if it is not specified it will
    #% be inferred.

    # Load the data
    l1 = np.loadtxt(filename, delimiter=",")
   
    # Keep only 0/1 weights, ignore blocked connections
    size = int(l1.max())
    Matrix = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(len(l1)):
        if l1[i][2] > 0:
            l1[i][2] = 1
            Matrix[int(l1[i][0])-1][int(l1[i][1])-1] = 1
        else:
            l1[i][2] = 0
            Matrix[int(l1[i][0])-1][int(l1[i][1])-1] = 0

    return Matrix




