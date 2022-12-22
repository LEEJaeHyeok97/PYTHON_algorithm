#최빈값 수정중

import sys

l = []
count = [0]* 8001

n = int(input())

for i in range(n):
    l.append(int(sys.stdin.readline()))


l.sort()

sum = 0
#산술평균
for i in l:
    sum +=i

ans1 = round(sum / len(l))
print(ans1)

#중앙값
center = int(len(l)/2)
print(l[center])


#최빈값
for i in l:
    if i > 0:
        count[i+4000] +=1
    else:
        count[-1*i] +=1

max1 = 0
max2 = 0
max = 0
for i in range(len(count)):
    if i > max1:
        max1 = i
        count[max1] = 0
for i in range(len(count)):
    if i > max2:
        max2 = i

if max1 == max2:
    max = max2
else:
    max = max1

if max > 4000:
    max = int(max - 4000)
else:
    max = -1 * max

print(max)



#범위
print(l[-1] - l[0])


