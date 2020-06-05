import scipy.stats as stats
from sympy.stats import Binomial, Uniform, density, P, E, variance


def t1():
    print('1')

    X = Binomial('X', 5, 0.2)
    p0 = density(X).dict[0]
    print('a)', p0)

    p2 = P(X > 2)
    print('b)', p2)

    ex = E(X)
    print('c)', ex)


def t2():
    print('2')


def t3():
    print('3')


def t4():
    print('4')


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


def t8():
    print('8')

    X = Uniform(name='X', left=0, right=1)
    Y = Binomial(name='Y', n=10, p=0.5) # TO JEST POLSKI BERNOULLI JBC

    a = E(2*X - 3*Y)
    b = E(X * Y)
    c = variance((3*Y - X) / 2)

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
