# -*- coding: utf-8 -*-
#1 集合运算
def reverse(s,n):
	result=''
	result=s[n:]+s[0:n]
	return result

print('1-reverse',reverse('abcd',1))
print('2-reverse',reverse('mnbol',2))

#2 计算阶乘和
def factorailSum(n):
	s=0	
	num=n
	for i in range(1,num+1):
		s1=1
		for j in range(1,i+1):
			s1=s1*j
		s=s+s1
	return s
print(factorailSum(6))


# 3 数字转换
def transNum(s):
	n=0
	b=1

	dictt={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
	n=s.split('-')
	for i in range(0,len(n)):
		n[i]=dictt[n[i]]
	b=n[0]
	for i in range(0,len(n)-1):
		b=b*10+n[i+1]
	n=b
	return n
print(transNum('eight-nine-one-two-three-four'))

#4 创建字典
def createDict(keys,values):
	d=dict()
	d=dict(zip(keys,values))
	return d

print(createDict((1,2,3),('abc','def','ghi')))


#5 创建集合
def createSet(s1,s2):
	union=set()
	aset=set(s1)
	bset=set(s2)
	union=aset|bset
	return union
print(createSet('abc','bcd'))


#6 月份天数
def countDays(y,m):
	day=0
	if m==2:
		if y%400==0 or (y%4==0 and y%100!=0):
			day=29
		else:
			day=28
	elif m in [1,3,5,7,8,10,12]:
		day=31
	else:
		day=30
	return day
print(countDays(2018,2))
print(countDays(2015,7))


# #7 判断水仙花数
def isNarcNum(n):
	flag=False
	s=0
	numYushu=0
	num=n
	

	L=len(str(n))
	while num!=0:
		numYushu=(num%10)**L
		s=s+numYushu
		num=num//10
	if s==n:
		flag=True
	return flag

print(isNarcNum(153))



#8 杨辉三角


9 判断质数
def isPrime(n):
	flag=True
	num=n
	for i in range(2,num):
		if num%i==0:
			flag=False
	return flag

print(isPrime(18))


#10 水仙花数
def printNarcNum(n):
	s=''
	numYushu=0
	
	ac=n
	
	for i in range(100,ac+1):
		a=0
		L=len(str(i))
		num=i
		while num!=0:
			numYushu=(num%10)**L
			a=a+numYushu
			num=num//10
		if a==i:
			print(a)

printNarcNum(2333)