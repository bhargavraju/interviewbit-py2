def solve(A):
    ans = []
    for i in range(A):
        sol = [1]
        if ans:
            prev = ans[-1]
            for j in range(len(prev) - 1):
                sol.append(prev[j] + prev[j + 1])
        if i != 0:
            sol.append(1)
        ans.append(sol)
    return ans


ans = solve(4)
print ans
