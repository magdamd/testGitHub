import CI_CD_test_python_script
import numpy as np

vector = np.loadtxt("True_values.txt")

value1 = vector[0]
value2 = vector[1]

class TestPythonScript:

    def test_add(self):
        assert value1 == CI_CD_test_python_script.add(2, 2)

    def test_subtraction(self):
        assert value2 == CI_CD_test_python_script.subtract(4, 2)
