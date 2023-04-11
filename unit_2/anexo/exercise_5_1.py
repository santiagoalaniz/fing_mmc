import math
from scipy.stats import norm

# Precomputed number of samples (../unit_2/anexo/log_5_1.txt)
nH = 1000000
S_nH = 303

# Constants
DELTA = 0.05
inversed_norm = norm.ppf

## Uncomment to see the results of the Monte Carlo simulation, with the number of samples required
# EPS = 0.0001
## Number of samples required for a given delta and epsilon using the Hoeffding's
# from exercise_4_1 import n_of_samples_hoeffding
# # Volume estimation of a 6-dimensional sphere with linear boundaries
# from exercise_3_1 import *


def main():
  ## Uncomment to see the results of the Monte Carlo simulation, with the number of samples required
  # nH = n_of_samples_hoeffding(DELTA, EPS)
  # print(f'eps={EPS}, delta={DELTA}, nH={nH}')

  # start_time = datetime.datetime.now()
  # (Vol_, Var_s, S_n) = montecarlo_simulation(nH)
  # elapsed_time = datetime.datetime.now() - start_time

  # print(f"n = {nH}, S_n = {S_n}, Vol_ = {Vol_}, Var = {Var_s}, BOUNDARIES = {INCLUDE_BOUNDARIES}, time = {elapsed_time}")

  (ic_C_lower, ic_C_upper) = chebyshev_interval_of_confidence(z=S_nH, n=nH, beta=math.sqrt(DELTA))
  print(f'Chebyshev Interval of Confidence: [{ic_C_lower}, {ic_C_upper}]')

  (ic_AC_lower, ic_AC_upper) = agresti_coull_interval_of_confidence(n_s=S_nH, n=nH, delta=DELTA)
  print(f'Agresti-Coull Interval of Confidence: [{ic_AC_lower}, {ic_AC_upper}]')

def chebyshev_interval_of_confidence(z=int, n=int, beta=float):
  a = z + (DELTA / 2)
  b = beta * math.sqrt((DELTA / 4) + (z * (n - z) / n))
  divident = n + DELTA

  ic_lower = (a - b) / divident
  ic_upper = (a + b) / divident

  return (ic_lower, ic_upper)

def agresti_coull_interval_of_confidence(n_s=int, n=int, delta=float):
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
