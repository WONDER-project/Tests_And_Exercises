import numpy
from scipy import integrate

from orangecontrib.wonder.controller.fit.wppm.wppm_functions import WulffCubeFace, lognormal_distribution, size_function_wulff_solids_lognormal, get_wulff_solid_Hj_coefficients

def Ac(D, L, coefficients):
    #print(D)
    #print(D*coefficients.limit_dist/100)
    D_limit_dist    = D*coefficients.limit_dist/100
    D_limit_dist_xj = D_limit_dist*coefficients.xj
    #print(D_limit_dist_xj)
    def __value_1(coefficients, x):
        return coefficients.a0 + coefficients.b0 * x + coefficients.c0 * (x ** 2) + coefficients.d0 * (x ** 3)

    def __value_2(coefficients, x):
        return coefficients.a1 + coefficients.b1 * x + coefficients.c1 * (x ** 2) + coefficients.d1 * (x ** 3)

    if type(L) == numpy.ndarray:
        result = numpy.zeros(L.size)

        cursor_1 = numpy.where(numpy.logical_and(L >= 0.0,            L <= D_limit_dist_xj)) # TODO: check L=0
        cursor_2 = numpy.where(numpy.logical_and(L > D_limit_dist_xj, L <= D_limit_dist))

        result[cursor_1] = __value_1(coefficients, L[cursor_1]/D)
        result[cursor_2] = __value_2(coefficients, L[cursor_2]/D)

        result[numpy.where(result < 0.0)] = 0.0
        return result
    else:
        if 0.0 <= L <= D_limit_dist_xj:
            return max(0.0, __value_1(coefficients, L/D))
        elif D_limit_dist_xj < L <= D_limit_dist:
            return max(0.0, __value_2(coefficients, L/D))
        else:
            return 0.0

def g(mu, sigma, D):
    return lognormal_distribution(mu, sigma, D)

def Vc(D, truncation):
    return ((D**3)*(1 - (3/2)*truncation**2 + (2/3)*truncation**3))

def size_function_wulff_solids_lognormal_brute_force(h, k, l, truncation, mu, sigma, L, integration_method, face=WulffCubeFace.TRIANGULAR):
    coefficients = get_wulff_solid_Hj_coefficients(h, k, l, truncation, face)
    #print(coefficients)

    Kc = 100/coefficients.limit_dist

    def __numerator(coefficients, mu, sigma, L,integration_method):
        if integration_method == 'quad':
            return integrate.quad(lambda D:  Ac(D, L, coefficients)*g(mu, sigma, D)*Vc(D, truncation), Kc*L, numpy.inf)[0]
        elif integration_method == 'trapz':
            D_0 = numpy.arange(0.1,100,0.1)
            D = D_0**(3)
            Ac_value = numpy.zeros(D.shape)
            for i in range(len(D)):
                Ac_value[i] = Ac(D[i], L, coefficients)
            g_value = numpy.zeros(D.shape)
            for i in range(len(D)):
                g_value[i] = g(mu, sigma,D[i])
            Vc_value = numpy.zeros(D.shape)
            for i in range(len(D)):
                Vc_value[i] = Vc(D[i], truncation)
            return integrate.trapz(Ac_value*g_value*Vc_value,D)



    def __denominator(mu, sigma,integration_method):
        if integration_method == 'quad':
            return integrate.quad(lambda D:  g(mu, sigma, D)*Vc(D, truncation), 0, numpy.inf)[0]
        elif integration_method == 'trapz':
            D_0 = numpy.arange(0.1,100,0.1)
            D = D_0**(3)
            g_value = numpy.zeros(D.shape)
            for i in range(len(D)):
                g_value[i] = g(mu, sigma, D[i])
            Vc_value = numpy.zeros(D.shape)
            for i in range(len(D)):
                Vc_value[i] = Vc(D[i], truncation)
            return integrate.trapz(g_value*Vc_value,D)
        else:
            print('Invalid integration method')
            return 0

    if type(L) == numpy.ndarray:
        numerator = numpy.zeros(L.size)

        for i in range(L.size):
            numerator[i] = __numerator(coefficients, mu, sigma, L[i], integration_method)

        return numerator/__denominator(mu, sigma, integration_method)
    else:
        return __numerator(coefficients, mu, sigma, L, integration_method)/__denominator(mu, sigma, integration_method)

if __name__=="__main__":
    integration_method = 'quad'
    h = 1
    k = 1
    l = 1
    L = numpy.arange(0.0, 1.0, 0.01)

    truncation = 0.
    mu         = 2.0
    sigma      = 0.1

    D_avg = numpy.exp(mu + 0.5*sigma**2)

    print("D_avg", D_avg)

    L *= numpy.ceil(D_avg)*1.5

    from matplotlib import pyplot as plt

    plt.plot(L, size_function_wulff_solids_lognormal_brute_force(h, k, l, truncation, mu, sigma, L, integration_method,face=WulffCubeFace.TRIANGULAR), linewidth=5)
    plt.plot(L, size_function_wulff_solids_lognormal(L, h, k, l, sigma, mu, truncation, WulffCubeFace.TRIANGULAR))
    #plt.show()


