#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(words, word):
    count = 0
    l = len(word)
    for i in words: #i = code , coed, cdeo
        for q in range(l): # j = c,o,d,e,c,o,e,d,c,d,e,o
            if i[q] != word[q]:
                count += 1

    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
words = ["CODE", "COED", "CDEO"]
word = "CODE"
ret = solution(words, word)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")