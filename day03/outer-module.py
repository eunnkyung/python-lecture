import qrcode
import qrcode.constants

qr_data = "www.naver.com"
#qr_img = qrcode.make(qr_data)
#save_path =  "test.png"
#qr_img.save(save_path)
#print("success")
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data(qr_data)
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="white")
img.save("qr_code.png")
