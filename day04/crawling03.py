#pip install selenium
#pip install requests
#pip install beautifulsoup4

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
query=input("검색어를 입력하세요. : ")
url = f"https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={query}"


options = Options()
options.add_argument("--headless")  #브라우져 띄우지 마라...
options.add_argument("--no-sandbox")  #크롬의 sansbox 보안 기능 비활성화

driver = webdriver.Chrome(options=options)
driver.get(url)
wait = WebDriverWait(driver,10)

news_count = 0
news_total = 30
while news_count < news_total :
    driver.find_element(By.TAG_NAME,"body").send_keys(Keys.END)
    time.sleep(2) #로딩될떄 걸리는 시간...
    soup = BeautifulSoup(driver.page_source,"html.parser")
    items = soup.select("div.UC1lc0LnKWszTX7CYO7K") 
    news_count = len(items)
    if news_count > news_total :
        break

workbook =  Workbook()
workbookActive = workbook.active
workbookActive.title = "네이버 뉴스 검색 결과"
workbookActive.append(["번호","제목","링크"])
for i, item in enumerate(items, 1) : 
    title_tag = item.select_one("span.sds-comps-text-type-headline1")
    title = title_tag.text.strip() if title_tag else "제목없음"
    
    img_src = "이미지 없음"
    img_div = item.select_one("div.sds-rego-thumb-overlay")
    if img_div :
        img_tag = img_div.select_one("img")
        if img_tag and img_tag.has_attr("src") :
            img_src = img_tag["src"]

    link = "링크없음"
    link_div = item.select_one("div.HyuoyN_3xv7CrtOc6W9S")
    if link_div :
        a_tags = link_div.select("a")  
        if len(a_tags) > 1 :
            link = a_tags[1]["href"]

    print(f"제목==={title}")
    print(f"이미지 경로==={img_src}")
    print(f"link==={link}")
    workbookActive.append([i,title,link])
save_file_name = f"{query}_네이버 뉴스 검색 결과.xlsx"
workbook.save(save_file_name)
driver.quit()


