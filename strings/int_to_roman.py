def intToRoman(self, A):
    ref = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman = ''
    while A > 0:
        for i, r in ref:
            while A >= i:
                roman += r
                A -= i
    return roman
