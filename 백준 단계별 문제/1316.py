n = int(input())

count = 0
cnt = n

while(True):
    if(count == n):
        break

    str = input()

    for i in range(len(str) - 1):
        if(str[i] == str[i+1]):
            pass
        elif(str[i] in str[i+1:]):
            cnt -=1
            break

    count+=1

print(cnt)