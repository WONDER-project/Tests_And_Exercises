'''
Write a function that calculates a bimodal gaussian function by using numpy arrays as parameters (the abscissas):
populate the ordinate values without cycles on indices
'''
#
import numpy
import matplotlib.pyplot as plt

def gaussian(mu, sigma, x):
    return numpy.exp(-(x-mu)**2/(2*sigma**2)) / numpy.sqrt(2*numpy.pi*(sigma**2))

def bimodal_gaussian(mu1,mu2,sigma1,sigma2,x):
    return gaussian(mu1, sigma1, x) + gaussian(mu2, sigma2, x)

def main():
    mu1 = 1
    mu2 = 2
    sigma1 = 0.1
    sigma2 = 0.04
    x = numpy.arange(0.0, 5.01, 0.01)
    plt.plot(x, bimodal_gaussian(mu1, mu2, sigma1, sigma2, x))
    plt.show()


if __name__=="__main__":
    main()
