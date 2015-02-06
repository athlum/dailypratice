#-*- coding:utf-8 -*-

def build_blanklist(length1,length2):
	result = []
	for i in range(length1):
		result.append([])
		for j in range(length2):
			result[i].append(0)

	return result

def get_min(numlist):
	minnum = None
	for i in numlist:
		if i == None:
			continue

		if minnum == None:
			minnum = i
		elif i < minnum:
			minnum = i

	if minnum == None:
		minnum = 0

	return minnum