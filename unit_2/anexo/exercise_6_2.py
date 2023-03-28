import random
import datetime
import math
from scipy.stats import norm
from scipy.integrate import quad
import numpy as np

# Seed number for the random number generator reproducibility
SEED_NUMBER = 50826476
random.seed(SEED_NUMBER)


def F(x1, x2, x3, x4, x5): return x1 * x2 ** 2 * x3 ** 3 * x4 ** 4 * x5 ** 5


# Experiment parameters
SAMPLE = 1000000
DELTA = 0.05
EPSILON = 0.0001
i_norm = norm.ppf
i_norm_95 = i_norm(1 - DELTA/2)
i_norm_90 = i_norm(1 - 0.1/2)
i_norm_99 = i_norm(1 - 0.01/2)


def main():
    start_time = datetime.datetime.now()
    (Int_, Var_Int_, IC_Normal, Var_F) = montecarlo_simulation(n=SAMPLE)
    elapsed_time = datetime.datetime.now() - start_time

    print('Preliminary run')
    print(f"n = {SAMPLE}, Int_ = {Int_}, Var = {Var_Int_}, IC_Normal = {IC_Normal}, time = {elapsed_time}")

    print('Analytical solution')
    analytic_value = quad(lambda x1:
                          quad(lambda x2:
                               quad(lambda x3:
                                    quad(lambda x4:
                                         quad(lambda x5: F(x1, x2, x3, x4, x5), 0, 1)[0], 0, 1)[0], 0, 1)[0], 0, 1)[0], 0, 1)[0]
    print(f"Analytic value = {analytic_value}")

    print('Calculating number of replications')
    nN = number_of_replications_normal(Var_F)
    print(f"nN = {nN}, delta = {DELTA}, epsilon = {EPSILON}")

    cubre_valor_90 = 0
    cubre_valor_95 = 0
    cubre_valor_99 = 0
    for _ in range(500):
        reset_seed(1)
        (Int_, Var_Int_, IC_Normal, Var) = montecarlo_simulation(n=nN)
        # 95%
        if IC_Normal[0] <= analytic_value <= IC_Normal[1]:
            cubre_valor_95 += 1
        # 90%
        IC_Normal = (Int_ - i_norm_90 * math.sqrt(Var_Int_),
                     Int_ + i_norm_90 * math.sqrt(Var_Int_))
        if IC_Normal[0] <= analytic_value <= IC_Normal[1]:
            cubre_valor_90 += 1
        # 99%
        IC_Normal = (Int_ - i_norm_99 * math.sqrt(Var_Int_),
                     Int_ + i_norm_99 * math.sqrt(Var_Int_))
        if IC_Normal[0] <= analytic_value <= IC_Normal[1]:
            cubre_valor_99 += 1

    cubre_valor_90 /= 500
    cubre_valor_95 /= 500
    cubre_valor_99 /= 500

    cubre_valor_90 *= 100
    cubre_valor_95 *= 100
    cubre_valor_99 *= 100

    print('Final run')
    print(
        f"90% = {cubre_valor_90}, 95% = {cubre_valor_95}, 99% = {cubre_valor_99}")


def montecarlo_simulation(n: int):
    # Initialize the variables
    S = 0
    T = 0

    for i in range(n):
        # Random point generator using uniform distribution U(0,1)
        x_j = random_point()
        F_x_y = F(*x_j)
        T += (1 - (1/i)) * ((F_x_y - (S/(i-1))) ** 2) if i > 1 else 0
        S += F_x_y

    Int_ = (S / n)
    Var_F = T / (n - 1)
    Var_Int_ = Var_F / n
    IC_Normal = (Int_ - i_norm_95 * math.sqrt(Var_Int_),
                 Int_ + i_norm_95 * math.sqrt(Var_Int_))

    return (Int_, Var_Int_, IC_Normal, Var_F)


def random_point():
    return [U_01() for _ in range(5)]


def U_01():
    return random.uniform(0, 1)


def number_of_replications_normal(punctual_variance: float):
    i_norm_delta = i_norm(1 - (DELTA / 2))
    sqr_epsilon = EPSILON ** 2
    return math.ceil((((i_norm_delta ** 2) * punctual_variance) / sqr_epsilon))


def reset_seed(i: int):
    random.seed(SEED_NUMBER + i)


if __name__ == "__main__":
    main()
