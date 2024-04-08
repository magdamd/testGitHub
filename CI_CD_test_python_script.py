import numpy as np

def add(a, b):
  r = a + b
  with open("New_version_values.txt", "ab") as f:
    np.savetxt("New_version_values.txt", r, fmt='%1.3f')
  return r

def subtract(a, b):
  r = a - b
  with open("New_version_values.txt", "ab") as f:
    np.savetxt("New_version_values.txt", r, fmt='%1.3f')
  return r
