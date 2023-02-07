s = input()

stck = []
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        stck.append('(')
    elif s[i] == ')':
        if s[i-1] == '(':
            stck.pop()
            ans += len(stck)
        else:
            stck.pop()
            ans += 1

print(ans)