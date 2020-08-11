def solution(n):
    solution.sm = n
    lst = [0] * n
    solution.conter = 0

    def recur(i, n, lst, index):
        if n == 0:
            if len(lst[:index]) >= 2 and sum(lst[:index]) == solution.sm:
                solution.conter = solution.conter + 1
        for j in range(i, n + 1):
            lst[index] = j
            if lst[index] == lst[index - 1]:
                continue
            else:
                recur(j, n - j, lst, index + 1)

    recur(1, n, lst, 0)
    return solution.conter
