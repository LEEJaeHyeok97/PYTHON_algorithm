import sys

N = int(sys.stdin.readline())


def recursion(s, l, r):
    global count
    #함수 안에서 전역 변수를 쓸때는 위와 같이 global 변수를 명시해야 한다
    if(l >= r):
        return 1
    elif(s[l] != s[r]):
        return 0
    else:
        count+=1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for i in range(N):
    count = 1
    s = sys.stdin.readline().strip()
    print(isPalindrome(s), count)
