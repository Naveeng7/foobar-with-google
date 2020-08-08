def solution(xs):
    pro = 1
    xs.sort()
    pos = list()
    neg = list()

    for i in range(len(xs)):
        ele = xs[i]
        if ele > 0:
            pos.append(ele)
        elif ele < 0:
            neg.append(ele)

    if len(xs) == 1:
        return str(xs[0])

    elif len(pos) > 0 and len(neg) > 1:
        if len(neg) % 2 != 0:
            neg.pop()
        for i in pos:
            pro = pro * i
        for i in neg:
            pro = pro * i

    elif len(pos) > 0:
        for i in pos:
            pro = pro * i

    elif len(neg) > 1:
        if len(neg) % 2 != 0:
            neg.pop()
        for i in neg:
            pro = pro * i

    return str(pro)

xs =[1]
print(solution(xs))