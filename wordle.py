import random

def import_words(): 
	fileContent = open ("./words.txt", 'r') 
	importedWords = fileContent.read().splitlines() 
	print(len(importedWords), "words imported" )
	words=[]
	for line in importedWords:
		if len(line)==5:
			words.append(line)
	print(len(words), "words kept")
	print("Example:", random.choice(words))
	return words

def printSection(message):
	print("")
	print("\033[1m" + message + "\033[0m")

printSection("Import & clean words")
wordlist = import_words ( )

printSection("Any field is optional. '_' for blank")
excluded = input("Excluded letters: ")
mispositioned = input("Mispositioned letters:\t")
mispositioned = mispositioned.ljust(5,"_")
mispositioned2 = input("Other mispositioned:\t")
mispositioned2 = mispositioned2.ljust(5,"_")
positioned = input("Positionned letters:\t")
positioned = positioned.ljust(5,"_")

candidates = []

for w in wordlist:
	for i,l in enumerate(w):
		if l in excluded:
			# An excluded letter is present
			break
		if mispositioned[i] == l or mispositioned2[i] == l  :
			# This is a non desirable position
			break
		if positioned[i] != '_' and positioned[i] != l :
			# There is a different expected letter
			break
	else:
		for l in mispositioned+mispositioned2:
			if l != '_' and l not in w:
				# a misplaced letter is not in the final word
				break
		else:
			candidates.append(w)

goodCandidates = []
otherCandidates = []
for c in candidates:
	for i,l in enumerate(c):
		if i<5 and l in c[i+1:]:
			# letter present twice
			otherCandidates.append(c)
			break
	else:
		goodCandidates.append(c)

printSection("Candidates with various letters:")
for c in goodCandidates:
	print(c)

printSection("Other candidates:")
for c in otherCandidates:
	print(c)