import datetime
import math
from scipy.stats import norm, uniform
import numpy as np
import pdb

np.random.seed(50826476)

## Cone parameters
CONE = {
  'C': (0.5, 0.5),
  'R': 0.4,
  'H': 8,
}

cone_vol = (1/3) * math.pi * (CONE['R']**2) * CONE['H']

## Function to estimate its integral,
### F(x,y) = 0 if (x,y) is outside the cone
### F(x,y) = H - ((H / R) * sqrt((x - C[0])**2 + (y - C[1])**2)) if (x,y) is inside the cone
H = CONE['H']
R = CONE['R']
X0 = CONE['C'][0]
Y0 = CONE['C'][1]

F = {
  'inside': lambda x, y: H - ((H / R) * math.sqrt((x - X0)**2 + (y - Y0)**2)),
  'outside': lambda x, y: 0
}

## Experiment parameters
SAMPLE = 1000000
DELTA = 0.05
EPSILON = 0.001
i_norm = norm.ppf
uniform_samples = uniform(loc=0, scale=1).rvs(size=2*SAMPLE).tolist()

# Excercise solution
def main():
  start_time = datetime.datetime.now()
  (Int_, Var_Int_, IC_Normal, Var_F) = montecarlo_simulation(n=SAMPLE)
  elapsed_time = datetime.datetime.now() - start_time

  diff = abs(cone_vol - Int_)

  print(f"n = {SAMPLE}, Int_ = {Int_}, Var = {Var_Int_}, IC_Normal = {IC_Normal}, Diff = {diff}, time = {elapsed_time}")

def montecarlo_simulation(n: int):
  # Initialize the variables
  S = 0
  T = 0

  for i in range(n):
    # Random point generator using uniform distribution U(0,1)
    x_j = random_point()
    F_x_y = F[point_in_circle(x_j)](*x_j)
    T += (1 - (1/i)) * ((F_x_y - (S/(i-1))) ** 2) if i > 1 else 0
    S += F_x_y

  Int_ = (S / n)
  Var_F = T / (n - 1)
  Var_Int_ = Var_F / n
  i_norm_delta = i_norm(1 - DELTA/2)
  IC_Normal = (Int_ - i_norm_delta * math.sqrt(Var_Int_), Int_ + i_norm_delta * math.sqrt(Var_Int_))

  return (Int_, Var_Int_, IC_Normal, Var_F)

def random_point():
  return [uniform_samples.pop() for _ in range(2)]



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
