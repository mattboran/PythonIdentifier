import os, random, re

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

def get_authorname(fname):
	'''
		This function gets the name of the author from the filename
	'''
	title = fname.rsplit("_")
	auth = title[len(title)-1]
	return auth[0:-4]

def get_numwords(file):
	'''
		This function gets the number of words in the book
	'''
	i = 0
	for line in file:
		words = line.split()
		i += len(words)
	return i

def count_instance(w, block):
	'''
		Gets the number of occurances of "w" in block. This is deprecated; it works on word-by-word basis.
	'''
	i = 0
	for word in block:
		if w in word:
			i = i + 1
	return i
	
def get_rand_startpoint(numwords):
	'''
		This function gets a random start point in the book (starting number of words)
	'''
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
	
def count_pronouns(chars):
	'''
		This function takes an incoming charstream and counts instance of pronouns
		We will use the Regular Expression package to do this for full matches
	'''
	i = 0 
	text = ''.join(chars).lower()
	pronouns = re.findall("he|she|it|I|you|we|they|me|us|them|my|your|his|her|its|it\'s|our|their|mine|yours|hers|ours|theirs|myself|yourself|himself|itself|ourselves|yourselves|themselves",text)
	return len(pronouns)

def count_word(chars, word):
	'''
		This function searches for and returns the number of times 'word' appears in the char stream 'chars'
	'''
	text = ''.join(chars).lower()
	words = re.findall(word, text)
	return len(words)
	
def get_first_letters(chars):
	'''
		This function returns a charstream containing the first letter of every word in 'chars'
	'''
	
	firstchars = []
	text = ''.join(chars).lower()
	
	for line in text.splitlines():
		for word in line.split():
			if(word[0] != '' or word[0] != ' ') and (word[0].isalpha()):
				firstchars.append(word[0])
	return firstchars

def count_alliteration(chars):
	'''
		This function searches for instances of alliteration - three words or more in a row that start with the same letter.
	'''
	allitcount = 0
	streak = 0
	firstletters = get_first_letters(chars)
	current = firstletters[0]
	for i in range (0,len(firstletters)-1):
		if(firstletters[i] == firstletters[i+1]):
			streak += 1
		if (streak > 1):
			allitcount += 1
			streak = 0
		if(firstletters[i] != firstletters[i+1]):
			streak = 0
	return allitcount
		
def count_short_words(chars):
	'''
		This function counts the number of short words - words with less than 6 chars
	'''
	text = ''.join(chars)
	i = 0
	for word in text.split():
		if len(word) <= 5 and (word != '' and word != ' '):
			i += 1
	return i
	
def count_long_words(chars):
	'''
		This function counts the number of long words - words with 6 or more chars
	'''
	text = ''.join(chars)
	i = 0
	for word in text.split():
		if len(word) >= 5:
			i += 1
	return i
	
def count_words_ending_in(char, pattern):
	'''
		This function counts the number of words that end in 'pattern'
	'''
	text = ''.join(char).lower()
	i = 0
	pattern_punctuation = []
	pattern_punctuation.append(pattern)
	pattern_punctuation.append(pattern + '.')
	pattern_punctuation.append(pattern + '"')
	pattern_punctuation.append(pattern + '\'')
	pattern_punctuation.append(pattern + '-')
	pattern_punctuation.append(pattern + '.')
	pattern_punctuation.append(pattern + '?')
	pattern_punctuation.append(pattern + ',')
	pattern_punctuation.append(pattern + '!')
	pattern_punctuation.append(pattern + '*')
	pattern_punctuation.append(pattern + ':')
	pattern_punctuation.append(pattern + ';')
	
	for word in text.split():
		for test in pattern_punctuation:
			if word.endswith(test):
				i += 1
	return i
	
def verify_directory(directory):
	'''
		This function verifies that the directory is specified as "Directory\" to the program. So we can find the file appropriately when fed from
		the argv list in FeatureExtractor
	'''
	if(directory.endswith('\\')):
		directory += '\\'
	elif(directory.endswith('/')):
		directory[-1] = '\\'
		directory += '\\'
	else:
		directory += '\\'
	return directory
		

