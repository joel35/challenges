def find_number_pairs(numbers, N=10):
    pairs = []
    for i, n1 in enumerate(numbers):
        for x in range(1, len(numbers) - i):
            n2 = numbers[i + x]
            if n1 + n2 == N:
                pairs.append((n1, n2))
    return pairs
