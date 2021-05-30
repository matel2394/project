#네이버 검색 Api 이용한 json 가공 프로그램
#Json : 키-값 => 한쌍 <- 딕셔너리와 유사

import os
import sys
import urllib.request
import json
import re

#네이버 검색함수
def 네이버검색(카테고리,검색결과물): #함수 만들기
    클라이언트id = "1lsGnepQrJ8pW449LsIN"
    클라이언트secret = "8vtuuvBdFs"
    # 검색결과물 json 으로 가져오기
    url = "https://openapi.naver.com/v1/search/" + 카테고리+".json"

    option = "&display=" +검색결과수+"&sort=count" #display : 출력 갯수 : 검색결과 수
    query = "?query="+urllib.parse.quote( input(카테고리 + "검색 정보 입력:") )
    url_query = url + query + option
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id", 클라이언트id)
    request.add_header("X-Naver-Client-Secret", 클라이언트secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

    검색결과 = response_body.decode('utf-8')  # 한글 지원
    json결과 = json.loads(검색결과)
    # 검색 결과 가공하기

    for i in json결과['items']:
        타이틀 = re.sub('<,+?>', '', i['title'], 0, re.I | re.S)
        print("----> 검색결과:"+타이틀)

        if 카테고리 == "shop":
            print( "---->최저가:",i['lprice'] )
        if 카테고리 == "movie":
            print( "---->배우:",i['actor'])
            print( "---->최저가:",i['userRating'])
        if 카테고리 == "news":
            print( "---->주요내용:",i['description'])
# 선택 제어
while True:
    print("검색[naverAPI] 프로그램")
    print("카테고리[1.뉴스 2.쇼핑 3.도서 4.영화 5.사전] 0.종료")
    선택 = int(input("선택:"))  # 입력받아 선택변수에 저장
    if 선택 == 1:
        카테고리 = "news"
        검색결과수 = input("-> 뉴스 선택 됐습니다. 몇개출력할까요?")
        네이버검색(카테고리,검색결과수) #함수 불러내기
    if 선택 == 2:
        카테고리 = "shop"
        검색결과수 = input("-> 쇼핑 선택 됐습니다. 몇개출력할까요?")
        네이버검색(카테고리, 검색결과수)
    if 선택 == 3:
        카테고리 = "book"
        검색결과수 = input("-> 도서 선택 됐습니다. 몇개출력할까요?")
        네이버검색(카테고리, 검색결과수)
    if 선택 == 4:
        카테고리 = "movie"
        검색결과수 = input("-> 영화 선택 됐습니다. 몇개출력할까요?")
        네이버검색(카테고리, 검색결과수)
    if 선택 == 5:
        카테고리 = "encyclopedia"
        검색결과수 = input("-> 사전 선택 됐습니다. 몇개출력할까요?")
        네이버검색(카테고리, 검색결과수)
    if 선택 == 0:
        print("-> 이용해주셔서 감사합니다")
        break #반복문 종료:
