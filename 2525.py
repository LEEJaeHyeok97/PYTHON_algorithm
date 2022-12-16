time = list(map(int, input().split(' ')))
amountTime = int(input())


time[1] = time[1] + amountTime


if(time[1] >= 60):
    time[0] += time[1] // 60
    time[1] = time[1] % 60

if(time[0] >= 24):
    time[0] = time[0] % 24

print(time[0], time[1])