
# 금 가격
from bs4 import BeautifulSoup as bs
import urllib.request as ur
import urllib
url = 'https://search.naver.com/search.naver?query=%EA%B8%88+1%EB%8F%88+%EA%B0%80%EA%B2%A9'
웹문서 = ur.urlopen(url)

soup = bs(웹문서.read(),'html.parser')
가격 = soup.find_all('em',{"class":"down _now_value"})
print(가격[0].text)