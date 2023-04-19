import random
import datetime
import math
import pdb
import sys
from scipy.stats import norm

# Constants
## P is the proffesors set, S is the students set, L is the lenguages set
P = set()
S = set()
L = set()

## idS is the dictionary that maps students to a set of lenguages they know
## idP is the dictionary that maps proffesors to a set of lenguages they know
idS = []
idP = []

## Seed number for the random number generator reproducibility
SEED_NUMBER = 50826476
random.seed(SEED_NUMBER)

# Monte Carlo.
## Entry parameters
SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
DELTA = float(sys.argv[2]) if len(sys.argv) > 2 else 0.05
DATA = 1 if len(sys.argv) > 3 else 0

## Library renames
inversed_norm = norm.ppf

def main():
  # Generates L, S, P, idS, idP
  initialize()
  print_generated_data() if DATA else None
  start_time = datetime.datetime.now()
  (X_, Var_X_, IC) = montecarlo_simulation(n=SAMPLES, r=len(P) ** len(S))
  elapsed_time = datetime.datetime.now() - start_time

  print(f"n = {SAMPLES}, delta = {DELTA}, X_ = {X_}, Var = {math.sqrt(Var_X_)}, IC (Agresti-Coull) = {IC}, time = {elapsed_time}")

def initialize():
  nL = random.randint(3, 6)
  nS = random.randint(8, 16)
  nP = random.randint(2, 4)

  for i in range(nL):
    L.add(i)

  for i in range(nS):
    S.add(i)
    idS.append(set())
    nLS = random.randint(1, nL)
    for j in range(nLS):
      idS[i].add(random.randint(0, nL - 1))

  for i in range(nP):
    P.add(i)
    idP.append(set())
    nLP = random.randint(1, nL)
    for j in range(nLP):
      idP[i].add(random.randint(0, nL - 1))

def print_generated_data():
  print('----------------Generated-Data-----------------')
  print(f"L = {L}")
  print(f"S = {S}")
  print(f"P = {P}")
  print(f"idS = {idS}")
  print(f"idP = {idP}")
  print(f"r = {len(P) ** len(S)}")
  print('-----------------------------------------------')

def montecarlo_simulation(n: int, r: int):
  S_n = 0

  for i in range(n):
    a = random_configuration()
    S_n += 1 if is_valid(configuration= a) else 0

  X_ = r * (S_n / n)
  Var_X_ = X_ * (r - X_) / (n - 1)

  IC = agresti_coull_IC(
    n_s=S_n,
    n=n,
    delta=DELTA
  )

  IC = (IC[0] * r, IC[1] * r)

  return (X_, Var_X_, IC)

def random_configuration():
  return [random.randint(0, len(P) - 1) for i in range(len(S))]

def is_valid(configuration: list):
  for i in range(len(configuration)):
    if not idS[i].intersection(idP[configuration[i]]):
      return False
  return True

def agresti_coull_IC(n_s=int, n=int, delta=float):
  z = inversed_norm(1 - (delta / 2))
  sqr_z = z ** 2
  n_ = n + (sqr_z)
  p_ = (1 / n_) * (n_s + (sqr_z / 2))
  ic_constant = (z * math.sqrt((p_ / n_) * (1 - p_)))

  ic_lower = p_ - ic_constant
  ic_upper = p_ + ic_constant

  return (ic_lower, ic_upper)

if __name__ == '__main__':
  main()
