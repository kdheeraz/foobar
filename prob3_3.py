from fractions import Fraction,gcd

def transform_matrix(m):
    l = len(m)
    for i in range(l):
        row_sum = sum(m[i])
        if row_sum == 0:
            m[i][i] = 1
        else:
            for j in range(l):
                m[i][j] = Fraction(m[i][j], row_sum)

def get_submatrix(matrix, rows, cols):
    new_matrix = []
    for row in rows:
        current_row = []
        for col in cols:
            current_row.append(matrix[row][col])
        new_matrix.append(current_row)
    return new_matrix

def get_q_matrix(matrix, transient_states):
    return get_submatrix(matrix, transient_states, transient_states)

def get_r_matrix(matrix, transient_states, absorbing_states):
    return get_submatrix(matrix, transient_states, absorbing_states)

def make_2d_list(n, m):
    a = []
    for row in range(n):
        a += [[0]*m]
    return a

def make_identity(n):
    matrix = make_2d_list(n, n)
    for i in range(n):
        matrix[i][i] = 1
    return matrix

def subtract_matrices(a, b):
    new_matrix = []
    n, m = len(a), len(b)
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[i][j] - b[i][j])
        new_matrix.append(row)
    return new_matrix

def multiply_matrices(a, b):
    ar, ac, bc = len(a), len(a[0]), len(b[0])
    c = make_2d_list(ar, bc)
    for i in range(ar):
        for j in range(bc):
            prod = Fraction(0, 1)
            for k in range(ac):
                prod += a[i][k] * b[k][j]
            c[i][j] = prod
    return c

def multiply_row_of_square_matrix(matrix, row, k):
    n = len(matrix)
    identity = make_identity(n)
    identity[row][row] = k
    return multiply_matrices(identity, matrix)

def add_multiple_of_row_of_square_matrix(matrix, source_row, k, target_row):
    n = len(matrix)
    row_operator = make_identity(n)
    row_operator[target_row][source_row] = k
    return multiply_matrices(row_operator, matrix)

def invert_matrix(matrix):
    n = len(matrix)
    inverse = make_identity(n)
    for col in range(n):
        diagonal_row = col
        k = Fraction(1, matrix[diagonal_row][col])
        matrix = multiply_row_of_square_matrix(matrix, diagonal_row, k)
        inverse = multiply_row_of_square_matrix(inverse, diagonal_row, k)
        source_row = diagonal_row
        for target_row in range(n):
            if source_row != target_row:
                k = -matrix[target_row][col]
                matrix = add_multiple_of_row_of_square_matrix(matrix, source_row, k, target_row)
                inverse = add_multiple_of_row_of_square_matrix(inverse, source_row, k, target_row)
    return inverse

def lcm(a, b):
    result = a * b // gcd(a, b)
    return result

def lcm_for_arrays(args):
    array_length = len(args)
    if array_length <= 2:
        return lcm(*args)

    initial = lcm(args[0], args[1])
    i = 2
    while i < array_length:
        initial = lcm(initial, args[i])
        i += 1
    return initial

def solution(m):
    transient_states = []
    absorbing_states = []
    for i in range(len(m)):
        row = m[i]
        if sum(row) == 0:
            absorbing_states.append(i)
        else:
            transient_states.append(i)

    transform_matrix(m)

    q = get_q_matrix(m, transient_states)
    r = get_r_matrix(m, transient_states, absorbing_states)
    identity = make_identity(len(q))
    diff = subtract_matrices(identity, q)
    inverse = invert_matrix(diff)
    result = multiply_matrices(inverse, r)

    denominator = lcm_for_arrays([item.denominator for item in result[0]])
    result = [item.numerator * denominator // item.denominator for item in result[0]]
    result.append(denominator)
    return result



if __name__ == "__main__":
    m1 = [
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(solution(m1))
