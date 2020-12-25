from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import sys
import time
from textblob import TextBlob
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

url = 'https://www.instagram.com/xiaomiindia/'
driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source)

containers = soup.findAll("div",{"class":"Nnq7C weEfm"})
print(len(containers))
link = 'https://www.instagram.com'+containers[0].div.a["href"]
print(link)
driver.get(link)

for i in range(4):
    try:
        more = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/div[1]/ul/li/div/button')
        more.click()
        time.sleep(3)
    
    except:
        print("No further comments")
        break
    
    

f=open("demofile.txt","a",encoding="utf-8")
i=0

new_soup = BeautifulSoup(driver.page_source)
holders = new_soup.findAll("div",{"class":"C4VMK"})
for holder in holders:
    i=i+1
    print(i)
    print(holder.span.text.translate(non_bmp_map))
    try:
        f.write(str(holder.span.text.translate(non_bmp_map))+"\n")
    except:
        print("Some error")

f.close()
f=open("demofile.txt","r",encoding="utf-8")
comments = f.readlines()
for comment in comments:
    print("-------------------")
    print(comment)
    analysis = TextBlob(comment)
    print(analysis.sentiment)
    


        




