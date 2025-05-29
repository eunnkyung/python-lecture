from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
# options.add_argument("--headless")  # 필요 시 주석 해제

driver = webdriver.Chrome(options=options)
driver.get("https://www.gmarket.co.kr/n/superdeal")

wait = WebDriverWait(driver, 10)
# 리스트 전체를 감싸는 ul 또는 div의 클래스명을 확인 (임시로 ul.livedeal-list 등으로 변경 가능)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.item_list")))

items = driver.find_elements(By.CSS_SELECTOR, "li.livedeal")

for item in items:
    try:
        name = item.find_element(By.CSS_SELECTOR, "p.text__itemcard-title").text
        price = item.find_element(By.CSS_SELECTOR, "strong.text__price").text
        print(name, price)
    except Exception as e:
        print("Error:", e)

driver.quit()
