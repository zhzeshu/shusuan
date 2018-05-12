#求素数

# def findNumber():
# 	N1=n

# 	number=0
# 	for i in range(2,100001):
# 		for j in range(2,i-1):
# 			if i%j==0:
# 				break
		
# 		number=number+1
# 		if number==N1:
# 			print(i)


# def main():
# 	row=input()
# 	row=int(row)
# 	L=[]
# 	for i in range(row):
# 		nuM=input()
# 		nuM=int(nuM)
# 		L[i]=nuM

# 	for i in range(row):
# 		findNumber(L[i])


# if __name__=='__main__':
# 	main()


# import sys
# if __name__=='__main__':
# 	n=int(sys.stdin.readline().strip())
# 	ans=0
# 	for i in range(n):
# 		line=sys.stdin.readline().strip()
# 		values=list(map(int,line.split()))
# 		for v in values:
# 			ans+=v
# 	print(ans)

# if __name__=='__main__':
# 	ans=0
# 	line=sys.stdin.readline().strip()
# 	values=list(map(int,line.split()))
# 	ans=values[0]+values[1]
# 	print(ans)

# for line in sys.stdin:
# 	a=line.split()
# 	print(int(a[0])+int(a[1]))

# #3-1 反转输出字符串
# from pythonds.basic.stack import Stack
# def revstring(mystr):
# 	m=Stack()
# 	st=mystr
# 	for i in st:
# 		m.push(i)
# 	# print(m.size())pyt
# 	while not m.isEmpty():
# 		print(m.pop(),end='')

# revstring('Hello')

# class Stack:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def push(self, item):
#         self.items.append(item)#self.items.insert(0,item) 从栈顶变为栈底

#     def pop(self):
#         return self.items.pop()#return self.items.pop(0)

#     def peek(self):
#         return self.items[len(self.items)-1]#return self.items[0]

#     def size(self):
#         return len(self.items)

# import sys
# if __name__=='__main__':

# 	m=Stack()
# 	s=''
# 	st=sys.stdin.readline().strip()
# 	for i in st:
# 		m.push(i)
# 	while not m.isEmpty():
# 		s=s+str(m.pop())
# 	if st==s:
# 		print('Y')
# 	else:
# 		print('N')



# import sys
# if __name__=='__main__':
#     L=[]

#     num=int(sys.stdin.readline().strip())
#     while num!=0:
#         L.append(num)
#         num=int(sys.stdin.readline().strip())
#     print(L)
#     print(len(L))



# import sys
# if __name__=='__main__':
# 	L=[]
# 	num=int(sys.stdin.readline().strip())
# 	while num!=0 and num<=1000000:
# 		L.append(num)
# 		num=int(sys.stdin.readline().strip())
# 		# print(L)
# 		# print(len(L))

# 	for i in range(len(L)):
# 		f=L[i]
# 		if f==1 or f==2 or f==3 or f==4:
# 			print('0')

# 		else:
# 			fa=2
# 			fb=f-fa
# 			count=0
# 			while fa<=fb:
# 				factor1=True
# 				factor2=True
# 				for j in range(2,fa):
# 					if fa%i==0:
# 						factor1=False
# 						break
# 				for k in range(2,fb):
# 					if fb%k==0:
# 						factor2=False
# 						break
# 				if factor1 and factor2:
# 					count=count+1
# 				fa=fa+1
# 				fb=fb-1
# 			print(count)
# 	print('end')
# import math
# if __name__=='__main__':
# 	m,n=map(int,input().split())
# 	s=m
# 	n=n-1
# 	while n>0:
# 		m=math.sqrt(m)
# 		s=s+m
# 		n=n-1
# 	print(float('%0.2f'%s))

# #7 判断水仙花数
# def isNarcNum(n):
# 	flag=False
# 	s=0
# 	numYushu=0
# 	num=n
	

# 	L=len(str(n))
# 	while num!=0:
# 		numYushu=(num%10)**L
# 		s=s+numYushu
# 		num=num//10
# 	if s==n:
# 		flag=True
# 	return flag
# print(isNarcNum(153))

# if __name__=='__main__':
# 	m,n=map(int,input().split())
# 	flag=False
# 	for num in range(m-1,n+1):		
# 		s=0
# 		numYushu=0
# 		baoLiu=num
# 		L=len(str(num))
# 		while num!=0:			
# 			numYushu=(num%10)**L
# 			s=s+numYushu
# 			num=num//10

# 		if baoLiu==s:
# 			flag=True
# 			print(s, end=' ')
# 	if not flag:
# 		print('No')
# 	print()

# # 9 判断质数
# def isPrime(n):
#     flag=True
#     num=n
#     for i in range(2,num):
#         if num%i==0:
#             flag=False
#     return flag

# print(isPrime(18))
from math import sqrt
if __name__=='__main__':
	L=[]
	q=int(input())
	for i in range(q):
		L.append(int(input()))
	# print(L)

	def isPrime(n):
		flag=True
		num=n
		for j in range(2,int(sqrt(num))+1):
			if num%j==0:
				flag=False
		return flag

	for k in range(q):
		if L[k] ==1:
			print(2)
		else:
			count=1
			number=3
			while count<L[k]:
				if isPrime(number)==True:
					count=count+1
				number=number+1
			print(number-1)







	


