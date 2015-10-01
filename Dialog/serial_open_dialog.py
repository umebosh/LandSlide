# coding: UTF-8
import os

__author__ = 'nonakanaoki'

class Dialog:
    class Variables:  # 色々と使い回す変数を格納しておく
        PORT = '/dev/'  # シリアルポートを開放するときにフルパスが必要なので'/dev/'を入れておく
        BAUD_RATE = 0

    def set_usb_port():  # ユーザの入力からデバイスのあるポートを指定する関数
        files = os.listdir("/dev")  # "/dev"にあるファイルを列挙して保存
        usbport = []  # USBシリアル関係のポート名を保存しておくlist
        print('Select your tocostick')
        i = 0
        for file in files:
            if file.find('usb') != -1 or file.find('USB') != -1:
                usbport.append(file)
                message = "[" + str(i) + "]" + file
                print(message)
                i += 1

        while True:
            try:
                num = input()
                print('>%s\n' % usbport[int(num)])
                Dialog.Variables.PORT += usbport[int(num)]
                break
            except:
                print('incorrect number')

    def set_baud_rate():  # ユーザの入力からボーレートを指定する関数
        baud_rate = [4800, 9600, 115200]
        print('Set baud rate')
        for i in range(len(baud_rate)):
            message = "[" + str(i) + "]" + str(baud_rate[i])
            print(message)
        while True:
            try:
                num = input()
                print('>%s\n' % str(baud_rate[int(num)]))
                Dialog.Variables.BAUD_RATE = baud_rate[int(num)]
                break
            except:
                print('incorrect number')
