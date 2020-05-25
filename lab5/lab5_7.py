import numpy as np

class SumElements:
    def MainMethod(self):
        start1 = int(input("Введіть початок діапазону 1: "))
        end1 = int(input("Введіть кінець діапазону 1: "))
        start2 = int(input("Введіть початок діапазону 2: "))
        end2 = int(input("Введіть кінець діапазону 2: "))
        m1 = np.random.randint(start1, end1, (5, 10))
        m2 = np.random.randint(start2, end2, (5, 10))
        self.PrintMatrix(m1)
        self.PrintMatrix(m2)
        m_row = m1.sum(axis=1)
        m_row = m_row.reshape(5, 1)
        m_call = m2.sum(axis=0)
        m_call = m_call.reshape(1, 10)
        self.PrintMatrix(m_row)
        self.PrintMatrix(m_call)
    def PrintMatrix(self, matrix):
        print(str(matrix))

def main():
    sumElements1 = SumElements()
    sumElements1.MainMethod()
main()