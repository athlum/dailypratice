#-*- coding:utf-8 -*-
'''
KMP算法

http://billhoo.blog.51cto.com/2337751/411486/
'''

from utils import print_cost

@print_cost
def get_NextList(text):
	next = []
	point = 1
	while point <= len(text):
		temptext = text[:point]
		temp_length = len(temptext)
		if temp_length == 1 :
			next.append(0)
		else:
			front = temp_length -1
			back = 0 - temp_length + 1

			picked = False

			while front > 0 :
				if temptext[:front] == temptext[back:] and not picked:
					picked = True
					sub_length = len(temptext[:front])
					for j in range(sub_length):
						score = j + 1
						location = j + 1 - sub_length
						if location < 0:
							next[location] = score
						elif location == 0:
							next.append(score)


				front -= 1
				back += 1

			if not picked:
				next.append(0)

		point += 1

	return next

@print_cost
def get_NextList_v2(text):
	next = []
	value = 0
	point = 0
	for i in range(len(text)):
		if i == 0:
			next.append(0)
		else:
			if text[i] == text[point]:
				value += 1
				point += 1
				next.append(value)
			else:
				value = 0
				point = 0
				if text[i] == text[point]:
					value += 1
					point += 1
					next.append(value)
				else:
					next.append(0)

	return next
