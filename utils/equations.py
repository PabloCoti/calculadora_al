import re


def equation_parse(string):
    eq_list = string.split('\n')

    n_pattern = r'-?\d+'
    l_pattern = r'[a-zA-Z]'

    coefficients = []
    constants = []
    letters = []

    for eq in eq_list:
        numbers = re.findall(n_pattern, eq)
        letters = re.findall(l_pattern, eq)

        number_list = []
        for n in range(len(numbers)):
            if n != len(numbers) - 1:
                number_list.append(int(numbers[n]))
            else:
                constants.append(int(numbers[n]))

        coefficients.append(number_list)

    return solve_equation(coefficients, constants, letters)

def solve_equation(coefficients, constants, letters):
    n = len(coefficients)

    # Applying Gaussian elimination
    for i in range(n):
        pivot = coefficients[i][i]
        for j in range(i + 1, n):
            ratio = coefficients[j][i] / pivot
            for k in range(n):
                coefficients[j][k] -= ratio * coefficients[i][k]
            constants[j] -= ratio * constants[i]

    # Back substitution to find the solution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            constants[i] -= coefficients[i][j] * solution[j]
        solution[i] = constants[i] / coefficients[i][i]

    result = ''
    for n, r in enumerate(solution):
        result += f"{letters[n]}={r}, "

    return result
