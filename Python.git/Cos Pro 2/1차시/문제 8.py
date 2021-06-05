#문제 8
def solution(sentence):
    str = ''
    for c in sentence: #해당 문장을 문자 하나씩 c에 대입
        if c != '.' or c != ' ': #문자가 .이 아니거나 공백ㅇ 아니면. #여기서 or을 and로 바꿔주면 정답
            str += c #str에 문자 저장
    size = len(str) #합쳐진 문자 길이 구하기
    for i in range(size//2): # // : 몫  문자길이 //2
        if str[i] != str[size-1 - i]: #첫 문자와 마지막 문자가 다를경우
            return False                #팰린드롬 x
        return True #팰린드롬 O

sentence1 = "never odd or even"
ret1 = solution(sentence1)
print("solution 함수 결과",ret1)

sentence2 = "palindrome"
ret2 = solution(sentence2)
print("solution 함수결과",ret2)