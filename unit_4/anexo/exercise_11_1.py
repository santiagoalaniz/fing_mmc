from scipy.stats import norm, uniform

import datetime
import math
import numpy as np
import pdb

np.random.seed(50826476)

# Defincion de constantes del ejercicio
ccl_cone = {
  'r' : 0.4,
  'c' : (0.5, 0.5), # (x,y)
}
cone_height = 8

ccl_cone_area = math.pi * (ccl_cone['r']**2)
cone_vol = (1/3) * math.pi * (ccl_cone['r']**2) * cone_height

# Definicion de funciones auxiliares
def sqrt(x=float)           : return math.sqrt(x)
def std_normal(n=int)       : return norm(loc= 0, scale= 1).rvs(size= n)     # [N(0,1), N(0,1)]
def std_uniform(n=int)      : return uniform(loc= 0, scale= 1).rvs(size= n)  # U(0,1)

# Definicion de funciones de distribucion del ejercicio
def Fr()  -> float: return sqrt(uniform_samples.pop())                # Fr(x) = x^2 0<=x<=1

def scl_to_ccl_cone(x: float, y: float) -> (float, float):
  return (
    x * ccl_cone['r'] + ccl_cone['c'][0],
    y * ccl_cone['r'] + ccl_cone['c'][1]
  )

def F()   -> (float, float):
  r = Fr()
  (Z1, Z2) = (normal_samples.pop(), normal_samples.pop())
  X1 = r * Z1 / sqrt(Z1**2 + Z2**2)
  X2 = r * Z2 / sqrt(Z1**2 + Z2**2)
  return scl_to_ccl_cone(X1, X2)

def k(x=float, y=float) -> float:
  h = cone_height
  r = ccl_cone['r']
  x0 = ccl_cone['c'][0]
  y0 = ccl_cone['c'][1]

  return h - ((h / r) * sqrt((x - x0)**2 + (y - y0)**2))

def point_in_circle(x_j):
  center = ccl_cone['c']
  radius = ccl_cone['r']
  norm = 0

  for i in range(len(x_j)):
    norm += (x_j[i] - center[i])**2

  return True if norm <= radius**2 else False

# Definiciones de constantes del experimento
n = 1000000
delta = 0.05
normal_samples = std_normal(n*2).tolist()
uniform_samples = std_uniform(n).tolist()

# Definicion de funciones del experimento
def montecarlo_simulation(n: int) -> (float, float, (float, float), float):
  S = 0
  T = 0

  for i in range(n):
    (x, y) = F()
    k_x_y = k(x, y)
    T += (1 - (1/i)) * ((k_x_y - (S/(i-1))) ** 2) if i > 1 else 0
    S += k_x_y

  Int_ = (S / n) * ccl_cone_area
  Var_F = T / (n - 1)
  Var_Int_ = Var_F / n
  ic_delta = norm.ppf(1 - delta/2) * math.sqrt(Var_Int_)
  IC = (Int_ - ic_delta, Int_ + ic_delta)

  return (Int_, Var_Int_, IC, Var_F)


# Funcion principal
def main():
  start_time = datetime.datetime.now()
  (Int_, Var_Int_, IC, Var_F) = montecarlo_simulation(n)
  elapsed_time = datetime.datetime.now() - start_time

  print(f"n = {n}, Int_ = {Int_}, Var = {Var_Int_}, IC_Normal = {IC}, Diff = {abs(cone_vol - Int_)}, time = {elapsed_time}")

if __name__ == "__main__":
  main()
