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
        print(i)
        data += li[i]
    else:
        if i != 0:
            datalist.append(data)
        data = li[i]
        print(i)

# datalist.append(data)

# for i in range(len(datalist)):
#     li = list(datalist[i])
#     for j in range(6):
#         if j == 0:
#             if data
#             hexnum +=
print(datalist)
