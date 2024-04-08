import numpy as np

def add(a, b):
  r = a + b
  #with open("New_version_values.txt", "ab") as f:
  np.savetxt("New_version_values.txt", np.asarray(r), fmt="%1.4e")#'test.out', x, fmt='%1.4e'
  return r

def subtract(a, b):
  r = a - b
  #with open("New_version_values.txt", "ab") as f:
  np.savetxt("New_version_values.txt", np.asarray(r), fmt="%1.4e")
  return r
