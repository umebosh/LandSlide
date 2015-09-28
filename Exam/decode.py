# coding: UTF-8
__author__ = 'nonakanaoki'
# :00A012FF00020010004210002F00095410044800014810535700000300001100000203F34903F349X
s = '00000010003E00000F000A00000B5A101136106E3D00000300001300000303F32803F328X'
li = list(s)
data = ''
datalist = []
hexnum = ""
print(len(li))
for i in range(len(li)):
    if (i)%6 != 0:
        data += li[i]
    else:
        if i != 0:
            datalist.append(data)
        data = li[i]

# datalist.append(data) ##データが3バイト未満の最後のところ
print(datalist)

numlist = []
for i in range(len(datalist)):
    n = datalist[i]
    tmp = [int(n[0], 16), int(n[1:4], 16), int(n[4:6], 16)]

    result = float(tmp[1] + tmp[2] * 0.01)

    if tmp[0] == 1:
        result *= -1

    numlist.append(result)

print(numlist)

