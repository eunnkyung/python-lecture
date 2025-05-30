import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
query="대통령선거"
url = f"https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={query}"

headers = {"User-Agent":"Mozilla/5.0"}
response = requests.get(url,headers=headers)    
soup = BeautifulSoup(response.text,"html.parser")
#print(soup.prettify())
items = soup.select("div.UC1lc0LnKWszTX7CYO7K") 

workbook =  Workbook()
workbookActive = workbook.active
workbookActive.title = "네이버 뉴스 검색 결과"
workbookActive.append(["번호","제목","링크"])
for i, item in enumerate(items, 1) : 
    title_tag = item.select_one("span.sds-comps-text-type-headline1")
    title = title_tag.text.strip() if title_tag else "제목없음"
    img_div = item.select_one("div.sds-rego-thumb-overlay")
    img_tag = img_div.select_one("img")
    img_src = img_tag["src"]
    link_div = item.select_one("div.HyuoyN_3xv7CrtOc6W9S")
    a_tags = link_div.select("a")  
    link = a_tags[1]["href"]

    print(f"제목==={title}")
    print(f"이미지 경로==={img_src}")
    print(f"link==={link}")
    workbookActive.append([i,title,link])
save_file_name = f"{query}_네이버 뉴스 검색 결과.xlsx"
workbook.save(save_file_name)


