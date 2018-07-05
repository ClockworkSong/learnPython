#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import math

list = [[1, 2, 0],[2, 4, 0],[7, 8, 0], [8, 9, 0], [9, 12, 0], [10, 15, 0], [12, 15, 0], [15, 17, 0], [18, 20, 0]]

print "len(list):", len(list)
print "list[0][0]:", list[0][0]
print "list[1][0]:", list[1][0]
print "list[-1]:", list[-1]

new_list = []
for i in range(len(list)):
	# print "list[][]=", list[i][i]
	if i == 8:
		i = -2
	num = np.square(list[i][0] - list[i+1][0]) + np.square(list[i][1] - list[i+1][1]) + np.square(list[i][2] - list[i+1][2])
	print "num = ", num
	num2 = np.sqrt(num)
	print "num2 = ", num2
	if num2 > 2:
		new_list.append(list[i])

print "list:", list
print "new_list:", new_list
