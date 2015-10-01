# coding: UTF-8
import datetime
import os

__author__ = 'nonakanaoki'

file_path = os.path.abspath(os.path.dirname(__file__))  # このスクリプトがおいてあるディレクトリ


def get_time():  # 時間を返す
    d = datetime.datetime.today()
    # time = [d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond]
    time = str(d.year) + "-" + str(d.month) + "-" + str(d.day) \
           + "-" + str(d.hour) + "-" + str(d.minute) + "-" + str(d.second) + "-" + str(d.microsecond)
    return time


if __name__ == '__main__':
    time = get_time()[:-7]
    file_name = '../Log/' + time + '.csv'
    for i in range(10):
        f = open(file_name, 'a')  # ファイルのパス指定できる
        f.write(str(i))
        f.close()
        print(i)
