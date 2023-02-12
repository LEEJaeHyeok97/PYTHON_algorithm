N = int(input())

card = list(map(int, input().split()))

M = int(input())

guess = list(map(int, input().split()))

ans = []

card.sort()

def binarySearch(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None



for i in guess:
    if binarySearch(card, i, 0, N - 1) == None:
        ans.append(0)
    else:
        ans.append(1)


print(*ans)