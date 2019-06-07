#############################
#		Question B			#
#############################

import re

class VersionControl():
	def __init__(self):
		self.VString1 = ''
		self.VString2 = ''

	def main(self):
		self.inputVersion()

		if(self.string_verification() == True):
			self.find_version_order()

	def inputVersion(self):
		self.VString1 = input("\nVersion 1: ")
		self.VString2 = input("Version 2: ")

	def find_version_order(self):
		v1Split = self.VString1.split('.')
		v2Split = self.VString2.split('.')

		v1Split = list(map(int, v1Split))
		v2Split = list(map(int, v2Split))

		v1Lenght = len(v1Split)
		v2Lenght = len(v2Split)

		if v1Lenght > v2Lenght:
			for i in range(v1Lenght-v2Lenght):
				v2Split.append(0)
		elif v2Lenght > v1Lenght:
			for i in range(v2Lenght-v1Lenght):
				v1Split.append(0)

		#print(v1Split)
		#print(v2Split)

		for i in range(0, v1Lenght):
			if v1Split[i] < v2Split[i]:
				print("\nV2 is greater than V1")
				return
			elif v1Split[i] > v2Split[i]:
				print("\nV1 is greater than V2")
				return
			elif v1Split[i] == v2Split[i] and i == len(v1Split)-1:
				print("\nV1 is equal to V2")

	def string_verification(self):
		# need better verification
		if re.match('^[0-9]+\.[0-9]', self.VString1) and re.match('^[0-9]+.[0-9]', self.VString2):
			return True
		else:
			print("\none of the input is not valid")
			return False

if __name__ == '__main__':
	vs=VersionControl()
	vs.main()