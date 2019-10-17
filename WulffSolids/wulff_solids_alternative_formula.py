#changes
import numpy
from scipy.special import erfc

from orangecontrib.wonder.controller.fit.wppm.wppm_functions import WulffCubeFace, size_function_wulff_solids_lognormal, get_wulff_solid_Hj_coefficients

from WulffSolids.binayak_1 import size_function_wulff_solids_lognormal_brute_force

def size_function_wulff_solids_lognormal_new(L, h, k, l, sigma, mu, truncation, face):

    def M_ln(mu, sigma2, n):
        return numpy.exp((n*mu) + (0.5*sigma2*n**2))

    def __FFourierLognormal(poly_coefficients, L, Kc, mu, sigma2, ssqrt2, M_l3, is_array):
        if is_array:
            A = numpy.zeros(len(L))
        else:
            A = 0.0

        for n in range(4):
            A += poly_coefficients[n] * erfc((numpy.log(L*Kc)-mu-((3.0-n)*sigma2))/ssqrt2) * (L**n) * 0.5 * M_ln(mu, sigma2, 3-n) / M_l3

        if is_array:
            A[numpy.where(A <= 1e-20)] = 0.0
        else:
           if A <= 1e-20: A = 0.0

        return A

    is_array = isinstance(L, list) or isinstance(L, numpy.ndarray)

    if not is_array and L==0: return 1.0

    sigma2 = sigma*sigma
    ssqrt2 = sigma*numpy.sqrt(2.0)
    M_l3     = M_ln(mu, sigma2, 3)

    coefficients = get_wulff_solid_Hj_coefficients(h, k, l, truncation, face)
    print(coefficients)


    Kc = 100.0 / coefficients.limit_dist

    poly_coefficients = numpy.array([coefficients.aa, coefficients.bb, coefficients.cc, coefficients.dd])
    fourier_amplitude = __FFourierLognormal(poly_coefficients, L * Kc, 1.0, mu, sigma2, ssqrt2, M_l3, is_array)

    if is_array:
        fourier_amplitude[numpy.where(L == 0.0)] = 1.0
        fourier_amplitude[numpy.where(fourier_amplitude < 0.0)] = 0.0
        fourier_amplitude[numpy.where(fourier_amplitude > 1.0)] = 1.0
        fourier_amplitude[2:][numpy.where(numpy.greater(fourier_amplitude[2:], fourier_amplitude[1:-1]))] = 0
    else:
        if fourier_amplitude > 1.0 : return 1.0
        if fourier_amplitude < 0.0 : return 0.0
        #check the previous

    return fourier_amplitude

if __name__=="__main__":
    integration_method = 'trapz'
    h = 1
    k = 1
    l = 1
    L = numpy.arange(0.0, 1.0, 0.01)

    truncation = 0.3
    mu         = 2.0
    sigma      = 0.1

    D_avg = numpy.exp(mu + 0.5*sigma**2)

    print("D_avg", D_avg)

    L *= numpy.ceil(D_avg)*1.5

    from matplotlib import pyplot as plt

    plt.plot(L, size_function_wulff_solids_lognormal_brute_force(h, k, l, truncation, mu, sigma, L, integration_method, face=WulffCubeFace.TRIANGULAR), linewidth=10, label = 'brute force')
    plt.plot(L, size_function_wulff_solids_lognormal(L, h, k, l, sigma, mu, truncation, WulffCubeFace.TRIANGULAR), linewidth=5, label = 'analytical')
    plt.plot(L, size_function_wulff_solids_lognormal_new(L, h, k, l, sigma, mu, truncation, WulffCubeFace.TRIANGULAR), label = 'new analytical')
    plt.legend()
    plt.show()
