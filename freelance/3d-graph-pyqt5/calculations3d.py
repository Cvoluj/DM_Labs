import math
import numpy as np

constants = {
    "Сталь": {
        "sigma_0": 0.135*pow(10,7),
        "lamda": 0.167*pow(10,2),
        "k": 0.442*pow(10,-5)
        },

    "Мідь": {
        "sigma_0": 0.588*pow(10,8),
        "lamda": 0.406*pow(10,3),
        "k": 0.118*pow(10,-3)
        },

    "Алюміній": {
        "sigma_0": 0.363*pow(10,8),
        "lamda": 0.209*pow(10,3),
        "k": 0.847*pow(10,-4)
        }
}

def get_plot_values(metal, delta0, Bi, H_0, h, d, n):
    count = 50
    def t(n):
        return (n*2*math.pi)/omega

    def T1(F0):
        return T0 * ((1 / a1) * (1 - math.exp(-a1 * F0)) - (2 / (a1 - B1)) * (
                    math.exp(-B1 * F0) - math.exp(-a1 * F0)) + (
                                 1 / (a1 - 2 * B1) * (math.exp(-2 * B1 * F0) - math.exp(-a1 * F0))))

    def T(x1, x3, F0):
        term1 = (1 + (1 / 3) * R_star1) - (R_star1 * pow(x1, 2))
        term2 = (1 + (1 / 3) * R_star1) - (R_star1 * pow(x3, 2))
        return T1(F0) * term1 * term2

    if metal not in constants.keys():
        return None

    sigma_0, lamda, k = constants[metal].values()
    mu = 0.000001257
    b = 1/2*pow(sigma_0, 2)
    omega =(1)/(2*pow(delta0,2)*sigma_0*mu*pow(h,2))

    R_star8 = 36 + 18*Bi + 2 * pow(Bi,2)
    R_star1 = (18*Bi + 3 * pow(Bi,2))/R_star8

    t_out = 2*math.pi*n/omega
    F_out = 4*math.pi*n*k*sigma_0 * mu
    F0 =F_out
    T0 = (pow(H_0,2)/(sigma_0 * lamda)) * (27/8) * (((d/2) + (pow(d,3)/5) + (8/15*d))* pow(b,2))/(9*pow((1+1/pow(d,2)),2)+pow(b,2))
    a1 = (36*Bi + 6* pow(Bi,2))/(18+ 9*Bi + pow(Bi,2))
    B1 = pow(h,2)*6.9/t_out * k

    x1 = np.linspace(-d, d, count)
    x2 = np.linspace(-h, h, count)
    X1, X2 = np.meshgrid(x1,x2)
    Z = T(X1, X2, F0)

    return X1, X2, Z
