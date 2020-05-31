import numpy as np
import scipy.stats as stats


def t3():
    print('3')
    X = [435, 533, 393, 458, 525, 481, 324, 437, 348, 503, 383, 395, 416, 553, 500, 488]
    sigma = 70
    alpha = 0.01

    x_m = np.mean(X)
    n = len(X)

    N = stats.norm(0, 1)
    L = x_m - N.ppf(1 - alpha / 2) * sigma / np.sqrt(n)
    P = x_m + N.ppf(1 - alpha / 2) * sigma / np.sqrt(n)
    print(f'[{L},{P}]')


t3()
