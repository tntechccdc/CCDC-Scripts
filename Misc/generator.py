#Sam Wehunt 9/30/2015
"""
this script finds four random words from a file (nounlist.txt) and displays them
used for password generation
the seed for the random number generator is something that the user enters, which makes the password
	regeneratable given the same "key", and because of this i'm not sure how "cryptographically secure" this is
"""
import optparse
import random
import binascii

#pre: filename is a string that is the name of the file where the key is contained
#post: an integer is returned that is generated randomly based on the key
def processKey(key):
	binKey = str2bin(key)
	
	total = 0
	for count in binKey:
		total = total + int(count, 10)
	
	return total % len(key)

#pre: message is a string of ascii characters
#post: returns a string of 0's and 1's which represents the message in it's binary form
def str2bin(message):
	binary = bin(int(binascii.hexlify(message), 16))
	return binary[2:]

#pre: filename is the name of a txt file, linenum is a number of a line to be read
#post: returns the line in the file at linenum, returns None if that line was not found (out of range)
def getLine(filename, linenum):
  f = open(filename)

  for i, line in enumerate(f):
    if (i == linenum - 1):
      f.close()
      return line.strip('\n')
  print "Invalid line index"
  return None

#counts the number of lines in a file, this is so my random getline doesn't go OOB
def countLines(filename):
	f = open(filename)
	for i, line in enumerate(f):
		pass
	return i + 1

#takes in a string (word) and returns the same string, but with the first letter capitalized
#you may say its pointless, or dumb, but I love it
def capWord(word):
	first = word[0]
	capped = first.upper()+word[1:]
	return capped
	
#takes in a filename, and smacks four random lines from it together like [1-2-3-4], instapassword
def makePass(filename):
	numlines = countLines(filename)
	finalPass1 = capWord(getLine(filename, random.randrange(1, numlines, 1)))
	finalPass2 = capWord(getLine(filename, random.randrange(1, numlines, 1)))
	finalPass3 = capWord(getLine(filename, random.randrange(1, numlines, 1)))
	finalPass4 = capWord(getLine(filename, random.randrange(1, numlines, 1)))

	finalPass = finalPass1 + "-" + finalPass2 + "-" + finalPass3 + "-" + finalPass4
	return finalPass
	
#seeds the RNG, i made this separate because sometimes I like to make my "random" sets reproducible
#but other times i want to seed the RNG with something more secure, like the current time or whatnot
def seedRNG():
	random.seed(processKey(raw_input("enter key: ")))
	
def toFile(filename, words):
	f = open(filename, "w")
	for word in words:
		f.write(word + "\n")
	f.close()

if __name__ == "__main__":
	seedRNG()
	numPasses = int(raw_input("how many passwords do you want to generate? "))
	
	allpasses = []
	i=0
	
	print "\n"
	while i < numPasses:
		currPass = makePass("nounlist.txt")
		print currPass
		allpasses.append(currPass)
		i += 1
	print "\n"
		
	choice = raw_input("do you want me to write these to a .txt file? (y/n) ")
	if choice == "y" or choice == "Y":
		filename = raw_input("what shall we call this file? (omit extension) ") + ".txt"
		toFile(filename, allpasses)
		print "file written"
	
