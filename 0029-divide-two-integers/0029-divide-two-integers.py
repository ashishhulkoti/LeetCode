class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1 and dividend <= -(2**31 - 1):
                return 2**31 - 1
        
        quotient = 0
        signPositive = True
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            signPositive = False
        
        if dividend < 0:
            dividend = 0 - dividend
        if divisor < 0:
            divisor = 0 - divisor
        
        tmpDivisor = divisor
        tmpDividend = dividend
        while dividend >= divisor:    
            powD = 1
            while divisor + divisor <= dividend:
                divisor += divisor
                powD += powD
            quotient += powD
            dividend -= divisor
            divisor = tmpDivisor
        return quotient if signPositive else 0 - quotient