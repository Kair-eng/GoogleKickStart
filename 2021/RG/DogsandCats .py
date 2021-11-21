N = int(input())
for i in range(N):
    i += 1
    _, D, C, M = [int(predef) for predef in input().split()]
    string = input()
    for j, animal in enumerate(string):
        if animal == 'C' and C > 0:
            C -= 1
            if(j == len(string) - 1):
                print(f"Case #{i}: YES")
            continue

        if animal == 'D' and D > 0:
            D -= 1
            C += M
            if(j == len(string) - 1):
                print(f"Case #{i}: YES")
            continue

        if animal == 'D':
            print(f"Case #{i}: NO")
        else:
            passNoPass = "YES" if -1 == string.find('D', j+1) else "NO"
            print(f"Case #{i}: {passNoPass}")
        break
