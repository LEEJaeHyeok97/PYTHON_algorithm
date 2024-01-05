from itertools import combinations

li = []

n = 4
k = 2

comb_generator = combinations(range(1, n + 1), k)

# 각 조합을 리스트로 변환하여 결과 리스트에 추가
for comb in comb_generator:
    li.append(list(comb))

print(li)