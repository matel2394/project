#You may use import as below.
#import math

def solution(price, grade):
    answer = 0
    for i in range(3):
        if grade == "S":
            answer = price * 95//100
        if grade == "G":
            answer = price*90//100
        if grade == "V":
            answer = price*85//100
    return answer

#The following is code to output testcase.
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")