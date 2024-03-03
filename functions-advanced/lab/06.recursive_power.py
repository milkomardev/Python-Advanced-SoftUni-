def recursive_power(n, p):
    if p == 1:
        return n

    return n * recursive_power(n, p - 1)

print(recursive_power(2, 10))
print(recursive_power(10, 100))