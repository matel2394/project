#발급받은 애플리케이션 정보를 변수에 저장
import json
import re

클라이언트id="1lsGnepQrJ8pW449LsIN"
클라이언트secret = "8vtuuvBdFs"
#네이버 검색을 파이썬에서하기
#검색결과는 딕셔너리 호출된다 [딕셔너리 데이터 가공]
    #결과: {"item" : [검색결과리스트] }
    #검색 결과 리스트중 한개당 {} 묶음
#documents 파이썬 코드를 복사해오기
import os
import sys
import urllib.request
import json
client_id = 클라이언트id
client_secret = 클라이언트secret
#직접 입력해서 검색하기
검색어 = input("책 검색:")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/book.json?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/book.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    검색결과 = response_body.decode('utf-8') #한글 지원
    json결과 = json.loads(검색결과)
    #검색 결과 가공하기

    for i in json결과['items']:
        타이틀 = re.sub('<,+?>','',i['title'],0,re.I | re.S)
        print(타이틀)

else:
    print("Error Code:" + rescode)



import os
import sys
import urllib.request
client_id = 클라이언트id
client_secret = 클라이언트secret
#직접 입력해서 검색하기
검색어 = input("블로그 검색:")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

import os
import sys
import urllib.request
client_id = 클라이언트id
client_secret = 클라이언트secret
#직접 입력해서 검색하기
검색어 = input("뉴스 검색:")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/news?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)