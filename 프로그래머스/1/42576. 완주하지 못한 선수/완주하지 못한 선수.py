def solution(participant, completion):
    dic = {}
    for p in participant:
        if p in dic.keys():
            dic[p] += 1
        else:
            dic[p] = 1

    for c in completion:
        dic[c] -= 1
        if not dic[c]:
            dic.pop(c)
    return list(dic.keys())[0]
