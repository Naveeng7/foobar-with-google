import time
import math

def solution(n):
    solution.conter = 0
    lst = [0] * n

    def proces(lst, nextindex, n, redsize, conter):
        if redsize < 0:
            return
        nlst = list()
        if redsize == 0 :
            for i in range(nextindex):
                nlst.append(lst[i])
            dist = 1
            for i in range(len(nlst)):
                for j in range(len(nlst)):
                    if i != j:
                        if nlst[i] == nlst[j]:
                            dist = 0
            if len(nlst) >= 2 and dist == 1:
                if sum(nlst) == n:
                    solution.conter = solution.conter + 1
            nlst.clear()
            return

        if (nextindex == 0):
            pre =1
        else :
            pre = lst[nextindex-1]

        for k in range(pre, n+1):
            lst[nextindex] = k
            print('running')
            proces(lst, nextindex+1, n, redsize-k, solution.conter)


    proces(lst, 0, n, n, solution.conter)
    return solution.conter

n = 200
s = time.time()
print(solution(n))
e = time.time()
print('timetaken',math.floor(e-s),'seconds')