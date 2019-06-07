#############################
#		Question C			#
#############################

import re

class Cache():
	def __init__(self):
		self.cacheSize = 3
		self.cache = []

	def main(self):

		print("\nAdd item to cache, use string compose of contigent numbers, use 'quit()' to end the simulation:\n")
		x=input("+ ")
		if self.inputVerification(x):
			self.setCache(x)


		if x != "quit()":
			print(self.cache)
		
		while x != "quit()":
			x=input("+ ")
			if self.inputVerification(x):
				self.setCache(x)
			if x != "quit()":
				print(self.cache)


	def setCache(self, cacheInput):
		if (len(self.cache) != self.cacheSize):
			self.cache.insert(0, cacheInput)
		elif(len(self.cache) == self.cacheSize):
				if cacheInput in self.cache:
					self.cache.pop(self.cache.index(cacheInput))
					self.cache.insert(0, cacheInput)
				elif cacheInput not in self.cache:
					self.cache.pop(self.cacheSize-1)
					self.cache.insert(0, cacheInput)


	def inputVerification(self, cacheInput):
		if re.match('^[0-9]+$', cacheInput):
			return True
		elif cacheInput == "quit()":
			return False
		else:
			print('\''+cacheInput + '\'' + "is not valide data type")
			return False


if __name__ == '__main__':
	c=Cache()
	c.main()