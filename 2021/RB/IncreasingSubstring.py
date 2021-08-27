N = int(input())

for I in range(N):
    length =  int(input())
    string = input()
    counter = 1
    numbers = [str(counter)]
    i,j = 0,1
    while j < length:
        if string[i] < string[j]:
            counter += 1
        else:
            counter = 1
        i += 1
        j += 1
        numbers.append(str(counter))
    print(f"Case #{I + 1}: {' '.join(numbers)}")