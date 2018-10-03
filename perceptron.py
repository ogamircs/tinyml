#Perceptron code developed by amircs at October-2014
#This code is only for private use, for any other user contact the author

#simple perceptron
import random, math

#utility functions
def sign(n):
    if n>=0:
        return 1
    else:
        return -1

#training
#TODO: there is a problem with convergence which needs deeps analysis
#I need to add the thershold as w0 and how that works here
#I need to go through the logic to see if there is any update needed
def perceptron_train(data, weights):
    MaxIterations = 10000
    n = len(data)
    ncols = len(data[0])
    
    ther = 0
    res = [0 for x in xrange(n)]
    for x in range(0, MaxIterations):
        for i in range(n):
            #run perceptron
            res[i] = 0
            for j in range(ncols-1):
                res[i] = res[i] + weights[j]*data[i][j];
            
            #misclassification
            if sign(res[i]) != sign(data[i][ncols-1]):
                #adjust the weights
                for j in range(ncols-1):
                    weights[j] = weights[j] + data[i][j]*data[i][ncols-1]
        
        #check to see if the algorithm is finished
        if perceptron_test(data, weights) < 1:
            return (x+1)
    return MaxIterations


#runs perceptron for one row                    
def perceptron_run(data, weights):
    res = 0
    ncols = len(data)
    for i in range(ncols-1):
            res = res + weights[i]*data[i];
    return sign(res)
    
def perceptron_test(data, weights):
    n = len(data)
    ncols = len(data[0])
    error = 0
    for k in range(n):
        error = error + abs( sign(data[k][ncols-1]) - perceptron_run(data[k], weights))
    return error/math.floor(n);
    
def XOR(x,y):
    if sign(x) == sign(y):
        return 1;
    else:
        return -1;
    
def main():
    #sample size
    n = 100
    ncols = 4	
    #the generated data should be a linearly seperable function
    data = [[0 for x in xrange(ncols)] for x in xrange(n)]
    resultset = [1 for x in range(2)]
    resultset[0] = -1
    for i in range(n):
        for j in range(ncols-1):
            if j==0:
                data[i][j] = -1
            data[i][j] = resultset[random.randint(0,1)]
        #unkown function for perceptron to find
        data[i][ncols-1] = XOR(data[i][1],data[i][2])
    
    #print data
    #for i in range(n):
    #    print "input data is "
    #    for j in range(ncols):
    #        print data[i][j]
    
    weights = [0 for x in xrange(ncols-1)]
    
    print "training started ..."
    numiter = perceptron_train(data, weights)
    print "done iters = " + str(numiter)
    print weights
    print "scoring ..."
    error = perceptron_test(data, weights)
    print "overall error is " + str(error)
    
    
if __name__ == "__main__":
    main()
