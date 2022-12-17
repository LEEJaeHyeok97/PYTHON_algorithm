roomNum = int(input())

cnt = 1
count = 1
count_six = 6

while(roomNum > cnt):
    count += 1
    cnt += count_six
    count_six += 6

print(count)