import qrcode

qr=qrcode.make('www.linkedin.com/in/manasvi-prakash-278abb1b7')
qr.save('Linkden.png')

image=qrcode.make('https://github.com/')
image.save('github.png')

w=qrcode.make('Hii, I am Manasvi Prakash!')
w.save('Intro.png')

import cv2

d= cv2.QRCodeDetector()
val,points,straight_qrcode= d.detectAndDecode(cv2.imread('Intro.png'))
print(val)