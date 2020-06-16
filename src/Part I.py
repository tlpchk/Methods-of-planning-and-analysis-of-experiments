import scipy.stats as stats
from sympy import integrate, Symbol
from sympy.stats import Binomial, Uniform, density, P, E, variance


def t1():
    print('1')

    n, p = 5, 0.2
    X = Binomial('X', n, p)
    p0 = density(X).dict[0]
    print('a)', p0)

    p2 = P(X > 2)
    print('b)', p2)

    ex = E(X)
    print('c)', ex)


def t2():
    print('2')
    n, p = 1000, 0.002

    print('P(X>=1) = 1 - P(X=0)')

    X = Binomial('X', n, p)
    print('a)', 1 - density(X).dict[0])

    X = stats.poisson(n * p)

    print('b)', 1 - X.cdf(0))


def t3():
    print('3')

    k = (-1, 2, 4, 6)
    A = 1 - 0.2 - 0.4 - 0.3
    pk = (0.2, 0.4, 0.3, A)

    print('a)', f'A = {A}')

    X = stats.rv_discrete(values=(k, pk))
    print('b)', X.expect())
    print('c)', X.var())


def t4():
    print('4')
    x = Symbol('x')

    c = 3 / 4
    f = c * x * (2 - x)

    a = 0
    b = 2

    print("E(X) = ", integrate(f * x, (x, a, b)))

    d = 0.5
    e = 1.0

    print("P(0.5< X <1) = ", integrate(f, (x, d, e)))


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


def t7():
    print('7')

    mu = 3.
    sigma = 2.  # Attention! variance = sigma ^ 2
    N0 = stats.norm(0, 1)

    p = 0
    a = 1 - N0.cdf((p - mu) / sigma)  # P(X>0) = 1 - P(X <= 0)
    print('a)', a)

    p1 = -5
    p2 = 5
    b = N0.cdf((p2 - mu) / sigma) - N0.cdf((p1 - mu) / sigma)  # P( -5 < X < 5)
    print('a2)', b)


def t8():
    print('8')

    X = Uniform(name='X', left=0, right=1)
    Y = Binomial(name='Y', n=10, p=0.5)  # TO JEST POLSKI BERNOULLI JBC

    a = E(2 * X - 3 * Y)
    b = E(X * Y)
    c = variance((3 * Y - X) / 2)

    print(f'a) {a}')
    print(f'b) {b}')
    print(f'c) {c}')


def t9():
    print('9')

    mu = 50.
    sigma = 5.
    N = stats.norm(mu, sigma)

    a = N.ppf(0.1)  # P(T > 0.9) = P(T < 0.1)
    print('a)', a)


def t10():
    print('10')


print('__________________________________')
t1()
print('__________________________________')
t2()
print('__________________________________')
t3()
print('__________________________________')
t4()
print('__________________________________')
t5()
print('__________________________________')
t6()
print('__________________________________')
t7()
print('__________________________________')
t8()
print('__________________________________')
t9()
print('__________________________________')
t10()
