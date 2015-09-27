# coding: UTF-8
__author__ = 'nonakanaoki'
import serial
import os
import sys

module_path = os.path.abspath(os.path.dirname(__file__)) + "/.." #モジュールを読み込むためのを指定
sys.path.append(module_path)

from Dialog.serial_open_dialog import Dialog

dialog = Dialog

if __name__ == "__main__":
    dialog.set_usb_port()
    dialog.set_baud_rate()

    ser = serial.Serial(dialog.Variables.PORT, dialog.Variables.BAUD_RATE)  # ポート名とボーレートを指定してシリアルポートをオープン
    print('Open Serial Port :%s %d' % (dialog.Variables.PORT, dialog.Variables.BAUD_RATE))
    ser.close()
    print('Close Serial Port')
