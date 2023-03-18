from scipy.stats import norm
from math import log
from math import ceil

import pdb

# Constants
EPS = 0.01
DELTAS = [0.001, 0.01, 0.05]
inversed_norm = norm.ppf
ln = log

def main():
  for delta in DELTAS:
    nC = n_of_samples_chebyshev(delta, EPS)
    nN = n_of_samples_normal(delta, EPS)
    nH = n_of_samples_hoeffding(delta, EPS)
    print(f'eps={EPS}, delta={delta}, nC={nC}, nN={nN}, nH={nH}')

def n_of_samples_chebyshev(delta, eps):
  aux = 1 / (4 * delta * (eps ** 2))
  return ceil(aux)

def n_of_samples_normal(delta, eps):
  aux = (inversed_norm(1 - (delta/2)) / (2*eps)) ** 2
  return ceil(aux)

def n_of_samples_hoeffding(delta, eps):
  aux = 2 * ln(2 / delta) / (4 * (eps**2))
  return ceil(aux)


if __name__ == '__main__':
  main()
