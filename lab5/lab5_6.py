import numpy as np

class Expression:
    def MainMethod(self):
        m1 = np.random.randint(0, 20, (3, 3))
        m2 = np.random.randint(0, 20, (3, 3))
        self.PrintMatrix(m1)
        self.PrintMatrix(m2)
        result = self.ExpressionMatrix(m1, m2)
        self.PrintMatrix(result)
        det_result = self.det(result)
        print(str(det_result))
    def PrintMatrix(self, matrix):
        print(str(matrix))
    def ExpressionMatrix(self, a, b):
        # 3*A + 5*B
        a = 3*a
        self.PrintMatrix(a)
        b = 5*b
        self.PrintMatrix(b)
        result = a + b
        return result
    def det(self, matrix):
        det_matrix = np.linalg.det(matrix)
        return det_matrix

def main():
    expression = Expression()
    expression.MainMethod()

main()