# coding: UTF-8
__author__ = 'nonakanaoki'

import numpy as np
from matplotlib import pyplot as plt

# t = np.zeros(100)
# y = np.zeros(100)
#
# plt.ion()
# plt.figure()
# li, = plt.plot(t, y)
# plt.ylim(0, 5)
# plt.xlabel("time[s]")
# plt.ylabel("Voltage[V]")
#
# t = np.append(t, (float(data[0])-tInt)/10**6)
#         t = np.delete(t, 0)
#         y = np.append(y, float(data[1])*5/1023)
#         y = np.delete(y, 0)
#
#         li.set_xdata(t)
#         li.set_ydata(y)
#         plt.xlim(min(t), max(t))
#         plt.draw()