def func_a(bundle, start): #번갈아가면서 카드 뽑는 함수
    return bundle[start::2]

def func_b(score1, score2): #획득한 점수가 큰 사람과 점수를 리스트에 담는 함수
    if score1 > score2: #만약 1p가 2p 점수보다 크면
        return [1, score1] #리스트에 1p와 점수를 담음
    elif score2 > score1:# "
        return [2, score2]# "
    else: #무승부라면
        return [0, score1] #0을 리턴

def func_c(bundle): #A와 B가 획득한 점수를 구하는 함수
    answer = 0 #점수 카운트
    score_per_cards = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    }
    for card in bundle: #변수에 bundle 변수의 항목들을 넣으며 반복
        answer += score_per_cards[card] #card 인덱스가 c면 3점을 추가하는 식으로 answer에 점수를 추가함
    return answer #answer 리턴
        
def solution(n, bundle): #이긴사람과 점수를 구하는 함수
    a_cards = func_a(bundle,start=1)[:n]
    b_cards = func_a(bundle,start=2)[:n]
    a_score = func_c(a_cards)
    b_score = func_c(b_cards)
    return func_b(score1=a_score, score2=b_score)

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n = 4
bundle = "cacdbdedccbb"
ret = solution(n, bundle)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#수정 전:  File "D:\project\Python.git\Cos Pro 2\4차시\4차 2급 3_initial_code.py", line 26
#     a_cards = func_a(@@@, @@@)[:n]
#                      ^
# SyntaxError: invalid syntax

#수정 후:solution 함수의 반환 값은 [0, 13] 입니다.


#문제에서 원하는 내용:이긴 사람과 그 점수를 구하기