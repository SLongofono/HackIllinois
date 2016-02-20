import sys
inFile = open(sys.argv[1], 'r')
words = inFile.read().split(',')
out = open("perlineop.txt", "a+")
for i in words:
	out.write(i)
	out.write('\n')
inFile.close()
out.close()
