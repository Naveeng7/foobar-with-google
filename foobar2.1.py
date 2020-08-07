def solution(x, y):
    # Your code here

    vd = 0
    for i in range(1, x + 1):
        vd = vd + i

    lst = list()
    hv = 1
    for i in range(0, y + 1):
        hv = i + hv
        lst.append(hv)

    lst1 = list()
    for i in range(len(lst) - 1):
        diff = lst[i + 1] - lst[i]
        lst1.append(diff)

    for i in range(1, y):
        nele = lst1[i - 1]
        nele = nele + (x - 1)
        vd = vd + nele

    return str(vd)


