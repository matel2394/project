#211번
print("211번")
print("안녕")
print("Hi")
#212번
print("212번")
print(7)
print(15)
#213번
print("213번")
print("파라미터가 사용자의 입력 문자인데 공백으로 두었기때문에 오류가 나는것")
#214번
print("214번")
print("산술연산자는 임의변수가 모두 int타입일때만 작동하기때문에 str타입인 문자열 안녕과 충돌한것이다")
#215번
print("215번")
def 스마일(대답):
    print(대답+ ":D")
#216번
print("216번")
스마일("안녕하세요")
#217번
print("217번")
def 가격(현재가격):
    print(현재가격 * 30/100)
가격(100)#써야되서 그냥 파라미터값 100으로 지정
#218번
print("218번")
def 덧셈(a,b):
    print(a+b)
덧셈(4,5)
#219번
print("219번")
def 사칙연산(a,b):
    print(a+b)
    print(a - b)
    print(a * b)
    print(a / b)
사칙연산(3,4)
#220번
print("220번")
def 큰수(a,b,c):
    if a>b and a>c:
        print(max(a,b,c))
    if b>a and b>c:
        print(max(a,b,c))
    if c>a and c>b:
        print(max(a,b,c))
큰수(4,7,2)
