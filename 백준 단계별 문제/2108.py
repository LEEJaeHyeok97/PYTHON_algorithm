import sys
input = sys.stdin.readline

n = int(input())

li = []
for i in range(n):
    li.append(int(input()))


li.sort()

# print(li)

ans1 = int(round(sum(li) / len(li), 0))
print(ans1)

ans2 = li[len(li)//2]
print(ans2)

ans3 = {}
for i in li:
    if i not in ans3:
        ans3[i] = 1
    else:
        ans3[i] += 1

max_cnt = max(ans3.values())
max_arr = sorted([k for k, v in ans3.items() if v == max_cnt])

if len(max_arr) == 1:
    print(max_arr[0])
else:
    print(max_arr[1])






if len(li) == 1:
    print(0)
else:
    print(li[-1] - li[0])

##############################################
# dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2}
# max_cnt = 2
#
# max_arr = sorted([k for k, v in dict.items() if v == 1])
#
# print(max_arr)


