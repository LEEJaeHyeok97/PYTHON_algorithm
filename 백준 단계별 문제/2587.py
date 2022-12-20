l = []

for i in range(5):
    l.append(int(input()))


l.sort()

sum = 0

for i in l:
    sum += i

avg = int(sum / 5)
mid = l[2]


print(avg)
print(mid)