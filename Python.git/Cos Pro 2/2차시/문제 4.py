import math
def solution(words):
    answer = ''
    for w in words:
        if len(w) >= 5:
            answer += w
        if len(answer) < 1:
            answer = "empty"
    return answer

words1 = ["my","favorite","color","is","violet"]
ret1 = solution(words1)

print("solution 함수의 변환값은 ",ret1)

words2 = ["yes","i","am"]
ret2 = solution(words2)

print(ret2)