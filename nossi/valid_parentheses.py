# 짝을 스택에 넣어주는 방법으로 스택을 만든다.

def solution(s):
    stack = []
    for i in s:
        if i == '[':
            stack.append(']')
        elif i == '(':
            stack.append(')')
        elif i == '{':
            stack.append('}')
        elif stack and i == stack[-1]: #인덱스 에러 방지
            stack.pop()
        else:
            return False
    return not stack

print(solution("[((()))]"))