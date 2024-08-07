memo = {

}
def w(a, b, c):
    if (a, b, c) in memo:
        return memo[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    elif a < b and b < c:
        w_num = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        memo[(a, b, c)] = w_num
        return w_num

    else:
        w_num = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        memo[(a, b, c)] = w_num
        return w_num



while True:
    a, b, c = map(int, input().split(' '))

    if a == -1 and b == -1 and c == -1:
        break

    res = w(a, b, c)


    print(f"w({a}, {b}, {c}) = {res}")