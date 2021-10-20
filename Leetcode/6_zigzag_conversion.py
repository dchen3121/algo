# QUESTION
# ZIGZAG conversion.
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        cycle_length = (numRows - 1) * 2
        result = ''

        for i in range(numRows):
            index = i
            while index < len(s):
                result += s[index]
                if i not in {0, numRows - 1} and index + cycle_length - i - i < len(s):
                    result += s[index + cycle_length - i - i]
                index += cycle_length

        return result

# IDEA:
# visit instead of storing to avoid additional storage. pattern recognition.

soln = Solution()
print(soln.convert("PAYPALISHIRING", 4))
print(soln.convert("PAYPALISHIRING", 3))
