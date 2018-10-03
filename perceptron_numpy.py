#Perceptron code developed by amircs at October-2014
#This code is only for private use, for any other user contact the author

#simple perceptron
import numpy as np
import random, math

#training
def perceptron_train(data, weights, n, ncols):
    counter = 0
    while True:
        data[:, 4] = -1.0
        data[data[:, 0]*weights[0] + data[:, 1]*weights[1] + weights[2] >= 0, 4] = 1.0
        misConfig = np.arange(0, n)[data[:, 3] != data[:, 4]]
        if not misConfig.size:
            break
        i = random.choice(misConfig)
        weights += np.array([data[i,3] * 3]) * np.array([data[i, 0], data[i, 1], 1])
        counter += 1
    return counter
    
def main():
    #sample size
    n = 100
    ncols = 5

    #the generated data should be a linearly seperable function
    data = np.zeros((n, ncols), float)
    data[:, 0:2] = np.random.uniform(-1.0, 1.0, (n, 2))
    x1, y1 = -1.0, random.uniform(-1.0, 1.0)
    x2, y2 = 1.0, random.uniform(-1.0, 1.0)
    b = (y2 + y1)/2.0
    a = (y2 - y1)/2.0
    f = (a, b, (x1, x2), (y1, y2))

    #put all targets at -1
    data[:, 3] = -1.0
    #only make the one that have this condition to 1
    data[data[:, 1] >= f[0]*data[:, 0] + f[1], 3] = 1.0
    
    #print data
    
    weights = np.zeros(3)
    #weights = [0 for x in xrange(ncols-1)]
    
    print "training started ..."
    numiter = 0.0
    experiment_num = 10

    for i in range(0,experiment_num):
        numiter += perceptron_train(data, weights, n, ncols)
    print "avg iters = " + str(numiter/experiment_num)
    
    
if __name__ == "__main__":
    main()
