# this is the testing of some function along with concatanation and Pig Latin
pyg = 'ay'
original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
# converting my original  into a lowercase
    word = original.lower()
# storing a first character into variable  first
    first = word[0]
# putting together a complete Pig Latin conversation
    new_word = word[1:len(word)] + first + pyg
# print the converted word using new variable new_word
    print new_word
else:
    print 'empty'
