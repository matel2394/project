#정보수집 크롤링 패키지
    #1. Ex1.py

#크롤링 : 인터넷에서 데이터 추출하기
    #인터넷문자 ==> 웹문자 ==> html(하이퍼텍스트 마크업 언어)
#1.Beautifulsoup , bs 설치

from bs4 import BeautifulSoup as bs
import urllib.request as ur

#1.인터넷 주소 넣기

url = 'https://quotes.toscrape.com/'

#2. 해당(url) 인터넷을 파이썬에서 열기해서 html 변수에 저장
html = ur.urlopen(url)

#3. read() : 인터넷을 열어보기
soup = bs(html.read(),'html.parser')

# for i in soup.find_all('span'):
#     print(i.text)
#div 태그에 포함된 해당 클래스만 찾기
for i in soup.find_all('div',{"class":"quote"}):
    print(i.text)