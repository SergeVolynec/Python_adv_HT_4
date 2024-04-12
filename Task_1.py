def transpouse(mat: list) -> list:
    """Функция транспонирует матрицу."""
    matrix = []
    for i in range(len(mat[0])):
        matrix.append(list())
        for j in range(len(mat)):
            matrix[i].append(mat[j][i])
    return matrix


if __name__ == '__main__':
    a = [[0, 4], [1, 5], [2, 6]]
    new_mtrx = transpouse(a)
    print(new_mtrx)
