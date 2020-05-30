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

t1()
t5()