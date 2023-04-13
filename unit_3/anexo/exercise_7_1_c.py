import random
import collections
import datetime
import math
import pdb
import sys
from scipy.stats import norm

# Constants
# Conjunto S (Estudiantes):
# {Maria, Sophie, Liliana, Lucia, Monique, Rodrigo, John, Neymar, Jacques, Juan}
S = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# Conjunto L (Lenguajes):
# {español, ingles, francés, portugués}
L = {0, 1, 2, 3}
# Conjunto P (Profesores):
# {Tom, Luciana, Gerard, Silvia}
P = {0, 1, 2, 3}

# Max and min number of students assigned to a teacher
MIN_S = 1
MAX_S = 4

# idS[i] = {j, k, ...} significa que el estudiante i habla los lenguajes j, k, ...
idS = [
  {0, 1},     # Maria (español, ingles)
  {1, 2},     # Sophie (ingles, frances)
  {0, 3},     # Liliana (español, portugues)
  {1, 3},     # Lucia (ingles, portugues)
  {2},        # Monique (frances)
  {0, 1, 2},  # Rodrigo (español, ingles, frances)
  {1},        # John (ingles)
  {0, 3},     # Neymar (español, portugues)
  {2, 3},     # Jacques (frances, portugues)
  {0}         # Juan (español)
]

# idP[i] = {j, k, ...} significa que el profesor i habla los lenguajes j, k, ...
idP = [
  {0, 1, 2},  # Tom (español, ingles, frances)
  {1, 3},     # Luciana (ingles, portugues)
  {1, 2},     # Gerard (ingles, frances)
  {0, 2}      # Silvia (español, frances)
]

## Seed number for the random number generator reproducibility
SEED_NUMBER = 50826476
random.seed(SEED_NUMBER)

# Monte Carlo.
## Entry parameters
SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
DELTA = float(sys.argv[2]) if len(sys.argv) > 2 else 0.05

## Library renames
inversed_norm = norm.ppf

def main():
  # print_generated_data()
  start_time = datetime.datetime.now()
  (X_, Var_X_, IC) = montecarlo_simulation(n=SAMPLES, r=len(P) ** len(S))
  elapsed_time = datetime.datetime.now() - start_time

  print(f"n = {SAMPLES}, delta = {DELTA}, X_ = {X_}, Var = {math.sqrt(Var_X_)}, IC (Agresti-Coull) = {IC}, time = {elapsed_time}")


def print_generated_data():
  print(f"L = {L}")
  print(f"S = {S}")
  print(f"P = {P}")
  print(f"idS = {idS}")
  print(f"idP = {idP}")
  print(f"r = {len(P) ** len(S)}")

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
  for p in P:
    if configuration.count(p) < MIN_S or configuration.count(p) > MAX_S:
      return False

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
