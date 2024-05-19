
s = input()

cnt_0 = 0
cnt_1 = 0

prev = int(s[0])


#0으로 만들 시
if prev == 1:
    cnt_0 = 1
else:
    cnt_0 = 0

for i in s[1:]:
    i = int(i)
    if prev == i or i == 0: 
        prev = i
        continue
    else:
        cnt_0 += 1
        prev = i



#1로 만들 시
prev = int(s[0])

if prev == 1:
    cnt_1 = 0
else:
    cnt_1 = 1

for i in s[1:]:
    i = int(i)
    if prev == i or i == 1:
        prev = i
        continue
    else:
        cnt_1 += 1
        prev = i


print(min(cnt_0, cnt_1))