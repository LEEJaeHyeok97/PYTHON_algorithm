import sys
n, l = map(int, input().split())

# print(n, l)
li = []
li2 = []
li3 = []

li = input().split()
for i in li:
    li2.append(int(i))

li2.sort()
# print(li2)

for i in li2:
    if l >= i:
        l+=1
    else:
        li3.append(i)
    for j in li3:
        if l >= j:
            j+=1

print(l)