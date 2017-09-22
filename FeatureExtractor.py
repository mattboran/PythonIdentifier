import sys, getopt, random, time
from Identifier import *

'''
In this file, we gather the features from each book and read it into a .csv file.

The execution of this program is done by command line. The arguments taken specify directory of books, iterations per book, and output file

arg0 - FeatureExtractor.py
arg1 - directory
arg2 - iterations
arg3 - output file

'''

#featnames is a list of all the names of the features we extracted from our text. This is the "header" of the output .csv
featnames = ["Paragraphs," ,"CharperLine,", "Pronouns,", "ing,", "Exclamations,","Commas,","Adverbs,","Hyphens,","Alliteration,","ShortRatio,","LongWords,", ":", ";","Author\n"]

#directory = verify_directory(sys.argv[1])
#print("Directory = ", directory)
directory = str(sys.argv[1])

iterations = int(sys.argv[2])

outputfilename = str(sys.argv[3])

filenames = get_filenames(directory)
authnames = get_authornames(filenames)

fullfilenames = []
for f in filenames:
	fullfilenames.append(directory + f)

out_file = open(outputfilename, 'w')
out_file.write(''.join(featnames))
out_line = ''
start_time = time.time()
#now we've assembled our filenames, and know their true class. Let's iterate over each one N times then
for f in fullfilenames:
        
        num_words = 0
        file = open(f, 'r')
        #print("Working with " + f + " as our file. ")
        for line in file:
                words = line.split()
                num_words += len(words)
        
        for i in range(0, iters):
                charstream = get_block_by_char(f, random.randint(0, num_words-1500))
                out_line += (str(get_num_paragraphs(charstream)) + ', ')
                out_line += (str(get_char_per_line(charstream)) + ', ')
                out_line += (str(count_pronouns(charstream)) + ', ')
                out_line += (str(count_words_ending_in(charstream, "ing")) + ', ')
                out_line += (str(count_word(charstream,"!")) + ', ')
                out_line += (str(count_word(charstream,",")) + ', ')
                out_line += (str(count_words_ending_in(charstream, "ly")) + ', ')
                out_line += (str(count_word(charstream,"-")) + ', ')
                out_line += (str(count_alliteration(charstream)) + ', ')
                longWords = count_long_words(charstream)
                shortWords = count_short_words(charstream)
                longShortRatio = float(longWords)/float(shortWords)
                out_line += (str(longShortRatio) + ', ')
                out_line += (str(longWords) + ', ')
                out_line += (str(count_word(charstream,":")) + ', ')
                out_line += (str(count_word(charstream,";")) + ', ')
                out_line += get_authorname(f)
                out_line += '\n'
                out_file.write(out_line)
                out_line = ''
                        
print("Time elapsed: %f" % (time.time() - start_time))
out_file.close()
	
