import random
import datetime
import pdb

# lower(l) and upper(u) bounds for the U(l,u) and the dependencies
TASKS = {
  'T1':   {'l': 40, 'u': 56, 'depends': []},
  'T2':   {'l': 24, 'u': 32, 'depends': ['T1']},
  'T3':   {'l': 20, 'u': 40, 'depends': ['T1']},
  'T4':   {'l': 16, 'u': 48, 'depends': ['T2', 'T3']},
  'T5':   {'l': 10, 'u': 30, 'depends': ['T2', 'T3']},
  'T6':   {'l': 15, 'u': 30, 'depends': ['T3']},
  'T7':   {'l': 20, 'u': 25, 'depends': ['T3']},
  'T8':   {'l': 30, 'u': 50, 'depends': ['T4', 'T5', 'T6', 'T7']},
  'T9':   {'l': 40, 'u': 60, 'depends': ['T5']},
  'T10':  {'l': 8, 'u': 16, 'depends': ['T7', 'T8', 'T9']},
}

# number of samples
SAMPLES = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

#seed number for the random number generator reproducibility
SEED_NUMBER = 50826476
random.seed(SEED_NUMBER)

def main():
  for sample in SAMPLES:
    start_time = datetime.datetime.now()
    # simulate X_s, Var_s for the given sample size
    (X_s, Var_s) = montecarlo_simulation(n=sample)
    elapsed_time = datetime.datetime.now() - start_time
    print(f"n = {sample}, X_s = {X_s}, Var_s = {Var_s}, time = {elapsed_time}")

def montecarlo_simulation(n: int):
  # Initialize the variables
  S_n = 0
  V_s = 0

  for i in range(n):
    sample_Ti = replication_set()
    S_n += sample_Ti['T10']
    V_s += sample_Ti['T10'] ** 2

  X_s = S_n / n
  V_s = V_s/(n*(n-1)) - (X_s ** 2)/(n-1)

  return (X_s, V_s)

def replication_set():
  # Initialize the sample_Ti, sample_Ti will be {Ti: task_i duration}
  sample_Ti = {}

  for task_i in TASKS:
    # If the task has no dependencies, then we can sample from the uniform distribution
    # Otherwise, then we need to calculate the overhead from the parents
    if TASKS[task_i]['depends'] == []:
      # U(l,u) = l + (u-l) * U(0,1)
      sample_Ti[task_i] = TASKS[task_i]['l'] + (TASKS[task_i]['u'] - TASKS[task_i]['l']) * u_01()
    else:
      # Being max_t the maximum of the parents duration
      # We can start the dependent task Ti after max_t
      # U(l + max_t, u + max_t) = l + max_t + (u-l) * U(0,1) = composed_overhead + (u-l) * U(0,1)
      max_t = max(list(map(lambda x: get_time(x, sample_Ti), TASKS[task_i]['depends'])))
      composed_overhead = TASKS[task_i]['l'] + max_t
      sample_Ti[task_i] = composed_overhead + (TASKS[task_i]['u'] - TASKS[task_i]['l']) * u_01()

  return sample_Ti

# Auxiliary function to get the time of a parent task (parent task is a task in the depends list)
def get_time(task, sample_Ti):
  return sample_Ti[task]

# Uniform distribution between 0 and 1
def u_01():
  return random.uniform(0,1)

if __name__ == "__main__":
  main()
