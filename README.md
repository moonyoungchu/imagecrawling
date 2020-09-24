# 간단한 이미지 크롤러 만들기 with python
### imagecrawling

## import...
* selenium
* Chrome webdriver
* BeautifulSoup
* urllib

## version1
- 검색한 값의 이미지 다운 받기
~~~
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from urllib.request import urlopen
from urllib.parse import quote_plus
import urllib.request

firsturl = 'https://www.ohora.kr/product/search.html?banner_action=&keyword=' #검색할 url
searchurl = input('검색어 입력 : ')

url = firsturl + quote_plus(searchurl) #한글검색어를 변환해줌

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url) # 드라이버를 띄운다. (크롬 웹 페이지를 연다.)

time.sleep(3) #3초대기

soup = BeautifulSoup(urlopen(url),"html.parser") #url의 html 가져와서 파싱하고
img = soup.find_all(class_= 'hover_img') #클래스로 소스 추출

n=1
for i in img:    
    imgurl = (i.get('src')) #이미지경로만 get
    baseurl = 'https:' #이미지경로 앞에 붙여주기
    totalurl = baseurl+imgurl #이미지 다운로드 경로 만들기
    
    filename = str(n) + '.png' #파일이름 1,2,3,4...
    urllib.request.urlretrieve(totalurl, "./img/" + filename) #img폴더에 이미지 다운로드
    print(totalurl + filename+ ' 다운로드완료') # check용도
    n+=1 #파일명 1,2,3,4 용도

driver.close() # 드라이버 닫기
~~~


## version2
- url을 정확히 알고 있을 경우 빠르게 이미지 다운 받고 싶을 때
~~~
from bs4 import BeautifulSoup
import time
from urllib.request import urlopen
import urllib.request

url = 'https://www.ohora.kr/product/search.html?keyword=%EB%84%A4%EC%9D%BC' #정확한 url을 알고 있을 경우

soup = BeautifulSoup(urlopen(url),"html.parser") #url의 html 가져와서 파싱하고
img = soup.find_all(class_= 'hover_img') #클래스로 소스 추출

n=1
for i in img: 
    # if n < 11 : #출력 개수 조절하고 싶다면 : 10개    
        imgurl = (i.get('src')) #이미지경로만 get
        baseurl = 'https:' #이미지경로 앞에 붙여주기
        totalurl = baseurl+imgurl #이미지 다운로드 경로 만들기
        
        filename = str(n) + '.png' #파일이름 1,2,3,4...
        urllib.request.urlretrieve(totalurl, "./img/" + filename) #img폴더에 이미지 다운로드
        print(totalurl + filename+ ' 다운로드완료') # check용도
        n+=1

    # else :
    #     break

driver.close() # 드라이버 닫기
~~~
