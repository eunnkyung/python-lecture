from PIL import Image
import qrcode
import os

# QR 코드 생성
qr_data = "https://www.naver.com"
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # H는 최대 30% 복구
    box_size=10,
    border=4,
)
qr.add_data(qr_data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# 로고 이미지 열기
logo = Image.open("day03/music.png")  # 같은 폴더 내 logo.png 있어야 함

# 로고 사이즈 조절
qr_width, qr_height = qr_img.size
logo_size = qr_width // 4
logo = logo.resize((logo_size, logo_size))

# 로고 삽입 위치 계산 (가운데 정렬)
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# QR 코드에 로고 붙이기
qr_img.paste(logo, pos)

# 저장 폴더 확인
os.makedirs("qr", exist_ok=True)
qr_img.save("qr/qr_with_logo.png")
print("로고 삽입된 QR코드 저장 완료")
