def mean(iterable):
    """
    Calculates the mean (average) of the given iterable.
    """
    total = sum(iterable)
    return total / len(iterable)


def variance(iterable, mean_val):
    """
    Calculates the variance of the given iterable.
    """
    squared_diff = [(x - mean_val) ** 2 for x in iterable]
    return sum(squared_diff) / len(iterable)


def correlation_coefficient(x, y):
    """
    Calculates the correlation coefficient between two lists x and y.
    """
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    sigma_x = variance(x, mean_x) ** 0.5
    sigma_y = variance(y, mean_y) ** 0.5

    numerator = sum((xi * yi - mean_x * mean_y) for xi, yi in zip(x, y))
    denominator = sigma_x * sigma_y

    return numerator / denominator


# Example usage
X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]
result = correlation_coefficient(X, Y)
print(f"Correlation coefficient: {result:.4f}")
