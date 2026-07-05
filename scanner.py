import qrcode
data="https://github.com/vighneshgaikwad59-web"
img=qrcode.make(data)
img.save("QR_code.png")
print("completed")