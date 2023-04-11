import random
import datetime
import sys
import pdb

# Set linear boundaries by command line
INCLUDE_BOUNDARIES = True if len(sys.argv) > 1 else False

# Seed number for the random number generator reproducibility
SEED_NUMBER = 50826476
random.seed(SEED_NUMBER)

# Number of samples
SAMPLES = [10000, 1000000]

# 6_th dimension sphere.
SPHERE = {
  'center': (0.45, 0.5, 0.6, 0.6, 0.5, 0.45),
  'radius': 0.35,
}

# Linear boundaries (from the problem)
# lb_1(x1,x4) = 3x1 + 7x4 <= 5
# lb_2(x3,x4) = x3 + x4 <= 1
# lb_3(x1, x2, x5, x6) = x1 - x2 - x5 + x6 >= 0

LINEAR_BOUNDARIES = [
  lambda x: 3*x[0] + 7*x[3] <= 5,
  lambda x: x[2] + x[3] <= 1,
  lambda x: x[0] - x[1] - x[4] + x[5] >= 0,
]

def main():
  for sample in SAMPLES:
    start_time = datetime.datetime.now()
    (Vol_, Var_s, S_n) = montecarlo_simulation(n=sample)
    elapsed_time = datetime.datetime.now() - start_time
    print(f"n = {sample}, Sn = {S_n}, Vol_ = {Vol_}, Var = {Var_s}, time = {elapsed_time}, BOUNDARIES = {INCLUDE_BOUNDARIES}")

def montecarlo_simulation(n: int):
  # Initialize the variables
  S_n = 0
  V_s = 0

  for i in range(n):
    # generador de la distribución uniforme
    x_j = random_point()

    # Si el punto está en la región, incrementar S_n
    S_n = S_n + 1 if point_in_region(x_j) else S_n

  Vol_ = S_n/n
  V_s = (S_n/n)*(1 - S_n/n)/(n-1)

  return (Vol_, V_s, S_n)

def random_point():
  return [U_01() for _ in range(6)]

def U_01():
  return random.uniform(0,1)

# Region: Sphere with some linear constraints (if LINEAR_CONSTRAINT is True)
def point_in_region(x_j):
  result = True

  # If linear boundaries are included, set them, otherwise, set a list with an always true lambda function
  boundaries = LINEAR_BOUNDARIES if INCLUDE_BOUNDARIES else [lambda x: True]

  # Check if the point violates any of linear boundaries
  for boundary in boundaries:
    result &= boundary(x_j)

  # If the point violates any of linear boundaries, return False, the point is not in the region
  # Otherwise, check if the point is in the sphere.
  if (not result):
    return result
  else:
    return point_in_sphere(x_j)

def point_in_sphere(x_j):
  center = SPHERE['center']
  radius = SPHERE['radius']
  norm = 0

  # Sumatory of the squared distance between the point and the center
  for i in range(len(center)):
    norm += (x_j[i] - center[i])**2

  # If the squared distance is less than the squared radius, the point is in the sphere
  return norm <= radius**2


if __name__ == '__main__':
  main()
