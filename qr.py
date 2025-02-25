import qrcode
url = "https://username.github.io/vcard-site/"
qr = qrcode.make(url)
qr.save("qrcode.png")
