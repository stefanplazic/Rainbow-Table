import md5
import time
import pickle

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
			f.write(hashed_words[key]+ " : " + key)
			f.write('\n')


if __name__ == '__main__':

	start = time.time()
	#hash words and put them to dictionary
	hashed_words = create_hash('words.txt')
	end = time.time()

	print "Time past: " + str(end-start)

	save_hash(hashed_words)

	print 'hash file saved'
	
