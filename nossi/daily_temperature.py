def solution(s):
    stack = []
    ans = [0] * len(s)  # 결과를 저장할 리스트 초기화

    for i, val in enumerate(s):
        while stack and val > s[stack[-1]]:
            top = stack.pop()
            ans[top] = i - top
        stack.append(i)

    return ans

print(solution([73,74,75,71,69,72,76,73]))
