import sys

n = sys.stdin.readline()

lst = list(map(int, sys.stdin.readline().split()))

lst2 = list(set(lst))

lst2.sort()

dict = {}

#사전 만들기
index = 0
for i in lst2:
    dict[i] = index
    index+=1


#압축 좌표 출력
for i in lst:
    if i in dict:
        print(dict[i], end=" ")
