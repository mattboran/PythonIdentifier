import os, random

def get_filenames(dir):
	'''
		Gets all filenames (no path) in a directory dir
	'''
	filenames = []
	for root, directories, files in os.walk(dir):
		for filename in files:
			filenames.append(filename)
	return filenames

def get_authornames(fnames):
	'''
		This function gets the names of the authors from the filename
	'''
	authnames = []
	for f in fnames:
		title = f.rsplit("_")
		auth = title[len(title)-1]
		authnames.append(auth[0:-4])
	return authnames
	
def get_numwords(fname):
	'''
		This function gets the number of words in the book
	'''
	i = 0
	with open(fname, 'r') as file:
		for word in file:
			i = i + len(word.split(" "))
	file.close()
	return i

def count_instance(w, block):
	'''
		Gets the number of occurances of "w" in block
	'''
	i = 0
	for word in block:
		if w in word:
			i = i + 1
	return i
	
def get_rand_startpoint(fname):
	'''
		This function gets a random start point in the book (starting number of words)
	'''
	numwords = get_numwords(fname)
	print("Numwords = ",numwords)
	return random.randint(0,numwords-1500)

def get_block_by_char(fname, start):
	'''
		This method returns a word block, but it's a string of characters not words. This is
		so that we can count characters per line, etc.
	'''
	#file = open(fname, 'wc')
	#numlines = len(file.splitlines())
	i = 0
	j = 0
	outchars = ''
	startrec = 0
	with open(fname, 'r') as file:
		for line in file:
			for word in line:
				if(word == ' ') or (word == '\n' ):
					i = i + 1
				if(i >= start):
					for char in word:
						outchars = outchars + char
				if(i >= start+1500):
					return outchars
	file.close()
	return outchars

def mean(nums):
	'''
		This function gets the arithmetic mean of elements of nums
	'''
	return float(sum(nums)) / max(len(nums), 1)
	
def get_char_per_line(chars):
	'''
		This method returns average number of characters per line
	'''
	i = 0
	numlines = 0
	charsperline = []
	for char in chars:
		i = i + 1
		if (char == '\n'):
			charsperline.append(i)
			numlines = numlines + 1
			i = 0
	return mean(charsperline)
			

def get_num_paragraphs(chars):
	'''
		This method counts number of paragraphs in a block. \n\n counts as a character
	'''
	i = 0
	streak = 0
	for char in chars:
		if char == '\n':
			streak = streak + 1
		else:
			streak = 0
		if streak == 2:
			i = i + 1
	return i


filenames = get_filenames("Book txt")
authnames = get_authornames(filenames)

fullfilenames = []
for f in filenames:
	fullfilenames.append("Book txt\\" + f)
print(fullfilenames[1])
print(get_numwords(fullfilenames[1]))
print(get_rand_startpoint(fullfilenames[1]))
chars = get_block_by_char(fullfilenames[1], 150)
print("chars per line = ",get_char_per_line(chars))
print("num paragraphs = ", get_num_paragraphs(chars))
