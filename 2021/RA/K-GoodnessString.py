N = int(input())
for i in range(N):
    l, k = input().split()
    l = int(l)
    k = int(k)
    string = input()
    counter = 0
    start = 0
    end = l - 1
    while start < end:
        if(string[start] != string[end]):
            counter = counter + 1
        start +=  1
        end -= 1
    steps = max(k, counter) - min(k, counter)
    print("Case #"+str(i+1)+": "+str(steps))
