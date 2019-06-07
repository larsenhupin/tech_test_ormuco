#############################
#		Question A			#
#############################

class LineOverlap():
	def __init__(self):
		self.x1=0
		self.x2=0
		self.x3=0
		self.x4=0

	def main(self):
		self.inputCoord()

		if(self.line_verification() == True):
			self.find_overlap()

	def inputCoord(self):
		self.x1 = input("\nx1:")
		self.x2 = input("x2:")
		self.x3 = input("x3:")
		self.x4 = input("x4:")

	def find_overlap(self):
		entete='\nL1('+self.x1+','+self.x2+')'+ 'and '+ 'L2('+self.x3+','+self.x4+') '

		if (self.x2 >= self.x3 or self.x4 <= self.x1):
			print(entete + 'overlap')
		else:
			print(entete + 'do not overlap')

	def line_verification(self):
		if (self.x1 >= self.x2):
			print("\nL1 is not valid")
			return False
		elif(self.x3 >= self.x4):
			print("\nL2 is not valid")
			return False
		else:
			return True

if __name__ == '__main__':
	lineoverlap=LineOverlap()
	lineoverlap.main()