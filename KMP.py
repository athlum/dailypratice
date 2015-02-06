#-*- coding:utf-8 -*-
'''
KMP算法

http://billhoo.blog.51cto.com/2337751/411486/
'''

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