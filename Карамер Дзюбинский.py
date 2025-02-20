class CramerSolver:
    def __init__(self, matrix):
        self.n = len(matrix)  # Размер системы
        if any(len(row) != self.n + 1 for row in matrix):  # Проверка на корректность
            raise ValueError("Матрица должна быть размера n×(n+1)")
        self.matrix = matrix

    def determinant(self, mat):
        size = len(mat)
        if size == 1:
            return mat[0][0]  # Детерминант матрицы 1×1
        if size == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]  # Детерминант 2×2

        det = 0
        for col in range(size):
            sub_matrix = [row[:col] + row[col + 1:] for row in mat[1:]]  # Минор
            det += (-1) ** col * mat[0][col] * self.determinant(sub_matrix)  # Разложение по строке
        return det

    def solve(self):
        main_matrix = [row[:-1] for row in self.matrix]  # Основная матрица (без последнего столбца)
        det_main = self.determinant(main_matrix)

        if det_main == 0:
            return "Нет единственного решения"

        solutions = []
        for i in range(self.n):
            modified_matrix = [row[:i] + [row[-1]] + row[i + 1:-1] for row in self.matrix]  # Заменяем i-й столбец
            solutions.append(self.determinant(modified_matrix) / det_main)

        return solutions


# Примеры
print("Решение 2x2:", CramerSolver([[12,-10,46], [3,20,-11]]).solve())  # [3.0, -1.0]
print("Решение 3x3:", CramerSolver([[3,-2,4,21], [3,4,-2,9], [2,-1,-1,10]]).solve())  # [5.0, -1.0, 1.0]
