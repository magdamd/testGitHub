import numpy as np

def add(a, b):
  r = a + b
  with open("New_version_values.txt", "ab") as f:
    numpy.savetxt(f, r)
  return r

def subtract(a, b):
  r = a - b
  with open("New_version_values.txt", "ab") as f:
    numpy.savetxt(f, r)
  return r
