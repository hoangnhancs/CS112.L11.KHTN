a, k, b, m, n = map(int, input().split())
sum = 0

def f(x):
    """
    :param x: số ngày 2 đội đã chặt cây
    :return: số cây 2 đội đã chặt trong x ngày
    """
    return (x - int(x // k)) * a + (x - int(x // m)) * b

result = int(n // ((1 - 1 / k) * a + (1 - 1 / m) * b)) - 1  # giải nghiệm

while (sum < n):
    sum = f(result)

    result += 1

print(result - 1)