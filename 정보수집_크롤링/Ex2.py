# from bs4 import  BeautifulSoup as bs #html 언어 읽어주는 함수 제공
# import urllib.request as ur
# import urllib
#     # URL : 인터넷 주소 : www.naver.com
#
# #1. 크롤링 할 인터넷 주소 넣어주기
# url = 'https://movie.naver.com/movie/running/current.nhn'
#
# #2. 주소 열어서 웹문서 변수에 저장
# 웹문서 = ur.urlopen(url)
#
# #3. 웹문서 변수 읽기
# soup =bs(웹문서.read(),'html.parser')
#
# #4. 해당 태그를 찾아서 가져오기
# 태그 = soup.find_all('ul',{"class":"current_list"})
#
# print(태그)
#
# ###
from bs4 import  BeautifulSoup as bs #html 언어 읽어주는 함수 제공
import urllib.request as ur
    # URL : 인터넷 주소 : www.naver.com

#1. 크롤링 할 인터넷 주소 넣어주기
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'

#2. 주소 열어서 웹문서 변수에 저장
웹문서 = ur.urlopen(url)

#3. 웹문서 변수 읽기
soup =bs(웹문서.read(),'html.parser')

#4. 해당 태그를 찾아서 가져오기
태그 = soup.find_all('div',{"class":"tit3"})

print(태그)
#
# ###
# from bs4 import  BeautifulSoup as bs #html 언어 읽어주는 함수 제공
# import urllib.request as ur
#     # URL : 인터넷 주소 : www.naver.com

# from bs4 import  BeautifulSoup as bs #html 언어 읽어주는 함수 제공
# import urllib.request as ur
# import urllib
#
# #1. 크롤링 할 인터넷 주소 넣어주기
# 지역 = input("지역:")
# 검색어 = urllib.parse.quote(지역+'날씨')
#
# url = 'https://search.naver.com/search.naver?ie=utf8&query=' + 검색어
#
# #2. 주소 열어서 웹문서 변수에 저장
# 웹문서 = ur.urlopen(url)
#
# #3. 웹문서 변수 읽기
# soup =bs(웹문서.read(),'html.parser')
#
# #4. 해당 태그를 찾아서 가져오기
# 온도 = soup.find_all('span',{"class":"todaytemp"})
# 미세먼지 = soup.find_all('dd',{"class":"lv1"})
# 오존 = soup.find_all('dd',{"class":"lv2"})
#
# print("온도:",온도[0].text,"도")
# print("미세먼지:",미세먼지[0].text)
# print("오존:",오존[0].text)

###
#자동차 모델을 입력받아 출시가 출력하기
from bs4 import BeautifulSoup as bs
import urllib.request as ur
import urllib
while True:
    모델 = input("모델명:")
    검색어 = urllib.parse.quote(모델)

    url = 'https://search.naver.com/search.naver?ie=utf8&query='+검색어

    웹문서 = ur.urlopen(url)

    soup =bs(웹문서.read(),'html.parser')
    가격 = soup.find_all('span',{"class":""})
    찾는문자 = "판매"
    for i in 가격:
        b =찾는문자 in i.text
        if b:
            print(i.text)

