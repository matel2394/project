import os
import sys
import urllib.request
import json
import re

def 네이버검색(카테고리,검색결과물):
    클라이언트id = "1lsGnepQrJ8pW449LsIN"
    클라이언트secret = "8vtuuvBdFs"

    url = "https://openapi.naver.com/v1/search/" + 카테고리+".json"

    option = "&display=" +검색결과수+"&sort=count"
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

    검색결과 = response_body.decode('utf-8')
    json결과 = json.loads(검색결과)
    # 검색 결과 가공하기

    for i in json결과['items']:
        타이틀 = re.sub('<,+?>', '', i['title'], 0, re.I | re.S)
        print("----> 검색결과:"+re.sub('<.+?>', '', 타이틀, 0, re.I | re.S) )


        if 카테고리 == "shop":
            print( "---->최저가:",re.sub('<.+?>', '', i['lprice'], 0, re.I | re.S) )
            print("---->제조사:", i['maker'])
            print("---->브랜드명:", i['brand'])
            print("---------------------------------------")
        if 카테고리 == "movie":
            print( "---->제목:",re.sub('<.+?>', '', i['title'], 0, re.I | re.S) )
            print("---->감독:", i['director'])
            print( "---->배우:",i['actor'])
            print( "---->관객평점:",i['userRating'])
            print("---------------------------------------")
        if 카테고리 == "book":
            print( "---->제목:",re.sub('<.+?>', '', i['title'], 0, re.I | re.S) )
            print("---->저자:", i['author'])
            print( "---->출판사:",i['publisher'])
            print( "--------------------------------------")

# 선택 제어
while True:
    print("검색[naverAPI] 프로그램")
    print("카테고리[1.쇼핑 2.도서 3.영화] 0.종료")
    선택 = int(input("선택:"))
    if 선택 == 1:
        카테고리 = "shop"
        검색결과수 = input("-> 쇼핑 선택 됐습니다. 몇개출력할까요?")
        네이버검색(카테고리, 검색결과수)
    if 선택 == 2:
        카테고리 = "book"
        검색결과수 = input("-> 도서 선택 됐습니다. 몇개출력할까요?")
        네이버검색(카테고리, 검색결과수)
    if 선택 == 3:
        카테고리 = "movie"
        검색결과수 = input("-> 영화 선택 됐습니다. 몇개출력할까요?")
        네이버검색(카테고리, 검색결과수)
    if 선택 == 0:
        print("-> 이용해주셔서 감사합니다")
        break


#영화명 검색해서 제목,감독,배우,평점 출력

#책 검색해서 제먹,저자명,출판사 출력

#쇼핑 검색해서 상품명,제조사명,브랜드명 출력하기
