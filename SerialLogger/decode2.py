# coding: UTF-8
__author__ = 'nonakanaoki'

# 01 A0 12 8100ECCA FFFFFFFF 8A 0024 000A0010001B100027000960100709102A1B10611800000300001100000103F16203F162D8
# まずヘッダー部分を切り出してチェックサムの部分（おしりの1バイト）を消す
# つぎにそれを6バイトづつに切り出す
# 規則に従って復号化

# s = ':01A0128100ECCAFFFFFFFF930024000900100027100023000A00100724102A2D10611800000300001100000103F16203F162FA'
s = b':01A0128100ECCAFFFFFFFF90002400D90010001710013C000A08100012001700103C0000000300001200000103E852001B1400\r\n'


# 送られてきた生データの最初の：とチェックサムを排除したstrを返す関数
# s = ejection_data_part(s)
#  実際はバイトで来るからそこの変換の各必要がある？
def ejection_data_part(args):
    # print('---------in decode2.ejection_data_part---------')
    # print(args)
    args = args[1:-4]
    if type(args) == bytes:
        args = args.decode('utf-8')
    # print(args)
    # print('-----------------------------------------------')

    return args


# 13,14バイト目を見て正しいデータが送られてきてるかを確認
# 正しいなら[子機番号,lqi,data,data,data,...]の形でlistを返す
# 正しくない場合emptyのlistを返す
def divide_data(args):
    # 子機番号： 最初の１バイト
    # LQI    ： 12バイト目
    # データ長 ： 13,14バイト目
    li = []
    print(len(args))
    if args[26:28] == '24' and len(args) == 100:  # バイト数 これが２４なら正しいデータが来てる
        li.append(int(args[:2], 16))  # 送信元
        li.append(int(args[22:24], 16))  # LQI 16進数から１０進数に直しておく

        args = args[28:]  # ヘッダー部分を切り捨てる

        temp = []
        for i in range(12):  # 3バイトずつに分割して１０進数に変換したものをリストに入れる
            li.append(decode_data(args[:6]))
            args = args[6:]

    return li


# 受け取ったアスキー形式の文字列を元の形に戻す
def decode_data(args):
    intg = float(int(args[1:4], 16))
    dsml = float(int(args[4:6], 16)) / 100
    num = intg + dsml

    if args[0] == "1":  # 正負の判定
        num *= -1
    return num


# 無線で送られてきたデータを渡すとデコードし終えたリストが帰ってくる
def total_decode(args):
    return divide_data(ejection_data_part(args))


# if __name__ == "__main__":
#     # data = s
#     # data = ejection_data_part(s)
#     # data_list = divide_data(data)
#     print(total_decode(s))