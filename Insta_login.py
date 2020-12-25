from bs4 import BeautifulSoup as  soup
from urllib.request import urlopen as uReq
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.instagram.com/xiaomiindia/')
driver.implicitly_wait(10)
searchpost = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div/div[2]')
searchpost.click()

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
login.send_keys("")


login2 = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
login2.send_keys("")

driver.implicitly_wait(10)

loginbut = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button')
loginbut.click()

time.sleep(3)
driver.get('https://www.instagram.com/xiaomiindia/')


thepost = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
thepost.click()



my_url = 'https://www.instagram.com/xiaomiindia/'
driver.get(my_url)

soup = soup(driver.page_source)

containers = soup.findAll("div",{"class":"Nnq7C weEfm"})
postext = containers[0].div.a["href"]
print("instagram.com"+postext)

new_url = "https://www.instagram.com"+postext
driver.get(new_url)

nsoup = soup(driver.page_source)
holder = soup.findAll("div",{"class":"Kj7h1  yJx9G"})
print(len(holder))




