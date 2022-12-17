n = int(input())
numberList = list(map(int, input().split(' ')))
searchNum = int(input())

count = 0

for i in numberList:
    if(i == searchNum):
        count+=1

print(count)