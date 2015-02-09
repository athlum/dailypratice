#-*- coding:utf-8 -*-
'''
KMP算法

http://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm
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
	next = [0]
	point = 1
	n_point = 0

	while point < len(text):
		if text[point] == text[n_point]:
			n_point += 1
			point += 1
			next.append(n_point)
		else:
			if n_point == 0:
				point += 1
				next.append(0)
			n_point = 0

	return next

@print_cost
def Match(text,search_string):
	point = 0
	key_point = 0

	string_length = len(search_string)
	next = get_NextList_v2(search_string)

	while point < len(text):
		if text[point] == search_string[key_point]:
			if key_point == string_length - 1:
				location = point - string_length + 1
				print "Found '%s' in location: %s" % (search_string,location + 1)
				return location

			key_point += 1
			point += 1

		else:
			if key_point == 0:
				point += 1
			key_point = next[key_point]

	print "Didn't find '%s' in text." % (search_string)
	return -1