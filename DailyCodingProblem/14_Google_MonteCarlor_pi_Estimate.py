'''
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''


import numpy as np
import matplotlib.pyplot as plt

'''
we have a circle of radius 1, enclosed by a 2 × 2 square. The area of the circle is πr**2=π(1)**2 = π, 
the area of the square is 4. If we divide the area of the circle, by the area of the square we get π/4.

We then generate a large number of uniformly distributed random points and plot them on the graph. 
These points can be in any position within the square i.e. between (-1,-1) and (1,1). 
If they fall within the circle(x2 + y2 = r2), 
they are coloured red, otherwise they are coloured green. 
We keep track of the total number of points, and the number of points that are inside the circle. 
If we divide the number of points within the circle, N_inner by the total number of points, N_total, 
we should get a value that is an approximation of the ratio of the areas we calculated above, π/4.

In other words,

π/4 ≈ Ninner/Ntotal
π ≈4* (Ninner/Ntotal)

When we only have a small number of points, 
the estimation is not very accurate, but when we have hundreds of thousands of points, 
we get much closer to the actual value - to within around 2 decimal places of accuracy.
'''


def MC_pi():
    # pi = 3.141592
    n = 1000000 # number of data points
    #data = np.random.rand(n, 2)  # generate uniform random x,y points b/w [0,1)
    data = np.random.uniform(low=-1, high=1, size=(n,2))
    inside = data[ np.sqrt(data[:,0]**2 + data[:,1]**2) < 1]
    pi =  4* len(inside)/len(data)
    plt.figure(figsize=(8,8))
    plt.scatter(data[:,0], data[:,1], s=.5, c='red')
    plt.scatter(inside[:, 0], inside[:, 1], s=.5, c='green')
    plt.show()
    return pi


if __name__ == '__main__':
    print(MC_pi())