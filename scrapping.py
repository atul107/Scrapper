import re
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
import urllib
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait

a = int(input())
b = int(input())
data = []

driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver.exe") 
sign_in_url = 'https://www.teacheron.com/login.html'
driver.get(sign_in_url) 
driver.wait = WebDriverWait(driver, 10)

button = driver.find_element_by_id("show-reg-form-common") 
button.click() 
time.sleep(1)

emailBox = driver.find_element_by_id("loginmodel_loginIdOrEmail_common")
emailBox.send_keys('***********@gmail.com')
time.sleep(1)

passwordBox = driver.find_element_by_id("loginmodel_password_common")
passwordBox.send_keys('************')
time.sleep(1)

submit = driver.find_element_by_css_selector("input[type='submit']")
submit.click()
time.sleep(1)

for page_count in range(a, b):
	URL = 'https://www.teacheron.com/tutor-jobs?p=' + str(page_count)
	# URL = 'https://www.teacheron.com/assignment-tutor-jobs?p=' + str(page_count)
	print(page_count)
	driver.get(URL)
	time.sleep(2)
	HTML = driver.page_source
	soup = BeautifulSoup(HTML, 'html.parser')
	results = soup.find_all('div', class_='inner-results overflow-hidden- padding-left-20 padding-right-20 padding-top-16 padding-bottom-0')

	for item in results:
		temp = item.find('ul', class_='list-inline down-ul no-padding-left-li margin-bottom-10-li').find_all("li")[1].find_all("span")[1]
		try: 
			if(temp.text=='Free'):
				print(temp.text)
				link = item.find('a')
				print(link['href'])
				detail_url = str(link['href'])
				driver.get(detail_url)
				time.sleep(2)
				# alpha = int(input())
				if  1 == 1:
					message_box_button = driver.find_element_by_id("btnApplyPostViaVerifiedEmail")
					message_box_button.click() 
					time.sleep(1)

					message_box = driver.find_element_by_id("message")
					message_box.send_keys('Hello, I can help you with your assignment. Do let me know if you are still looking for help.')
					time.sleep(1)

					send_btn = driver.find_element_by_id("messagePostBtn")
					send_btn.click() 
					time.sleep(1)
		except: 
			pass



				


