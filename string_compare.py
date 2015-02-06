#-*- coding:utf-8 -*-
'''
字符串相似度

现有两个序列X={x1,x2,x3，...xi}，Y={y1,y2,y3，....，yi}，
设一个C[i,j]: 保存Xi与Yj的当前最小的LD。
1.当 Xi = Yi 时，则C[i,j]=C[i-1,j-1]；
2.当 Xi != Yi 时， 则C[i,j]=Min{C[i-1,j-1],C[i-1,j],C[i,j-1]} + 1；
'''

import utils

def compare_str(str1,str2):
	result = utils.build_blanklist(len(str1),len(str2))

	for i in range(len(str1)):
		result[i][0] = i

	for i in range(len(str2)):
		result[0][i] = i

	for i in range(len(str1)):
		for j in range(len(str2)):
			if str1[i] == str2[j]:
				if i and j:
					result[i][j] = result[i-1][j-1]
			else:
				top = None
				if j:
					top = result[i][j-1]
				left = None
				if i:
					left = result[i-1][j]
				topleft = None
				if i and j:
					topleft = result[i-1][j-1]

				result[i][j] = utils.get_min([top,left,topleft]) + 1

	print ' ',' '.join(list(str1))
	for i in range(len(result)):
		numlist = result[i]
		list_str = ' '
		for j in numlist:
			list_str += '%s ' % str(j)
		print str2[i] + list_str

	return result[len(str1)-1][len(str2)-1]


if __name__ == '__main__':
	str1 = 'abde'
	str2 = 'dbae'
	print 'str1:',str1
	print 'str2:',str2
	ld = compare_str(str1,str2)
	print 'ld:',ld