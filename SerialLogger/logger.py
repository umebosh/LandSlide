# coding: UTF-8
__author__ = 'nonakanaoki'
import serial
import os


def set_usb_port():
    files = os.listdir("/dev")  # "/dev"にあるファイルを列挙して保存
    usbport = []  # USBシリアル関係のポート名を保存しておくlist
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


def set_baud_rate():
    baud_rate = [4800, 9600, 115200]
    print('Set baud rate')
    for i in range(len(baud_rate)):
        message = "[" + str(i) + "]" + str(baud_rate[i])
        print(message)
    while True:
        try:
            port = input()
            print(str(baud_rate[int(port)]))
            break
        except:
            print('incorrect number')


if __name__ == "__main__":
    set_usb_port()
    set_baud_rate()
