n = int(input())

for i in range(n):
    cnt = int(i)+1
    tmp = input().split()
    print("Case #" + str(cnt) + ":", end=" ")
    for j in tmp[::-1]:
        print(j, end=" ")
    print()