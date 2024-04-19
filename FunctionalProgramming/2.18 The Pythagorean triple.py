def findTheTriple():
    target_sum = 1000

    # We will find suitable m and n
    for m in range(1, int(target_sum ** 0.5) + 1):
        for n in range(1, m):  # ensure n < m
            if 2 * m * (m + n) == 1000:
                a = m ** 2 - n ** 2
                b = 2 * m * n
                c = m ** 2 + n ** 2
                if a + b + c == target_sum:
                    return {a, b, c}

    return None


# Testing the function
result = findTheTriple()
print(result)
