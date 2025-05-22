calls = 0


def fib(n):
    global calls
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_o1(n):
    phi = (1.0 + 5.0 ** (1 / 2)) / 2
    return (phi ** n) / (5.0 ** (1 / 2)) - ((1 - phi) ** n) / (5.0 ** (1 / 2))


def fib_on(n):
    if n < 2:
        return n
    f0 = 0
    f1 = 1
    fn = 0

    for i in range(n):
        fn = f0 + f1
        f0 = f1
        f1 = fn
    return fn


n = 8
print(f"Recursive: {fib(n)}, o(1): {fib_o1(n)}, o(n): {fib_on(n)}")
print(f"Lower: {2 ** (n / 2)}, real: {calls}, upper: {2 ** n}, calls2: {2 * fib_on(n + 1) - 1}")
