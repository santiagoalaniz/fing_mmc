from scipy.stats import norm, uniform
import sys
import datetime
import math
import numpy as np
import pdb

SEED_NUMBER = 50826476
np.random.seed(SEED_NUMBER)

# Funciones de distribucion para generar las muestras
def std_uniform(n=int): return uniform(loc= 0, scale= 1).rvs(size= n)
def strat_uniform(n=int, a=float, b=float): return uniform.rvs(loc=a, scale=b-a, size= n)

# Defincion de constantes del ejercicio
def k(x) -> float:
    return x[0] * x[1]**2 * x[2]**3 * x[3]**4 * x[4]**5

# Parametros del experimento
n = 1000000
delta = 0.05
uniform_samples = std_uniform(n*8).tolist()
# x5_strats = [(0, 0.20), (0.20, 0.40), (0.40, 0.60), (0.60, 0.80), (0.80, 1)]
x5_strats = [(0, 0.72), (0.72, 0.83), (0.83, 0.90), (0.90, 0.95), (0.95, 1)]

def evenly_strat_sampling() -> list:
    aux = []
    n_ = int(n/len(x5_strats))

    for strat in x5_strats:
        aux += strat_uniform(n=n_, a=strat[0], b=strat[1]).tolist()
    
    return aux

def proportionaly_strat_sampling() -> list:
    aux = []
    prob_strats = [round((strat[1] - strat[0]), 6) for strat in x5_strats]

    for i, strat in enumerate(x5_strats):
        n_ = int(round(n * prob_strats[i],2))
        aux += strat_uniform(n=n_, a=strat[0], b=strat[1]).tolist()

    return aux
        
 
def stratified_montecarlo_simulation(proportional=bool):
    # Init
    S = 0
    T = 0
    x5_samples = proportionaly_strat_sampling() if proportional else evenly_strat_sampling()

    for i in range(n):
        X_i = [uniform_samples.pop() for _ in range(4)] + [x5_samples.pop()]
        k_x_i = k(X_i) # k(X_i)
        T += (1 - (1/i)) * ((k_x_i - (S/(i-1))) ** 2) if i > 1 else 0
        S += k_x_i
    
    Int_ = (S/n)
    Var_F = T / (n - 1)
    Var_Int_ = Var_F / n
    ic_delta = norm.ppf(1 - delta/2) * math.sqrt(Var_Int_)
    IC = (Int_ - ic_delta, Int_ + ic_delta)

    return (Int_, Var_Int_, IC)

def main():
    prop = len(sys.argv) > 1

    start_time = datetime.datetime.now()
    (Int_, Var_Int_, IC) = stratified_montecarlo_simulation(proportional=prop)
    end_time = datetime.datetime.now()

    title = '[PROPORTIONALY]' if prop else '[EVENLY]'
    print(f'{title}')
    print(f'Int_ = {Int_}, Var_Int_ = {Var_Int_}, IC = {IC}, time = {end_time - start_time}')

if __name__ == "__main__":
    main()