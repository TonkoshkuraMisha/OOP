from math import sqrt
from functools import reduce


def mean(lst):
    """Calculate the mean (average) of a list."""
    return sum(lst) / len(lst)


def variance(lst):
    """Calculate the variance of a list."""
    m = mean(lst)
    return sum((x - m) ** 2 for x in lst) / len(lst)


def correlation_coefficient(x_list, y_list):
    """Calculate the correlation coefficient between two lists x_list and y_list."""
    n = len(x_list)

    # Calculate mean of x_list and y_list
    mean_x = mean(x_list)
    mean_y = mean(y_list)

    # Calculate standard deviation (sigma) of x_list and y_list
    sigma_x = sqrt(variance(x_list))
    sigma_y = sqrt(variance(y_list))

    # Calculate the numerator of the correlation coefficient formula
    numerator = sum((x * y - mean_x * mean_y) for x, y in zip(x_list, y_list))

    # Calculate the correlation coefficient
    correlation = numerator / (sigma_x * sigma_y)

    return correlation


def get_numeric_list(prompt):
    """Prompt the user to enter a list of numbers separated by spaces."""
    input_data = input(prompt).strip()
    return list(map(float, input_data.split()))


# Получаем списки x_list и y_list от пользователя
x_list = get_numeric_list()

y_list = get_numeric_list()

# Вычисляем коэффициент корреляции между x_list и y_list
result = correlation_coefficient(x_list, y_list)
print("Коэффициент корреляции:", result)
