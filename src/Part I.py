import scipy.stats as stats
from sympy.stats import Binomial, density, P, E


def t1():
    print('1')

    X = Binomial('X', 5, 0.2)
    p0 = density(X).dict[0]
    print('a)', p0)

    p2 = P(X > 2)
    print('b)', p2)

    ex = E(X)
    print('c)', ex)


def t5():
    print('5')

    mu = 0.
    sigma = 2.  # Attention! variance = sigma ^ 2
    N = stats.norm(mu, sigma)

    a = N.cdf(0.2) - N.cdf(0)  # P(0 < X < 0.2)
    print('a)', a)

    b = N.cdf(0.5)  # P( X < 0.5)
    print('a)', b)

def t6():
    print(6)

    mu = 2.
    sigma = 3.  # Attention! variance = sigma ^ 2
    N = stats.norm(mu, sigma)
    N0 = stats.norm(0, 1)

    b = N0.ppf(0.95)  # P(X <= 0.95)
    a = b * sigma + mu
    print('a)', a)

    b2 = N0.isf(0.25)  # P(X > 0.25)
    a2 = b2 * sigma + mu
    print('a2)', a2)

def t9():
    print('9')

    mu = 50.
    sigma = 5.
    N = stats.norm(mu, sigma)

    a = N.ppf(0.1)  # P(T > 0.9) = P(T < 0.1)
    print('a)', a)


t1()
t5()
t6()
t9()
