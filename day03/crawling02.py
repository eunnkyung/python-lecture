from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.get("https://www.gmarket.co.kr/n/superdeal")

wait = WebDriverWait(driver, 10)
# 'ul' 태그에 클래스 두 개가 모두 있을 때 선택자 작성법
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.item_list.option")))

# 스크롤 내리기 (동적 로딩 처리)
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 상품 아이템들 불러오기
items = driver.find_elements(By.CSS_SELECTOR, "ul.item_list.option > li.livedeal")

print(f"총 상품 수: {len(items)}")

for item in items:
    try:
        name = item.find_element(By.CSS_SELECTOR, "p.text__itemcard-title").text
        price = item.find_element(By.CSS_SELECTOR, "strong.text__price").text
        print(name, price)
    except Exception as e:
        print("Error:", e)

driver.quit()
