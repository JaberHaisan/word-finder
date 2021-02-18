# word_finder.py - Finds all words containing required letters and up to 
# maximum length.
# Uses words_alpha.txt from https://github.com/dwyl/english-words

import itertools

with open("words_alpha.txt") as f_obj:
	words = set(f_obj.read().splitlines())

letters = input("Letters which should be present: ")
maximum_length = int(input("Maximum length of word: "))

# Remove non unique letters.
letters = set(letters)

# Keep a gap between input and output.
print()

# Find all words that match up to maximum length.
for length in range(1, maximum_length + 1):
	
	# Get all possible combinations from letters equal to length.
	all_combinations = itertools.product(letters, repeat=length)

	matches = []
	for comb in all_combinations:
		joined_comb = "".join(comb)
		if joined_comb in words:
			matches.append(joined_comb)
	
	print("{}: ".format(length), end="")
	
	if matches:
		print(*matches, sep=", ")
	else:
		print("N/A")
	print()
