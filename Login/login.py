from selenium import webdriver

driver = webdriver.Chrome('Location of chromedriver.exe')
delay_time = 3

driver.implicitly_wait(delay_time)

driver.get('https://nid.naver.com/nidlogin.login')

id = "Naver ID"
pw = "Naver PW"

driver.execute_script("document.getElementById('id').value=\'" + id + "\'")
driver.execute_script("document.getElementById('pw').value=\'" + pw + "\'")
driver.find_element_by_xpath('//*[@id="log.login"]').click()
