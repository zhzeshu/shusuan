# -*- coding: utf-8 -*-


#3-1 反转输出字符串
from pythonds.basic.stack import Stack
def revstring(mystr):
	m=Stack()
	st=mystr
	for i in st:
		m.push(i)
	# print(m.size())pyt
	while not m.isEmpty():
		print(m.pop(),end='')

# revstring('Hello')
# print('hello')




#分析括号准确与否
def parChecker(symbolString):
	s=Stack()
	balanced=True
	index=0
	i=0
	while index<len(symbolString)and balanced:
		symbol=symbolString[index]
		if symbol=='(':
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced =False
			else:
				s.pop()
		index=index+1

	if balanced and s.isEmpty():
		return True
	else:
		return False

# print(parChecker('((()))'))
# print(parChecker('((()'))

#分析各种括号{[()]}
def parChecker1(symbolString):
	s=Stack()
	balanced=True
	index=0
	while index<len(symbolString) and balanced:
		symbol=symbolString[index]
		if symbol in '([{':
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced=False
			else:
				top=s.pop()
				if not matches(top,symbol):
					balanced=False
		index=index+1
	if balanced and s.isEmpty():
		return True
	else:
		return False

def matches(open,close):
	opens='([{'
	closers=')]}'
	return opens.index(open)==closers.index(close)

# print(parChecker1('{{[()]}}'))


#十进制转化为二进制
def dividedBy2(decNumber):
	remstack=Stack()
	while decNumber>0:
		rem=decNumber%2
		remstack.push(rem)
		decNumber=decNumber//2

	binString=''
	# binString=0
	while not remstack.isEmpty():
		binString=binString+str(remstack.pop())#字符串组合延长
		# binString=binString*10+remstack.pop()

	return binString

# print(dividedBy2(42))


#10进制转化为任意进制
def baseConverter(decNumber,base1):
	digits='0123456789ABCDEF'

	remstack=Stack()
	# rem=0
	while decNumber>0:
		rem=decNumber%base1
		remstack.push(rem)
		decNumber=decNumber//base1

	newString=''
	while not remstack.isEmpty():
		#字符串里面的第几个，用list方法来定位
		newString=newString+digits[remstack.pop()]

	return newString

# print(baseConverter(25,2))
# print(baseConverter(25,16))



#公式转化为后进式
def infixToPostfix(infixexpr):
	#操作符优先级
	prec={}
	prec['^']=3
	prec['*']=3
	prec['/']=3
	prec['+']=2
	prec['-']=2
	prec['(']=1

	opStack=Stack()
	postfixList=[]
	#解析表达式到单词列表 str -- 分隔符，
	#默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
	tokenList=infixexpr.split()

	for token in tokenList:
		#字符串是A-Z或0-9
		# if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':

		#字符串是数字
		if token.isdigit():
			postfixList.append(token)
		elif token=='(':
			opStack.push(token)
		elif token==')':
			topToken=opStack.pop()
			while topToken!='(':
				postfixList.append(topToken)
				topToken=opStack.pop()
		else:
			while(not opStack.isEmpty()) and (prec[opStack.peek()]>=prec[token]):
				postfixList.append(opStack.pop())
			opStack.push(token)

	while not opStack.isEmpty():
		postfixList.append(opStack.pop())
	return ' '.join(postfixList)

# print(infixToPostfix('A * B + C * D'))
print(infixToPostfix(' 10 + 3 * 5 / ( 16 - 4 )'))
print(infixToPostfix('5 * 3 ^ ( 4 - 2 )'))


#计算后缀表达式的值
def postfixEval(postfixExpr):
	operandStack=Stack()
	tokenList=postfixExpr.split()

	for token in tokenList:
		# if token in '0123456789':
		if token.isdigit():
			operandStack.push(int(token))
		else:
			operand2=operandStack.pop()
			operand1=operandStack.pop()
			result=doMath(token,operand1,operand2)
			operandStack.push(result)
	return operandStack.pop()

def doMath(op,op1,op2):
	if op=='*':
		return op1*op2
	elif op=='/':
		return op1/op2
	elif op=='+':
		return op1+op2
	else:
		return op1-op2

print(postfixEval(' 10 3 5 * 16 4 - / + '))
print(postfixEval(' 5 3 * 4 2 - ^ '))



#======================================================================
#Queue
#热土豆问题
from pythonds.basic.queue import Queue

def hotPotato(namelist,num):
	simqueue = Queue()
	for name in namelist:
		simqueue.enqueue(name)
	while simqueue.size() > 1:
		for i in range(num):
			simqueue.enqueue(simqueue.dequeue())
		simqueue.dequeue()
	return simqueue.dequeue()

# print(hotPotato(['A','B','C','D','E','F'],3))


#----------------------------------------------------------------------
#打印问题
import random

class Printer:
	def __init__(self,ppm):
		self.pagerate = ppm
		self.currentTask = None
		self.timeRemaining = 0

	def tick(self):
		if self.currentTask!=None:
			self.timeRemaining=self.timeRemaining-1
			if self.timeRemaining<=0:
				self.currentTask=None
	def busy(self):
		if self.currentTask!=None:
			return True
		else:
			return False
	#打印新作业
	def startNext(self,newtask):
		self.currentTask=newtask
		self.timeRemaining=newtask.getPages()*60/self.pagerate

class Task:
	def __init__(self,time):
		self.timestamp=time
		#打印页数
		self.pages=random.randrange(1,21)
	def getStamp(self):
		return self.timestamp
	def getPages(self):
		return self.pages
	def waitTime(self,currenttime):
		return currenttime-self.timestamp

def simulation(numSeconds,pagesPerMinute):
	labprinter=Printer(pagesPerMinute)
	printQueue=Queue()
	waitingtimes=[]

	for currentSecond in range(numSeconds):
		if newPrintTask():
			task=Task(currentSecond)
			printQueue.enqueue(task)
		if (not labprinter.busy()) and (not printQueue.isEmpty()):
			nexttask=printQueue.dequeue()
			waitingtimes.append(nexttask.waitTime(currentSecond))
			labprinter.startNext(nexttask)
		labprinter.tick()

	averageWait=sum(waitingtimes)/len(waitingtimes)
	print('average wait %6.2f secs %3d tasks remaining.' %(averageWait,printQueue.size()))

def newPrintTask():
	num=random.randrange(1,181)
	if num==180:
		return True
	else:
		return False

# def main():
# 	for i in range(10):
# 		simulation(3600,10)

# if __name__=='__main__':
# 	main()

#==================================================================
#Deque
#回文词判定
from pythonds.basic.deque import Deque

def palchecker(aString):
	chardeque=Deque()
	for ch in aString:
		chardeque.addRear(ch)

	stillEqual=True

	while chardeque.size()>1 and stillEqual:
		first=chardeque.removeFront()
		last=chardeque.removeRear()
		if first!=last:
			stillEqual=False

	return stillEqual
# print(palchecker('lsdkjfskf'))
# print(palchecker('ardra'))

#================================================================
#链表
class Node:
	def __init__(self,initdata):
		self.data=initdata
		self.next=None
	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def setData(self,newData):
		self.data=newData
	def setNext(self,newnext):
		self.next=newnext

class UnorderedList:
	def __init__(self):
		self.head=None

	def isEmpty(self):
		return self.head == None

	def add(self,item):
		temp=Node(item)
		temp.setNext(self.head)
		self.head=temp

	def size(self):
		current=self.head
		count=0
		while current != None:
			count=count+1
			current=current.getNext()
		return count

	def search(self,item):
		current=self.head
		found=False
		while current!=None and not found:
			if current.getData()==item:
				found=True
			else:
				current=current.getNext()
		return found
	
	def remove(self,item):
		current=self.head
		previous=None
		found=False
		while not found:
			if current.getData()==item:
				found=True
			else:
				prevous=current
				current=current.getNext()
		
		if previous==None:
			self.head=current.getNext()
		else:
			previous.setNext(current.getNext())#删除的方法采用previous自动对应next

#有问题的append，有机会要修改------------------------------------------------------------
	def append(self,item):
		current=self.head
		temp=Node(item)		
		while current.getNext()!=None:
			current=current.getNext()
		temp.setNext(current.getNext())
		current.setNext(temp)

	def getIndex(self,item):
		current=self.head
		index=0
		found=False
		while current!=None:
			if current.getData()==item:
				found=True
				break
			else:
				current=current.getNext()
				index=index+1
		if not found:
			index=None
		return index

	def getItem(self,index):
		current=self.head
		for i in range(index):
			current=current.getNext()
		if current!=None:
			return current.getData()
		else:
			raise('index out of range')

	def pop(self,index):
		self.remove(self.getItem(index))

	def insert(self,index,item):
		current=self.head
		temp=Node(item)
		for i in range(index):
			previous=current
			current=current.getNext()
		temp.setNext(current.getNext())
		current.setNext(temp)

	
	# def show(self):
	# 	current=self.head
	# 	while current != None:
	# 		current=current.getNext()
	# 		print(current.getData())


# alist = UnorderedList()
# alist.add(30)
# alist.add(31)
# alist.add(27)
# alist.append(100)
# alist.append(101)
# alist.show()
# # print(alist.getIndex(27))
# # print(alist.getItem(4))
# # alist.pop(4)
# # print(alist)
# # alist.insert(1, 5)
# print(alist)


#============================================================
#有序表OrderedList
class Student:
	def __init__(self, name, grade):
		self.name, self.grade = name, grade
	def __lt__(self, other):
		return self.grade > other.grade
		# return self.name < other.name
	def __str__(self):
		return '(%s,%d)' % (self.name, self.grade)
	#student的正式字符串表示
	__repr__ = __str__

# s=list()
# s.append(Student('Jack',80))
# s.append(Student('Jane',75))
# s.append(Student('Smith',82))
# s.append(Student('Cook',90))
# s.append(Student('Tom',70))
# print('Original:',s)
# s.sort()
# print('Sorted:',s)
#-----------------------------------------------------------------
class OrderedList:
	def __init__(self):
		self.head = None
	
	def isEmpt(self):
		return self.head == None
	
	def size(self):
		current = self.head
		count = 0
		while current is not None:
			count=count+1
			current=current.getNext()
		return count

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				prevous = current
				current = current.getNext()
			if previous is None:
				self.head = current.getNext()
			else:
				previous.setNext(current.getNext())

	def search(self,item):
		current = self.head
		found = False
		stop = False
		while current != None and not found and not stop:
			if current.getData() == item:
				found = True
			else:
				if current.getData()>item:
					stop = True
				else:
					current = current.getNext()
		return found

	def add(self, item):
		current = self.head
		previous=None
		stop=False
		#发现插入位置
		while current!=None and not stop:
			if current.getData()>item:
				stop=True
			else:
				previous=current
				current=current.getNext()
		temp=Node(item)
		#插入表头
		if previous==None:
			temp.setNext(self.head)
		#插入表中
		else:
			temp.setNext(current)
			previous.setNext(temp)


