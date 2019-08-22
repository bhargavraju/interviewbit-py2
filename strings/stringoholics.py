from fractions import gcd
def calc_time(n):
    time, total = 0, 0
    while 1:
        time += 1
        total += time
        if total % n == 0:
            return time


def calc_lcm(times):
    def find_lcm(num1, num2):
        gcd_num = gcd(num1, num2)
        lcm = int((num1 * num2)/gcd_num)
        return lcm

    lcm = times[0]
    for i in times[1:]:
      lcm = find_lcm(lcm, i)
    return lcm


class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(A):
        times = []
        for single_str in A:
            n = len(single_str)
            time = calc_time(n)
            times.append(time)
        ans = calc_lcm(times)
        return ans % (10**9 + 7)
