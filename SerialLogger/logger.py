# coding: UTF-8
__author__ = 'nonakanaoki'
import serial
import os
import sys
import datetime

module_path = os.path.abspath(os.path.dirname(__file__)) + "/.."  # モジュールを読み込むためのを指定
sys.path.append(module_path)  # これでモジュールの読み込みができるようになる
from Dialog.serial_open_dialog import Dialog
from SerialLogger.decode2 import *

dialog = Dialog


def get_time():  # 時間を返す
    d = datetime.datetime.today()
    # time = [d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond]
    time = str(d.year) + "-" + str(d.month) + "-" + str(d.day) \
           + "-" + str(d.hour) + "-" + str(d.minute) + "-" + str(d.second) + "-" + str(d.microsecond)
    return time


if __name__ == "__main__":
    # print(get_time())
    file_date = get_time()[:-7]  # ログファイルの保存名 get_time関数の返り値からミリ秒をとったものを採用することにする
    dialog.set_usb_port()
    dialog.set_baud_rate()

    ser = serial.Serial(dialog.Variables.PORT, dialog.Variables.BAUD_RATE)  # ポート名とボーレートを指定してシリアルポートをオープン
    print('Open Serial Port :%s %d' % (dialog.Variables.PORT, dialog.Variables.BAUD_RATE))
    try:
        while True:
            now_time = get_time()
            line = ser.readline()

            raw_data = [now_time, line]  # センサーから送られてきたままのアスキーコマンドデータに受け取った時刻を追加したもの
            raw_data_str = ','.join(map(str, raw_data))
            raw_data_path = '../Log/Raw/' + file_date + '-raw.csv'
            raw_file = open(raw_data_path, 'a')
            raw_file.write(raw_data_str)
            raw_file.close()

            decoded_data = total_decode(line)  # センサーから受け取ったデータをエンコードして頭に受け取った時刻をつけてる
            decoded_data.insert(0, now_time)
            decoded_data_str = ','.join(map(str, decoded_data))
            decoded_data_path = '../Log/' + file_date + '.csv'
            decoded_file = open(decoded_data_path, 'a')
            decoded_file.write(decoded_data_str)
            decoded_file.close()

            print('---------------------------')
            print(line)
            print(total_decode(line))


    except:
        ser.close()
        print('Close Serial Port')
