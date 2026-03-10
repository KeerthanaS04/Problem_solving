class Solution:
    def intToRoman(self, num: int) -> str:
        roman_symbols = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        decimal_values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

        result = []

        for symbol, value in zip(roman_symbols, decimal_values):
            while num>=value:
                num-=value
                result.append(symbol)
        return ''.join(result)