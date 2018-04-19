# -*- coding: utf-8 -*-
def findMin1(lst):
	num=len(lst)
	a=lst[0]
	for i in range(0,num):
		if lst[i]<a:
			a=lst[i]
	return a

# lst=[8,2,3,4,5]
# print(findMin1(lst))


def findMin2(lst):
	num=len(lst)
	for i in range(0,num):
		for j in range(0,num):
			if lst[i]<lst[j]:
				return lst[i]

# lst=[2,3,4,5,1]
# print(findMin2(lst))


计时实验，验证List按照索引值为O（1）
import time
lst=[i for i in range(1000000)]
def test1(lst):
	start=time.time()
	n=lst[100]
	end=time.time()
	return end-start

print(test1(lst))

import time
def test2():
	d={'a':80,'b':88,'c':66,'d':95}
	L=[1,2,3,4,5,6,7,8,9,0]

	start1=time.time()
	# score=d.get('b')
	# d['e']=89
	del d['a']
	end1=time.time()
	t1=end1-start1

	start2=time.time()
	del L[2]
	end2=time.time()
	t2=end2-start2

	# score=t2/t1

	return t1,t2

print(test2())

