import requests
#특정 URL에 접속하는 요청(Request) 객체를 생성
request = requests.get("http://dowellcomputer.com/main.jsp")

#접속한 이후의 웹 사이트 소스코드를 추출합니다
html = request.text.strip()

print(html)