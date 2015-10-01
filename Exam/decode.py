# coding: UTF-8
__author__ = 'nonakanaoki'
# :00A012FF00020010004210002F00095410044800014810535700000300001100000203F34903F349X
# s = '00000010020F000358000862001851101509103B1210041410042F10030403F353001C3C'
s = "000900100027100023000A00100724102A2D10611800000300001100000103F16203F162"
li = list(s)
data = ''
datalist = []
print(len(li))
for i in range(len(li)):
    if (i) % 6 != 0:
        data += li[i]
    else:
        if i != 0:
            datalist.append(data)
        data = li[i]

datalist.append(data) ##データが3バイト未満の最後のところ
print(datalist)

def div_data(data):
    li = list(data)
    divide_data = ''
    datalist = []
    print(len(li))
    for i in range(len(li)):
        if (i) % 6 != 0:
            divide_data += li[i]
        else:
            if i != 0:
                datalist.append(divide_data)
            divide_data = li[i]

datalist.append(data) ##データが3バイト未満の最後のところ
print(datalist)


def decode(list):
    numlist = []
    for i in range(len(list)):
        n = list[i]
        tmp = [int(n[0], 16), int(n[1:4], 16), int(n[4:6], 16)]

        result = float(tmp[1] + tmp[2] * 0.01)

        if tmp[0] == 1:
            result *= -1

        numlist.append(result)
    return numlist


print(decode(datalist))
