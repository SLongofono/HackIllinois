import random
import sys

#guess what this does...
def capitalize(word):
	if len(word) > 0:
		y = word[0].upper()
		return y + word[1:]
	else:
		return ''

#builds word bank for parts of speech lists
def fetchLists(root):
	v = open(root + "/lists/verbs.txt", 'r')
	n = open(root + "/lists/nouns.txt", 'r')
	pn = open(root + "/lists/proper_nouns.txt", 'r')
	a = open(root + "/lists/adjectives.txt", 'r')

	verbs = v.read().split('\n')
	nouns = n.read().split('\n')
	pnouns = pn.read().split('\n')
	adjs = a.read().split('\n')

	v.close()
	n.close()
	pn.close()
	a.close()
	
	return (verbs, nouns, pnouns, adjs)

#builds 2D lists of sentences and word tokens
def fetchParagraphs(paragraphpath):
	p1 = open(paragraphpath, 'r')

	#paragraphs with one sentence per line (makes capitalization & punctuation easier)
	temp = p1.read().split('\n')
	p1.close()

	#listify our sentences
	sentences = []
	for i in temp:
		sentences.append(i.split(' '))
	return sentences


def genOutput(sentences, verbs, nouns, pnouns, adjs):
	#For each sentence
	for i in sentences:

		#if we match a meta pattern, fetch a random 
		for j in range (len(i)):

			if i[j] == "PN":
				#make sure we don't get the EOF line
				x = random.choice(pnouns)
				while(len(x) < 1):
					x = random.choice(pnouns)	
				i[j] = x
	
			elif i[j] == 'N':
				x = random.choice(nouns)
				while(len(x) < 1):
					x = random.choice(nouns)	
				i[j] = x
		
			elif i[j] == 'J':
				x = random.choice(adjs)
				while(len(x) < 1):
					x = random.choice(adjs)	
				i[j] = x

			elif i[j] == 'V':
				x = random.choice(verbs)
				while(len(x) < 1):
					x = random.choice(verbs)	
				i[j] = x

		#capitalize the first word
		i[0] = capitalize(i[0])

	#Get rid of EOF line (not portable)
	#sentences.pop(-1)


	#build output strings
	output = ''

	for i in sentences:
		if len(i)==0:
			pass
		else:
			for j in i:
				if j == ',':
					output += ','
				else:
					output += ' ' + j
			output += '. '
	#hackity hack too tired to find this bug
	return output[:len(output)-2]

#Generates a number of populated copy patterns
def genCopy(path, paragraphpath, repeats=1):
	verbs, nouns, pnouns, adjs = fetchLists(path)
	sentences = fetchParagraphs(paragraphpath)
	if(repeats < 1):
		print "Error - repeats must be greater than or equal to one\n\n"
	elif(repeats > 1):
		result = []

		for i in range(repeats):
			result.append(genOutput(sentences, verbs, nouns, pnouns, adjs))
		return result
	else:
		return genOutput(sentences, verbs, nouns, pnouns, adjs)

if __name__ == "__main__":
	import sys
	if len(sys.argv) < 3:
		print "\n\nUsage: python paragraph.py <path to pararaph definitions> <full path of desired paragraph pattern>\n\n"
		sys.exit(0)
	if len(sys.argv) == 4:
		x = genCopy(sys.argv[1], sys.argv[2], int(sys.argv[3]))	
	else:
		x = genCopy(sys.argv[1], sys.argv[2])	
	print x, '\n\n'
