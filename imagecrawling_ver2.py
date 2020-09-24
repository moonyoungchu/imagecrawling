from bs4 import BeautifulSoup
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


