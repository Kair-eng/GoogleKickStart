N = int(input())

for I in range(N):
    length = int(input())

    sequence = [int(i) for i in input().split()]
    if length <= 3:
        print(f"Case #{I + 1}: {length}")
        continue
    numbers = []
    # (Start,End,Diff,Size)

    start, j = 0, 1
    diff = sequence[j] - sequence[j - 1]

    while j < length:
        if diff == sequence[j] - sequence[j - 1]:
            pass
            # do nothing
        else:
            numbers.append((start, j - 1, diff, (j - 1) - start + 1))
            diff = sequence[j] - sequence[j - 1]
            start = j - 1
        j += 1
    numbers.append((start, j - 1, diff, (j - 1) - start + 1))

    # Count
    j = 0
    maximum = numbers[0][3]
    while j < len(numbers):
        start, end, diff, size = numbers[j]
        if len(numbers) > 1 and maximum < size + 1:
            maximum = size + 1

        leftVal = sequence[start] - diff
        rightVal = sequence[end] + diff

        # Check left side
        if j - 3 >= 0 and numbers[j - 1][3] == 2 and numbers[j - 2][3] == 2 and leftVal - diff == sequence[start - 2] and diff == numbers[j - 3][2]:
            #guess is right
            if maximum < size + 1 + numbers[j - 3][3]:
                maximum = size + 1 + numbers[j - 3][3]
        if start - 2 >= 0 and leftVal - diff == sequence[start - 2]:
            #guess is right
            if maximum < size + 2:
                maximum = size + 2

        # Check right side
        if j + 3 < len(numbers) and numbers[j + 1][3] == 2 and numbers[j + 2][3] == 2 and leftVal + diff == sequence[end + 2] and diff == numbers[j + 3][2]:
            #guess is right
            if maximum < size + 1 + numbers[j + 3][3]:
                maximum = size + 1 + numbers[j + 3][3]
        if end + 2 < length and rightVal + diff == sequence[end + 2]:
            #guess is right
            if maximum < size + 2:
                maximum = size + 2
        j += 1

    print(f"Case #{I + 1}: {maximum}")
