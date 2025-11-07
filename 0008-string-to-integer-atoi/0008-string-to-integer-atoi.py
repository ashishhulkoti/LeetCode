class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31
        sign = 1
        number = 0
        i = 0
        print(INT_MAX)
        while i<len(s) and s[i] == " ":
            i+=1
        if i<len(s) and s[i] == "-":
            sign = -1
            i+=1
        elif i<len(s) and s[i] == "+":
            sign = 1
            i+=1
        while i<len(s) and s[i]=="0":
            i+=1
        while i<len(s) and s[i]>="0" and s[i]<="9":
            digit = ord(s[i]) - ord("0")
            if number > INT_MAX//10 or (number == INT_MAX//10 and digit > 7):
                if sign == -1:
                    return -1 * INT_MAX
                else:
                    return INT_MAX-1
            number = number*10 + digit
            i+=1
        return sign*number