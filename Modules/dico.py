
class Dico:
	"""
	"""
	
	def __init__(self, dico = {}, **param):
		
		self.__keys = list()
		self.__values = list()
		
		if type(dico) != dict :
			raise TypeError(" Dico take can take only dictionary and named parameters as parameters !!")
		
		self.__keys += list(dico.keys()) + list(param.keys())
		self.__values += list(dico.values()) + list(param.values())
	
	def keys(self):
		return list(self.__keys)
	
	def values(self):
		return list(self.__values)
	
	def __repr__(self):
	
		dicoStr = "{"
		for index,key in enumerate(self.keys()):
			if type(key) == str:
				dicoStr +="\n   [ '{}' ] => {} \n".format(key,self.values()[index])
			else:
				dicoStr +="\n   [ {} ] => {} \n".format(key,self.values()[index])
		return dicoStr+"}"
	
	def __len__(self):
		return len(self.keys())
	
	def items(self):
		itemList = list()
		for index, key in enumerate (self.keys()):
			itemList.append((key, self.values()[index]))
		return itemList

	def __add__(self, dico):
		if type(dico) != type(self):
			raise TypeError(" We can add only Dico with Dico")
		key = self.keys() + dico.keys()
		value = self.values() + dico.values()
		newDico = {}
		for index,val in enumerate(key):
			newDico[val] = value[index]
		return Dico(newDico)

	def reverse(self):
		self.__values.reverse()
		self.__keys.reverse()
		
		
	def __contains__(self,itemKey):
		for key in self.keys():
			if key == itemKey:
				return True
		return False

	def __getitem__(self,key):
		if key not in self.keys():
			raise KeyError("the key "+key+" not exits in this Dico")
		return self.values()[self.keys().index(key)]
	
	def __setitem__(self, key, value):
		if type(key) not in (int,float,str,tuple):
			raise KeyError ("Sorry ,the Dico key can only be an immutable type")
		
		self.__keys.append(key)
		self.__values.append(value)
	
	def __delitem__(self,key):
		if key not in self.keys():
			raise KeyError ("the specified key is not in Dico")
		del self.__values[self.keys().index(key)]
		self.__keys.remove(key)
	
	def sort(self, reverse=False):
		pass
		sortedkey = sorted(self.keys())
		if reverse:
			sortedkey.reverse()
		newValue = list()
		for key in sortedkey:
			newValue.append(self.value()[self.keys().index(key)])
		
		self.__keys = sortedkey
		self.__values = newValue
	
	#to do itr and sort
	



