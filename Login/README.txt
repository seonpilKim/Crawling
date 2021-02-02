[네이버 자동 로그인 프로그램]

- Requirements
 1. Chrome driver install : https://chromedriver.chromium.org/downloads
 2. Module install : cmd -> "pip install selenium"

"Selenium" : 웹사이트 테스트를 위한 도구로 브라우저 동작을 자동화 할 수 있음
 셀레니움을 이용하는 Web Crawling 방식은 바로 이 점을 적극적으로 활용함
 프로그래밍으로 브라우저 동작을 제어해서 마치 사람이 이용하는 것 같이 웹페이지를 요청하고 응답을 받을 수 있음

먼저, chromedriver.exe'를 적절한 경로에 저장한 뒤, 환경변수에 저장한다.
 driver = webdriver.Chrome('C:\chromedriver.exe')

Crawling할 주소('https://nid.naver.com/nidlogin.login')를 넣어 사이트를 호출한다.
 driver.get('https://nid.naver.com/nidlogin.login')

Resources를 기다리기위해 3초간 delay를 추가한다.
 delay_time = 3
 driver.implicitly_wait(delay_time)

다음으로, 해당 주소에 직접 들어가서 F12를 눌러 개발자모드로 들어가 html태그 내부에서 로그인 form의, input 태그를 찾는다.
해당 태그의 id값을 가져와 아래와 같이 value를 설정하고, 다음과 같이 script를 실행시킨다.
 id = "네이버 ID"
 pw = "네이버 PW"
 driver.execute_script("document.getElementById('id').value=\'" + id + "\'")
 driver.execute_script("document.getElementById('pw').value=\'" + pw + "\'")
(네이버의 경우에 id와 pw를 받는 input태그의 id가 각각 'id', 'pw'이다. 그림 <html> 참고)

마지막으로 XPATH를 이용하여 로그인버튼을 Crawling하고, 해당 버튼을 click한다.
 driver.find_element_by_xpath('//*[@id="log.login"]').click()
 p.s) xpath는 해당 html태그를 마우스 우측클릭해서 copy할 수 있다.

XPATH 문법 (https://wkdtjsgur100.github.io/selenium-xpath/)
 1. nodename : Node명이 "nodename"인 Node 선택
 2. / : 루트Node로 부터 선택
 3. // : 현재 Node로부터 문서상의 모든 Node를 조회
 4. . : 현재 Node 선택
 5. .. : 현재 Node의 부모Node 선택
 6. @ : 현재 Node의 속성 선택

