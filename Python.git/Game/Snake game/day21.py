    #모든 줄에 주석 넣기
# 1.pygame 설치
import pygame #파이게임 불러오기
from pygame.locals import QUIT , Rect , KEYDOWN , K_UP , K_LEFT , K_RIGHT , K_DOWN #파이게임으로부터 여러 동작이벤트를 불러옴
                         #종료    #직각  #키 눌렀을때 #위방향 #좌향 키   #우향 키   #아랫방향 키
import sys #시스템 파일 불러오기
import random #랜덤 함수 가져오기
점수 = 0
프레임수 = 5
점수1 = 10

#############################################################################
#2.게임에 필요한 기본설정
pygame.init() #파이게임 기본값
화면 = pygame.display.set_mode( (1000,1000) ) #화면 구성
프레임 = pygame.time.Clock() #시간 체크

#############################################################################
음식 = [] #포인트 리스트 선언
뱀 = []    #뱀 몸통 리스트 선언
배경 = pygame.image.load('down.jpg')
pygame.mixer.music.load('background-loop-straight-04-2699.mp3')
pygame.mixer.music.play(-1)
(가로,세로) = (50,50) #가로세로 높이 지정]
#3.함수 생성###################################################################
#3-1 음식만들기 함수 -뱀이 음식을 먹었을때 새로 음식 추가
def 음식만들기(): #음식만들기 이름의 함수 디파일0
    while True: #무한반복
        음식위치 = (random.randint(0,가로-1),random.randint(0,세로-1))# 가로와 세로의 0~49까지의 위치에 난수로 위치 지정)
        if 음식위치 in 음식 or 음식위치 in 뱀: #만약 음식위치 안에 음식이 있거나 뱀이 있다면
            continue #다시 실행
        음식.append(음식위치) #포인트 리스트에 음식위치를 추가해줌
        break #반복 끝내기
#############################################################################
#3-2 음식 위치 함수 - 뱀이 음식을 먹었을떄
def 음식움직임(음식위치): #음식을 다른위치로 바꾸는 함수 디파일
    i = 음식.index(음식위치) #i라는 변수에 포인트 리스트에있는 음식 위치의 번호 저장
    del 음식[i] #포인트 리스트에 있는 i에 들어있는 음식위치의 순서에 있는 음식위치를 지움
    음식만들기() #3-1의 음식만들기 함수 호출
#############################################################################
#3-3 음식 그리기 함수 - [좌표,화면,음식]
def 그리기(점수판,게임종료): #그리기 이름의 함수 디파일


    #음식 그리기
    for food in 음식: #리스트내 갯수 입력
        pygame.draw.ellipse(화면,(0,255,0 ) ,  Rect(food[0] * 20, food[1]*20,20,20)) #ellipse로 원을 그리고 20의 사이즈로 음식을 그림

    #뱀 그리기
    for body in 뱀: #리스트내 갯수 입력
        pygame.draw.rect(화면, (255, 255, 0), Rect(body[0] * 20, body[1]*20,20,20)) #rect로 사각형 그리고 20의 크기로 뱀 그리기

    #점수 그리기
    if 점수 != None: #점수에 내용이 있으면
        화면.blit(점수판,(10,10))

    #종료 메세지 그리기
    if 게임종료 : # 게임종료메세지가 내용이 있으면
        게임종료메세지 = my글꼴.render("게임종료[획득점수는:" + str(점수) + "]" ,True,(255,255,255))
        화면.blit(게임종료메세지,(300,500)) #x좌표 y좌표에 쓰기

    pygame.display.update() #화면을 그리는대로 실시간 재로딩함
##########################################################################################
#4.게임실행
my글꼴 = pygame.font.SysFont("malgungothic", 60) #글꼴,글자크기
키 = K_DOWN #아래키
게임종료 = False
뱀.append( (int(세로/2), int(가로/2))) #뱀을 화면 가운데 배치
점수 = 0 #점수변수 선언
게임종료메세지 = 0 #게임종료메세지 변수 선언
for i in range(400): #30번 반복
    음식만들기() #음식만들기 함수 호출
while True:#무한반복
    화면.blit(배경,(0,0))
    for 동작 in pygame.event.get(): #파이게임 이벤트[동작] 있을경우
        if 동작.type == QUIT: #이벤트가 종료이면
            pygame.quit() #파이게임 종료
            sys.exit() #시스템[모든코드] 종료
        elif 동작.type == KEYDOWN : #키를 눌렀을때
            키 = 동작.key #키 변수에 동작키를 대입
#######################################################################
    #키를 눌렀을때
    if not 게임종료 : #게임종료가 False이면
        if 키 == K_LEFT: #만약 키가 왼쪽키라면
            머리 = (뱀[0][0]-1,뱀[0][1]) #x좌표를 -1 바꿈

        elif 키== K_RIGHT: #만약 키가 오른쪽키라면
            머리 = (뱀[0][0] + 1,뱀[0][1]) #x좌표를 1 바꿈

        elif 키== K_UP: #만약 키가 윗쪽키라면
            머리 = (뱀[0][0] ,뱀[0][1]-1) #y좌표를 -1 바꿈

        elif 키== K_DOWN: #만약 키가 아랫쪽키라면
            머리 = (뱀[0][0] ,뱀[0][1]+1) #y좌표를 1 바꿈

        if 머리 in 뱀 or 머리[0] < 0 or 머리[0] > 세로 or 머리[1] < 0 or 머리[1] > 가로: #만약 머리가 뱀 안에있거나 머리가 0보다 작거나 가로세로보다 크면

            게임종료 = True #게임종료를 트루로 바꾸기
###################################################################################
        #뱀 머리 추가
        뱀.insert(0,머리) #머리 추가
#########################################################
        #음식을 먹었을때 꼬리 추가 아니면 추가 X
        if 머리 in 음식: #만약 머리가 음식 안에 있다면
            음식움직임(머리) #3-2번 함수 호출
            점수 += 1 #점수변수에 1점추가

        else:
            뱀.pop() #리스트내 가장 뒤에있는 항목 제거
        점수판 = my글꼴.render("먹은횟수:" + str(점수), True, (255, 255, 0))  # 점수판변수에 my글꼴을 렌더링해서 먹은횟수와 점수를 넣음
####################################################################################################

    그리기(점수판,게임종료) #3-3 그리기함수 호출
    프레임.tick(점수//10*5 + 5) #초당5프레임
