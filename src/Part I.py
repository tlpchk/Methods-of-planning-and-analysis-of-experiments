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

t1()
