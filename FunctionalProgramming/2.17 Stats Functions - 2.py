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

    # Calculate mean of x_list and y_list
    mean_x = mean(x_list)
    mean_y = mean(y_list)

    # Calculate standard deviation (sigma) of x_list and y_list
    sigma_x = sqrt(variance(x_list))
    sigma_y = sqrt(variance(y_list))

    # Calculate the numerator of the correlation coefficient formula
    numerator = sum(map(lambda x, y: (x - mean_x) * (y - mean_y), x_list, y_list))

    # Calculate the correlation coefficient
    correlation = numerator / (sigma_x * sigma_y)

    return correlation


# Example usage:
x_list = [1, 2, 3, 4, 5]
y_list = [2, 4, 6, 8, 10]

result = correlation_coefficient(x_list, y_list)
print("Correlation Coefficient:", result)
