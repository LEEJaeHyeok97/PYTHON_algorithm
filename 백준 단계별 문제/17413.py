import sys
from collections import deque

s = sys.stdin.readline().strip() + " "

is_in_tag = 0

st = deque()

result = ''

for i in s:
    if i == '<':
        for _ in range(len(st)):
            result += st.pop()
        is_in_tag = 1
    st.append(i)

    if i == '>':
        for _ in range(len(st)):
            result += st.popleft()
        is_in_tag = 0

    if i == ' ' and is_in_tag == 0:
        st.pop()
        for _ in range(len(st)):
            result += st.pop()
        result += ' '

print(result)
