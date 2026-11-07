"""it was a sample progrom created by opencode you can delete it for your projects"""

"""A small matrix program: basic operations on matrices stored as lists of lists."""


def add(a, b):
    _check_same_shape(a, b)
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def subtract(a, b):
    _check_same_shape(a, b)
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def multiply(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Cannot multiply: columns of A must equal rows of B")
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transpose(a):
    return [list(row) for row in zip(*a)]


def determinant(a):
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("Determinant requires a square matrix")
    if n == 1:
        return a[0][0]
    if n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]

    total = 0
    for col in range(n):
        minor = [row[:col] + row[col + 1:] for row in a[1:]]
        total += ((-1) ** col) * a[0][col] * determinant(minor)
    return total


def identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def _check_same_shape(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Matrices must have the same shape")


def show(name, m):
    print(f"{name}:")
    for row in m:
        print("  [" + "  ".join(f"{x:4}" for x in row) + "]")
    print()


if __name__ == "__main__":
    A = [[1, 2, 3],
         [4, 5, 6]]
    B = [[7, 8],
         [9, 10],
         [11, 12]]
    C = [[2, 0],
         [0, 2]]

    show("A", A)
    show("B", B)
    show("A x B", multiply(A, B))
    show("A transposed", transpose(A))

    show("C", C)
    print("det(C) =", determinant(C))
    print("det([[0, 1], [1, 0]]) =", determinant([[0, 1], [1, 0]]))
    show("Identity 3x3", identity(3))
