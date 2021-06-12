#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(words, word): #words와 word를 파라미터로 사용하는 solution함수
    count = 0 #count 변수에 0 대입
    l = len(word) #l 변수에 word의 글자수 길이인 3 대입
    for i in words: #i변수에 words 내용 대입
        for q in range(l): #q 변수에 word의 글자수만큼 반복
            if i[q] != word[q]: #만약 words의 q번째 인덱스가 word의 q번째 인덱스와 다르면
                count+=1 #count에 1 추가
    return count #count 변수 리턴

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
words = ["CODE", "COED", "CDEO"]
word = "CODE"
ret = solution(words, word)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")