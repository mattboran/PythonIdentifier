import os, random

def get_filenames(dir):
	'''
		Gets all filenames (no path) in a directory dir
	'''
	filenames = []
	for root, directories, files in os.walk(dir):
		for filename in files:
			#filepath = os.path.join(root, filename)
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
	f = open(fname, 'r')
	for word in f:
		i = i + 1
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
	
def count_instance_between(start, end, word, fname):
	return 0
	
	
filenames = get_filenames("Book txt")
authnames = get_authornames(filenames)

fullfilenames = []
for f in filenames:
	fullfilenames.append("Book txt\\" + f)
