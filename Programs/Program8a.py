def _abecedarian(word):
	test=list(word)
	if test.sort()==test:
		return True
	return False
word=input("Enter a word: ")
print(_abecedarian(word))