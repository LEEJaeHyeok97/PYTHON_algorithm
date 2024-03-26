N, M = map(int, input().split())

# print(N, M)

s = []

for i in range(N):
    s.append(input())

s2 = set(s)

ans = []

for i in range(M):
    word = input()
    if word in s2:
        ans.append(word)

print(len(ans))