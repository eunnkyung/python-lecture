import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 검색어와 URL
query = '파이썬'
url = f'https://search.naver.com/search.naver?where=news&query={query}'

# HTTP 요청
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 각 뉴스 카드 기준으로 추출
cards = soup.select('div.UC1lc0LnKWszTX7CYO7K')

# 엑셀 워크북 생성
wb = Workbook()
ws = wb.active
ws.title = '뉴스 검색 결과'
ws.append(['번호', '제목', '링크', '이미지 URL', '출처'])  # 헤더

print(f"'{query}' 관련 뉴스 기사:")

for i, card in enumerate(cards, 1):
    # 제목
    title_tag = card.select_one('span.sds-comps-text-type-headline1')
    title = title_tag.text.strip() if title_tag else '제목 없음'

    # 링크
    link_tag = card.select_one('a._AuHeQ05X7PwSlhb6H2B')
    link = link_tag['href'] if link_tag else '링크 없음'

    # 이미지
    img_tag = card.select_one('img')
    img_url = img_tag['src'] if img_tag else '이미지 없음'

    # 출처
    press_tag = card.select_one('span.sds-comps-profile-info-title-text')
    press = press_tag.text.strip() if press_tag else '출처 없음'

    print(f"\n{i}. [{press}] {title}")
    print(f"   📎 링크: {link}")
    print(f"   🖼️ 이미지: {img_url}")

    # 엑셀에 한 줄씩 추가
    ws.append([i, title, link, img_url, press])

# 엑셀 파일 저장
file_name = f"{query}_뉴스_검색결과.xlsx"
wb.save(file_name)
print(f"\n✅ 엑셀 저장 완료: {file_name}")
