# coding: UTF-8
import os

# ログデータをセンサー毎に分割するスクリプト
# 何故かExam/にログが吐かれるバグが有る

__author__ = 'nonakanaoki'

path = '/Users/nonakanaoki/Desktop/CPS/LandSlide/2015-10-2-11-0-54.csv'
f = open(path)
data = f.readlines()
f.close()

file_name = os.path.basename(path)[:-4]  # 拡張子なしのファイル名
print(file_name)

logger1 = []
logger2 = []
error_data = []


def print_data(data):
    for l in data:
        print(l)


if __name__ == '__main__':
    # print(type(data))
    print(len(data))
    i = 0
    for line in data:
        if i % 1000 == 0:
            print(100 * i / len(data))
        i += 1

        first = line.find(',')
        logger_no = line[first + 1:first + 2]  # 子機番号の切り出し

        if logger_no == '1':
            logger1.append(line)
            f_logger1 = open(file_name + '-logger1.csv', 'a')
            f_logger1.writelines(line)
            f_logger1.close()

        elif logger_no == '2' and first > 15:  # first>15は’2015-10-2-7-25-5’の部分 これよりも長いなら正しい位置から子機番号を取ってきてる
            # センサーからデータが読み出せてなかった場合にはpython側で追加した日付だけのデータになるのでこの記述を追加
            logger2.append(line)
            f_logger2 = open(file_name + '-logger2.csv', 'a')
            f_logger2.writelines(line)
            f_logger2.close()
        else:
            error_data.append(line)

            # print('-------logger1--------')
            # print_data(logger1)
            # print('-------logger2--------')
            # print_data(logger2)
            print('-------error_data--------')
            print_data(error_data)
