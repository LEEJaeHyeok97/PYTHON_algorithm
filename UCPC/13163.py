n = int(input())


for i in range(n):
    li = input().split()
    li[0] = "god"
    for _ in li:
        print(_, end="")
    print()