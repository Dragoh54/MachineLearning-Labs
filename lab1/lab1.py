import numpy as np


def spiral_matrix(n: int) -> np.ndarray:  # n dimensional array
    # передаем текущую матрицу и новую размерность
    def transform(matrix: np.ndarray, n: int) -> np.ndarray:
        # если ушли за 0 то заканчиваем рекурсию
        if n == -1:
            return matrix
        # отсоединяем верхнюю строку от матрицы
        top, bottom = np.vsplit(matrix, [1])
        bottom = bottom.reshape(bottom.shape[::-1])
        # обьединяем матрицу с ее готовой верхней частью новую матрицу,
        # которая будет повернута на 90 градусов по часовой
        return np.concatenate([top, np.rot90(transform(bottom, n - 1), -1)])

    matrix = np.arange(1, n**2 + 1).reshape(n, n)

    return transform(matrix, n)


print(spiral_matrix(5))
