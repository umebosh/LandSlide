# coding: UTF-8
__author__ = 'nonakanaoki'
import serial
import os
import sys
import datetime

module_path = os.path.abspath(os.path.dirname(__file__)) + "/.."  # モジュールを読み込むためのを指定
sys.path.append(module_path)  # これでモジュールの読み込みができるようになる
from Dialog.serial_open_dialog import Dialog

dialog = Dialog


def get_time():  # 時間が入ったlistを返す
    d = datetime.datetime.today()
    time = [d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond]
    return time


if __name__ == "__main__":
    dialog.set_usb_port()
    dialog.set_baud_rate()

    ser = serial.Serial(dialog.Variables.PORT, dialog.Variables.BAUD_RATE)  # ポート名とボーレートを指定してシリアルポートをオープン
    print('Open Serial Port :%s %d' % (dialog.Variables.PORT, dialog.Variables.BAUD_RATE))
    ser.close()
    print('Close Serial Port')
