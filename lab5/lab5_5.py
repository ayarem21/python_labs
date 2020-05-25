import numpy as np

class SumMatrix:
    def MainMethod(self):
        m1 = np.random.randint(0, 20, (3, 3))
        m2 = np.random.randint(0, 20, (3, 3))
        self.PrintMatrix(m1)
        self.PrintMatrix(m2)
        result = self.SumMatrix(m1, m2)
        self.PrintMatrix(result)
        det_result = self.det(result)
        print(str(det_result))
    def PrintMatrix(self, matrix):
        print(str(matrix))
    def SumMatrix(self, a, b):
        result = a + b
        return result
    def det(self, matrix):
        det_matrix = np.linalg.det(matrix)
        return det_matrix

def main():
    sumMatrix = SumMatrix()
    sumMatrix.MainMethod()
main()