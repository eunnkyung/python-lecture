from PIL import Image
import qrcode
import qrcode.constants
qr_data = "http://www.apple.com"
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H, #qrcode가 손상되더라도 자체 복구 알고리즘으로 복구
    box_size=10, #셀하나당 10px  
    border=4 #테두리 4px
)
qr.add_data(qr_data)
qr.make(fit=True)
qr_img  = qr.make_image(fill_color="#000000",back_color="#ffffff").convert("RGBA")

logo = Image.open("day03/apple.png").convert("RGBA")
qr_width, qr_height = qr_img.size  #로고를 가운데 넣어두기 위해 필요 js에 있는 구조분해 할당이랑 비슷
print(qr_img.size)  #튜플 언팩킹 불변객체
# logo_size = qr_width / 4 
# print(logo_size)
logo_size = qr_width // 4  #  //는 정수 나눗셈 즉 qr코드 크기의 1/4 사이즈로 로고를 만들어 달라.
print(logo_size)  
logo = logo.resize((logo_size,logo_size))  #resize의 매개변수 타입이 tuple임
pos =  ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
qr_img.paste(logo,pos)
qr_img.save("qr_apple.png")
print("저장완료")

