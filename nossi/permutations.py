from itertools import permutations

my_list = [1, 2, 3]
perm_generator = permutations(my_list, 2)  # my_list에서 2개의 요소로 가능한 모든 순열을 생성하는 제너레이터
ans = []

# 제너레이터를 리스트로 변환
for i in perm_generator:
    ans.append(list(i))

print(ans)