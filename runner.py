import md5
import time

import os.path


hashed_path='hashed.txt'

def create_hash(path=''):

	words = {}
	m = md5.new()
	with open(path) as f:
		for line in f:
			m = md5.new()
			m.update(line)
			words[m.hexdigest()] = line

	return words

def save_hash(hashed_words, path='hashed.txt'):

	with open(path, 'w') as f:
		for key in hashed_words:
			f.write(hashed_words[key]+ ":" + key)
			f.write('\n')

'''
laod file data
'''
def load_hash():
	words = {}
	with open(hashed_path) as f:
		for line in f:
			vals = line.split(":")
			#put into dict
			print vals
			#words[vals[1]] = vals[0]

	return words

'''
take user input - and find if hash exists
'''
def enter_word(words):

	while True:
		print "Enter word: \n"
		user_input = raw_input()

		#check if words is in dict
		if user_input in words:
			print "Word founded: " + words[user_input]
		else:
			print "No such word"

		#check if user wants to continue
		print "Do you want to continue? \n"
		user_input = raw_input()

		if user_input.lower() == 'n':
			break

if __name__ == '__main__':

	
	if os.path.isfile(hashed_path):

		# if hashed.txt file exists
		words = load_hash()

		#enter the word
		enter_word(words)
	
	else:
		
		#hashed.txt doesn't exists
		print "Enter original text location: \n"
		loc_path = raw_input()
		words = create_hash(loc_path)

		enter_word(words)
		save_hash(words)



	
