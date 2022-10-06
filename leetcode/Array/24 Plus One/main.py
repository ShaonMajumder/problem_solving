class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        n = length
        carry = 1
        for i in range(0,length):
            digit = digits[length-1-i]
            if digit + carry >= 10:
                digits[length-1-i] = 0
                carry = 1
            else:
                digits[length-1-i] = digit + 1
                return digits
        digits = [carry] + digits
        return digits