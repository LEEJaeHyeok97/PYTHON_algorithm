# 666, 1666, 2666, 3666, 4666, 5666, 6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668, 6669, 7666, 8666, 9666, 10666
#str()
n = int(input())

lst = []

i = 0
while(len(lst) != n):
    tmp = str(i)
    tmp2 = str(i)
    tmp2 = tmp2.replace('6', '*')
    if '***' in tmp2:
        lst.append(tmp)
    i+=1

print(lst[-1])