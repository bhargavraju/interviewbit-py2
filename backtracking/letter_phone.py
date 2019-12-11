"""
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.
"""
ref = {
    '0': ['0'],
    '1': ['1'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


def combinations(string):
    if len(string) == 1:
        return ref[string]
    curr = string[0]
    next_comb = combinations(string[1:])
    combs = []
    for el in ref[curr]:
        combs += [el + comb for comb in next_comb]
    return combs


# @param A : string
# @return a list of strings
def letterCombinations(A):
    result = combinations(A)
    return sorted(result)
