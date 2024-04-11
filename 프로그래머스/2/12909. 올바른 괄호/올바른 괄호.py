def solution(s):
    cnt = 0
    for c in s:
        if c == '(':
            cnt+=1
        elif not cnt:
            return False
        else:
            cnt-=1
    if not cnt:
        return True
    return False