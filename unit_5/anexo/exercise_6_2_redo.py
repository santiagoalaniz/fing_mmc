from scipy.stats import norm, uniform

import datetime
import math
import numpy as np
import pdb

SEED_NUMBER = 50826476
np.random.seed(SEED_NUMBER)

def std_uniform(n=int): return uniform(loc= 0, scale= 1).rvs(size= n)

# Defincion de constantes del ejercicio
def k(x) -> float:
    return x[0] * x[1]**2 * x[2]**3 * x[3]**4 * x[4]**5

# Parametros del experimento
n = 1000000
delta = 0.05
uniform_samples = std_uniform(n*5).tolist()

def montecarlo_simulation() -> (float, float, (float, float)):
    # Init
    S = 0
    T = 0

    for i in range(n):
        k_x_i = k([uniform_samples.pop() for _ in range(5)]) # k(X_i)
        T += (1 - (1/i)) * ((k_x_i - (S/(i-1))) ** 2) if i > 1 else 0
        S += k_x_i
    
    Int_ = (S/n)
    Var_F = T / (n - 1)
    Var_Int_ = Var_F / n
    ic_delta = norm.ppf(1 - delta/2) * math.sqrt(Var_Int_)
    IC = (Int_ - ic_delta, Int_ + ic_delta)

    return (Int_, Var_Int_, IC)

def main():
    start_time = datetime.datetime.now()
    (Int_, Var_Int_, IC) = montecarlo_simulation()
    end_time = datetime.datetime.now()

    print(f'Int_ = {Int_}, Var_Int_ = {Var_Int_}, IC = {IC}, time = {end_time - start_time}')

if __name__ == "__main__":
    main()