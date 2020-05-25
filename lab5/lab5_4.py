import numpy as np

class Determinant:
    def MainMethod(self):
        matrix = np.random.randint(0, 20, (3, 3))
        self.PrintMatrix(matrix)
        det_matrix = self.det(matrix)
        print(str(det_matrix))
        self.check_det(det_matrix, matrix)
    def PrintMatrix(self, matrix):
        print(str(matrix))
    def det(self, matrix):
        det_matrix = 0
        det_matrix += matrix[0, 0] * matrix[1, 1] * matrix[2, 2]
        det_matrix += matrix[2, 0] * matrix[0, 1] * matrix[1, 2]
        det_matrix += matrix[1, 0] * matrix[0, 2] * matrix[2, 1]
        det_matrix -= matrix[2, 0] * matrix[1, 1] * matrix[0, 2]
        det_matrix -= matrix[1, 0] * matrix[0, 1] * matrix[2, 2]
        det_matrix -= matrix[0, 0] * matrix[2, 1] * matrix[1, 2]
        return det_matrix
    def check_det(self, det, matrix):
        library_value = np.linalg.det(matrix)
        print("Бібліотечне значення детермінанта = ", str(library_value))
        if (abs(det - library_value) <= 0.0000001):
            print("Детермінант правильний")
        else:
            print("Детермінант неправильний")

def main():
    detMatrix = Determinant()
    detMatrix.MainMethod()
main()