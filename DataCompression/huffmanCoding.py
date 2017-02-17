import operator


class binaryTree:
	def __init__(self):
		self.left = None
		self.right = None
		self.count = 0
		self.data = None


def getByteList(readFile):
	result = []
	for line in readFile:
		result.extend([x for x in line])

	return result
	

def populateTree(t, sortedTuple):
	pass
	

def main():
	byteDict = {}
	fileToCompress = raw_input('file to compress:')
	f = open(fileToCompress)
	byteList = getByteList(f)
	uniqueBytes = list(set(byteList))
	for i in uniqueBytes:
		byteDict[i] = byteList.count(i)
		
	sorted_x = reversed(sorted(byteDict.items(), key=operator.itemgetter(1)))
	
	# (byte, #occurences)
	for each in sorted_x:
		print each
	
	
		
if __name__ == "__main__":
	main()
		

