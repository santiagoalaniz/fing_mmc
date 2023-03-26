import random
import datetime
import math
from scipy.stats import norm
from scipy.integrate import quad
import pdb

# Constants

# Seed number for the random number generator reproducibility
SEED_NUMBER = 50826476
random.seed(SEED_NUMBER)

# Cone parameters
CONE = {
    'C': (0.5, 0.5),
    'R': 0.4,
    'H': 8,
}

# Function to estimate its integral,
# F(x,y) = 0 if (x,y) is outside the cone
# F(x,y) = H - ((H / R) * sqrt((x - C[0])**2 + (y - C[1])**2)) if (x,y) is inside the cone
H = CONE['H']
R = CONE['R']
X0 = CONE['C'][0]
Y0 = CONE['C'][1]


def F(x1, x2, x3, x4, x5): return x1 * x2 ** 2 * x3 ** 3 * x4 ** 4 * x5 ** 5


# Experiment parameters
SAMPLE = 1000000
DELTA = 0.05
EPSILON = 0.001
i_norm = norm.ppf

# Excercise solution


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

    reset_seed(1)

    start_time = datetime.datetime.now()
    (Int_, Var_Int_, IC_Normal, Var) = montecarlo_simulation(n=nN)
    elapsed_time = datetime.datetime.now() - start_time

    print('Final run')
    print(
        f"n = {nN}, Int_ = {Int_}, Var = {Var_Int_}, IC_Normal = {IC_Normal}, time = {elapsed_time}")


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
    i_norm_delta = i_norm(1 - DELTA/2)
    IC_Normal = (Int_ - i_norm_delta * math.sqrt(Var_Int_),
                 Int_ + i_norm_delta * math.sqrt(Var_Int_))

    return (Int_, Var_Int_, IC_Normal, Var_F)


def random_point():
    return [U_01() for _ in range(5)]


def U_01():
    return random.uniform(0, 1)


def point_in_circle(x_j):
    center = CONE['C']
    radius = CONE['R']
    norm = 0

    for i in range(len(x_j)):
        norm += (x_j[i] - center[i])**2

    return 'inside' if norm <= radius**2 else 'outside'


def number_of_replications_normal(punctual_variance: float):
    i_norm_delta = i_norm(1 - (DELTA / 2))
    sqr_epsilon = EPSILON ** 2
    return math.ceil((((i_norm_delta ** 2) * punctual_variance) / sqr_epsilon))


def reset_seed(i: int):
    random.seed(SEED_NUMBER + i)


if __name__ == "__main__":
    main()
