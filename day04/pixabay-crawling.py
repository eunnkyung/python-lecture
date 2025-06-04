from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import urllib.request


def unsplash_image_crawling(search = "nature", total = 30) :
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    url = f"https://pixabay.com/ko/images/search/{search}"
    driver.get(url)
    time.sleep(3)

    folder = f"pixabay_images_{search}"
    os.makedirs(folder, exist_ok =True)

    images = driver.find_elements(By.CSS_SELECTOR,"img[srcset]")
    count = 0
    for img in images :
        if (count > total) :
            break
        img_url = img.get_attribute("srcset")
        # print(img_url)
        if img_url in img_url :
            original_photos = img_url.split(",")[-1].strip().split(" ")[0]
            print(original_photos[0])
            filename = os.path.join(folder, f"pixabay_{count}.jpg")
            urllib.request.urlretrieve(original_photos,filename)
        count +=1
    driver.quit()
unsplash_image_crawling("dolphin")



