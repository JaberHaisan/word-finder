# word_finder.py - Finds all words containing required letters and up to 
# maximum length.
# Uses words_alpha.txt from https://github.com/dwyl/english-words

import itertools

with open("words_alpha.txt") as f_obj:
	words = set(f_obj.read().splitlines())

letters = input("Letters which should be present: ")
maximum_length = int(input("Maximum length of word: "))

# Keep a gap between input and output.
print()

for length in range(1, maximum_length + 1):
	# Get all possible combinations from letters equal to length.
	all_combinations = itertools.product(letters, repeat=length)

	matches = []
	for perm in all_combinations:
		word = "".join(perm)
		if word in words:
			matches.append(word)
	
	print("{}: ".format(length), end="")
	print(*matches, sep=", ", end="\n")
	print()
