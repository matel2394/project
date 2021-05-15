# 1.print()_ 함수
#     정의 : 무언가를 출력할때 사용하는 함수이다
#     사용방법 :print() 함수를 이용해 괄호안에 "" 를 넣고 "" 안에 문자를 써서 콘솔에 출력해낼수 있다
#
# 2. type() int() str() float() 함수
#     정의 : 문자의 형태를 나타내는 함수이다
#     사용방법 : 타입은 해당 문자의 형태를 알아낼때 인트는 문자열을 정수로 바꾸거나 정수를 입력할때 str은 정수를 문자열로 바꿀때나 문자를
#              입력할때 사용되고 float은 유리수를 나타낼때 주로 사용된다
#
# 3. 인덱싱이란
#     리스트나 무언가의 순서를 나타내는것으로 원하는 정보의 번호를 입력하거나 특정 순서를 입력했을때 해당 번호의 인덱스가 호출된다
#
# 4. 슬라이싱
#     정의 : 문자나 정수 리스트등에서 일부만 가져오는것
#     사용방법 : 콜론(:X)를 이용해서 이름[:X] 이름[::X] 이름[Y:X] 처럼 Y부터 X까지,X까지 X부터 등으로 사용됨
# 5.replace() 함수
#     정의 : 지정한 텍스트나 인덱스부터의 문자열을 다른 문자열로 바꿔주는 함수
#     사용방법 : 변수(함수,리스트)이름.replace("A"," ")라고 한다면 A를 공백으로 바꾸겠다는 뜻이고 문자나 특정 문자를 바꿔야할때 사용된다
#
# 6.split():함수
#     정의:스플릿은 특정 문자를 기점으로 삼아 분리해주는 함수이다
#     사용방법:분리하려는 문자열의 특정 문자를 스플릿함수에 입력하여 사용 ex)변수이름.split("특정 문자")
# 7.formatting 이란
# 문자열 속 특정한 위치에 특정한 값을 삽입해 주는 것을 의미함 10을 문자열에 %s 를 이용해 넣을수있음
# 8.format() 함수
#     정의:문자열을 원하는 형태로 사용하고싶을때 사용하는 함수로 포맷 안에 있는 값을 다른방식으로 출력하고싶을때
#     사용방법:{}안에 숫자와 실수를 지정하여 넣을수있음 ex)print('숫자 : {}, 실수 : {}'.format(5, 0.5))
#
# 9.f-string
#     정의:문자열에서 특정 부분만 바꿀때 f string포매팅을 이용해 편하게 바꿔줄수있음
#     사용방법:문자열 맨 앞에 f를 붙여주고, 중괄호 안에 직접 변수 이름이나 출력하고 싶은것을 바로 넣으면 됨 f'문자열 {변수} 문자열'
# 10.strip() rstrip() lstrip()
#     정의:특정 문자를 제거하는 함수로 strip은 왼쪽 오른쪽에서 인자 제거 나머지 두개의 r l은 오른쪽 왼쪽을 나타낸다
#     사용방법:변수.xstrip으로 사용할수있음
# 11.upper() lower() capitalize() 함수
#     정의:문자열의 대소문자를 변경하고 구분하는 함수다
#     사용방법:변수.위 3개 함수 를 사용하면 모두 대문자,모두 소문자,앞글자만 대문자로 바꿀수있다
# 12.endwith() startwith() 함수
#     정의: 문자열의 앞이나 뒤의 단어가 그에 맞는지 검토하는 함수
#     사용방법: 변수.위 3개함수(단어)로 True와 False를 알수있다
# 13.리스트와 변수차이
#     리스트는 변수를 여러개 저장하는 상자이고 변수는 한개를 저장하는 상자다
# 14.append() insert() del 함수
#     정의:리스트에 추가하고,해당 순서를 가져오고,리스트의 항목을 지우는 함수
#     사용방법: 리스트.위 3개 함수 를 사용하면 추가하고,순서를 가져오고,지울수있다
# 15. max() min() sum() len() 함수
#     정의: 최댓값 최솟값 모두 더한값 리스트항목 갯수를 알수있게해주는 함수
#     사용방법: 리스트.위 함수 를 사용하면 최댓값 최솟값 모두 더한값 리스트항목 갯수를 알수있다
# 16. 데이터를 저장하는방법 4가지의 차이와 사용방법
# 16-1 변수:함수나 숫자,문자열을 저장하는것으로 변수이름 = (함수/숫자/문자열) 로 사용한다 변수를 다른곳에 호출해 사용가능하며
#      이런 함수나 수,문자열을 하나씩만 저장 가능하다. 변수에 변수를 저장하는것도 가능하다
# 16-2 리스트:함수나 숫자를 "여러개" 넣을수있다.함수를 여러개 저장도 가능하고 일반적인 문자열 수도 가능하다
#     리스트의 함수들은 상당히 많은데 len(리스트이름) 은 리스트안에 있는 항목의 수를 나타낸다 리스트이름.append(넣을 항목) 은 리스트에
#     넣을 항목을 추가한다 리스트이름.index()는 항목의 순서를 나타낸다 리스트이름[항목번호]는 리스트 내에있는 항목번호가 쓰인 항목을
#     호출한다 리스트이름[항목번호:항목번호2] 는 항목1부터 항목 2까지 나타내겠다는 뜻이다 리스트이름[::항목번호]는 항목번호부터 끝까지 모두 호출
#     하겠다는 뜻이다 del 리스트이름[항목번호]는 해당항목을 불러와서 삭제하겠다는 뜻이다 리스트이름[::-1]은 뒤에서부터 모두 호출하겠다는 뜻이다
#     리스트이름.sort는 오름,내림등 여러 요소에따라 정렬시키는 함수다 pop는 리스트의 요소를 꺼내는 함수다 리스트를 선언하고 이를 사용할수있다
# 16-3 딕셔너리:키와 값이 쌍으로 저장되는 형태의 리스트와 비슷한것으로 딕셔너리 = {키:값,키2:값2}
#     형태로 사용된다 리스트와는 다르게 중괄호를 사용하며 dict로 표시한다 del 과 update 로 딕셔너리 내의 항목을 수정할수있다
#     zip() 함수로 튜플이나 리스트를 추가가능하고 keys,value로 키 값을 지정할수있다
# 16-4 튜플: 튜플은 딕셔너리와 리스트와 달리 () 소괄호를 사용한다 튜플 안에 있는 값은 변경이 불가하며 삭제또한 지원되지 않는다 리스트와 마찬가지로
#     인덱싱이 가능하며 슬라이싱도 가능하다 튜플1 + 튜플2로 튜플 두개를 더해서 합할수도 있으며 튜플1 * 3을 한다면 튜플1의 내용이 3번 반복된다
#     len으로 튜플의 길이를 구할수 있다
#
# 16-5 튜플을 리스트로 바꾸는방법: list(tuple)
# 16-6 리스트를 튜플로 바꾸는방법: tuple(list)
#
# 튜플 언패킹이란
# 정의: 튜플에 있는 요소들을 변수에 나눠담는것
# 사용방법: a,b,c =(1,2,3) 으로 a는 1 b는 2..처럼 담을수있다
#
# 딕셔너리
# 딕셔너리에 리스트 추가방법은 딕셔너리명["키"]=값
# 키만 출력방법은 딕셔너리.keys
# 밸류는 딕셔너리.values
# 딕셔너리 두개 합치기는 딕셔너리1 + 딕셔너리2
# 튜플을 딕셔너리는 dict(zip(튜플1,튜플2))
# 리스트를 딕셔너리는 dict(zip(리스트1,리스트2))

#논리 : 맞는지 틀린지 판단
#연산자 :
    #산술 연산자: +더하기 - 빼기 *곱하기 /나누기 //나누기 몫 %나누기 나머지
    #비교 연산자 : >초과 < 미안 >= 이상 <= 이하 == 같다 != 같지않다
    #논리 연산자 : and[이면서] or [이거나] ! [부정]
    #대입 연산자 : = [오른쪽값을  왼쪽에 대입]
        # += [오른쪽값을 왼쪽값에 더하기 후 대입]
        # -= [오른쪽값을 왼쪽값에 더하기 후 대입]
        # *=,%/

    #if 논리:
    #   참[코드]
    #elif 논리2:
        #참2[코드2]
    #elif 논리3:
        #참3[코드3]
    #else:
    #   거짓[코드]

# if 논리:
#   참[코드]
# if 논리2:
#   참2[코드2]
# if 논리3:.
#   참3[코드3]

    #     if 논리:                               if 학년 = 3:
    #         if 논리:                                  if 성별=남:
    #             참[코드]                                  학년이 3이면서 남학생
    #         else:                                    else:
    #             거짓[코드]                                학년이 3이면서 여학생
    #     else:                                 else:
    #         if 논리:                                if 성별 = 남:
    #             참[코드]                                 3학년이 아니면서 남학생
    #         else:                                  else:
    #             거짓[코드]                                3학년이 아니면서 여학생
