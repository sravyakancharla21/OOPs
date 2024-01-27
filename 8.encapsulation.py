#Encapsulation 
class india:
	def __init__(self):
		self.a='andhra'
		self._b='telangana'    #protected member
		self.__c='karnataka'   #private member
#both protected and private members are accessed in the class itself
	def states(self):
		print(self.a)
		print(self._b)
		print(self.__c)

class country(india):
	def child(self):
		print(self.a)
		print(self._b)
		print(self.__c)

obj=india()
obj.states()       # returns   'andhra'   'telangana'   'karnataka'

print(obj.a)       #returns 'andhra'
print(obj.b)       #throws an error because we cannot access outside the class
print(obj.c)       #throws an error because we cannot access outside the class

obj1=country()
obj1.child()      #returns 'andhra'       'telangana'
				  # does not return 'karanataka' because  we cannot access private member  in the child class

print(obj1.a)               #returns 'andhra'
print(obj1.b)       #throws an error because we cannot access outside the class
print(obj1.c)       #throws an error because we cannot access outside the class


