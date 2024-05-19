# answers = list(map(int, input().strip('[]').split(',')))

# sp_1 = [1, 2, 3, 4, 5]
# sp_2 = [2, 1, 2, 3, 2, 4, 2, 5]
# sp_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

# cnt = 1
# while True:
#     sp_1 = sp_1 * cnt
#     if len(answers) <= len(sp_1):
#         break

#     cnt +=1

# cnt = 1
# while True:
#     sp_2 = sp_2 * cnt
#     if len(answers) <= len(sp_2):
#         break

#     cnt +=1

# cnt = 1
# while True:
#     sp_3 = sp_3 * cnt
#     if len(answers) <= len(sp_3):
#         break

#     cnt +=1


# cor_1 = 0
# cor_2 = 0
# cor_3 = 0

# for i, v in enumerate(answers):
#     if v == sp_1[i]:
#         cor_1+=1

# for i, v in enumerate(answers):
#     if v == sp_2[i]:
#         cor_2+=1

# for i, v in enumerate(answers):
#     if v == sp_3[i]:
#         cor_3+=1




# ans = []
# ans.append([1, cor_1])
# ans.append([2, cor_2])
# ans.append([3, cor_3])

# ans.sort(key=lambda x: x[1], reverse=True)

# print(ans)

# prev = ans[0]
# f_ans = []
# f_ans.append(prev[0])
# for i in ans[1:]:
#     if i[1] == prev[1]:
#         f_ans.append(i[0])

# print(f_ans)


def solution(answers):
    sp_1 = [1, 2, 3, 4, 5]
    sp_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sp_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt = 1
    while True:
        sp_1 = sp_1 * cnt
        if len(answers) <= len(sp_1):
            break

        cnt +=1

    cnt = 1
    while True:
        sp_2 = sp_2 * cnt
        if len(answers) <= len(sp_2):
            break

        cnt +=1

    cnt = 1
    while True:
        sp_3 = sp_3 * cnt
        if len(answers) <= len(sp_3):
            break

        cnt +=1


    cor_1 = 0
    cor_2 = 0
    cor_3 = 0

    for i, v in enumerate(answers):
        if v == sp_1[i]:
            cor_1+=1

    for i, v in enumerate(answers):
        if v == sp_2[i]:
            cor_2+=1

    for i, v in enumerate(answers):
        if v == sp_3[i]:
            cor_3+=1




    ans = []
    ans.append([1, cor_1])
    ans.append([2, cor_2])
    ans.append([3, cor_3])

    ans.sort(key=lambda x: x[1], reverse=True)


    prev = ans[0]
    f_ans = []
    f_ans.append(prev[0])
    for i in ans[1:]:
        if i[1] == prev[1]:
            f_ans.append(int(i[0]))

    return f_ans
    