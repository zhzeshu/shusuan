# -*- coding: utf-8 -*-
class People(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def getName(self):
		return self.name

	def getAge(self):
		return self.age

p=people('Jack',37)
print(p.getName(),p.getAge())

#初始化后要赋值，继承的是方法
#__xxxx这种变量是限制访问

class Student(People):
	def __init__(self,name,age,id):
		self.name=name
		self.age=age
		self.id=id

	def getId(self):
		return self.id

s=Student('Tess',18,'1700000001')
print(s.getName(),s.getAge(),s.getId())


#3 Xdit 类
class Xdict(dict):
	def getKeys(self,value):

		return Xdict.getKeys(value)

xd=Xdict({2:'a',3:'a',4:(2,3)})
print(xd.getKeys('a'))


#4 vector 类
import math
class Vector(object):
	def __init__(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z
		
	def __add__(self,other):
		x=self.x+other.x
		y=self.y+other.y
		z=self.z+other.z
		return Vector(x,y,z)
	def __sub__(slef,other):
		x=self.x-other.x
		y=self.y-other.y
		z=self.z-other.z
		return Vector(x,y,z)
	def __mul__(self,other):
		x=self.x*other
		y=self.y*other
		z=self.z*other
		return Vector(x,y,z)
		
	def __truediv__(self,other):
		x=self.x/other
		y=self.y/other
		z=self.z/other
		return Vector(x,y,z)
		
	def __str__(self):
		return str(self.x,self.y,self.z)

v1 = Vector(1,1,2)
v2 = Vector(2,4,2)
print(v1+v2)
print(v1*12)
print(v2/2)	
