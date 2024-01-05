from itertools import combinations

def solution(relation):
    col = len(relation[0])
    all_case = []
    for i in range(1, col+1):
        all_case.extend(combinations(range(col), i))

    unique = []
    for case in all_case:
        temp = ["".join(relate[int(idx)] for idx in case) for relate in relation]
        if len(set(temp)) == len(relation):
            unique.append(case)
    
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]).intersection(set(unique[j]))):
                answer.discard(unique[j])

    return len(answer)