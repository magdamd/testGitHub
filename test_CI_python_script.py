import CI_CD_test_python_script

class TestPythonScript:

    def test_add(self):
        assert 4 == CI_CD_test_python_script.add(2, 2)

    def test_subtraction(self):
        assert 1 == CI_CD_test_python_script.subtract(4, 2)
