from PIL import Image
import qrcode
import qrcode.constants
import os

os.makedirs("qr-code",exist_ok=True)


data_list = [
    "http://www.apple.com",
    "http://www.peach.com",
    "http://www.melon.com",
    "http://www.plum.com",
]

logo_list = [
    "day03/logo/apple.png",
    "day03/logo/peach.png",
    "day03/logo/water-melon.png",
    "day03/logo/plum.png",
    
]

for i, (data,logo_path) in enumerate(zip(data_list,logo_list), start=1) : 
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H, #qrcode가 손상되더라도 자체 복구 알고리즘으로 복구
        box_size=10, #셀하나당 10px  
        border=4 #테두리 4px
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img  = qr.make_image(fill_color="#000000",back_color="#ffffff").convert("RGBA")

    logo = Image.open(logo_path).convert("RGBA")
    qr_width, qr_height = qr_img.size  #로고를 가운데 넣어두기 위해 필요 js에 있는 구조분해 할당이랑 비슷
    print(qr_img.size)  #튜플 언팩킹 불변객체
    # logo_size = qr_width / 4 
    # print(logo_size)
    logo_size = qr_width // 4  #  //는 정수 나눗셈 즉 qr코드 크기의 1/4 사이즈로 로고를 만들어 달라.
    print(logo_size)  
    logo = logo.resize((logo_size,logo_size))  #resize의 매개변수 타입이 tuple임
    pos =  ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    qr_img.paste(logo,pos)
    save_path = f"qr-code/qr_logo_{i}.png"
    qr_img.save(save_path)
    print("저장완료")

