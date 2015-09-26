# coding: UTF-8
__author__ = 'nonakanaoki'
import os

files = os.listdir("/dev")                  #"/dev"にあるファイルを列挙して保存
usbport = []                                #USBシリアル関係のポート名を保存しておくlist
print('Select your tocostick')
i = 0
for file in files:
    if file.find('usb') != -1:
        usbport.append(file)
        message = "[" + str(i) + "]" + file
        print(message)
        i += 1

while True:
    try:
        port = input()
        print(usbport[int(port)])
        break
    except:
        print('incorrect number')
