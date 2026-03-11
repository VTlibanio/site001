import qrcode

url = "http://SEU_IP_AQUI:8000"
img = qrcode.make(url)
img.save("qrcode.png")