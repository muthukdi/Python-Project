# This Python file uses the following encoding: utf-8

# TITLE: Word Frequency Counter + Sorter
# AUTHOR: Dilip Muthukrishnan
# DATE: January 23, 2012
# DESCRIPTION: This script attempts to scan a passage of text and record the frequencies of
# each word in the passage. Then, it sorts this data in descending order and displays it to
# standard output as well as writes it to a text file.

# This statement stores the following passage that has been given to me in a variable.
input = 'Speaking on the NBC News program Meet the Press on Sunday morning, Mr. Gingrich acknowledged those concerns and said he wore them as a badge of honor as he pushed forward toward the nomination. The establishment is right to be worried about a Gingrich nomination, he said. We are going to make the establishment very uncomfortable. We are going to demand real change in Washington. \
Some of Mr. Gingrichs former colleagues have warned — often anonymously — that he cannot be trusted to lead the party, or the country. Newts absolutely brilliant, an admirer who negotiated with him in Congress told The Daily News of New York on Saturday night. He has 100 ideas; 97 are real good, the other three will blow up the world. \
Mr. Gingrich said he was not surprised by that kind of reaction, but he dismissed it as the same kind of nervousness that some in the partys establishment exhibited when Ronald Reagan was first running for national office. Im happy to be in the tradition of Ronald Reagan as the outsider who scares the Republican establishment, Mr. Gingrich said. And frankly, after the mess they made of things, maybe they should be shaken up pretty badly.'

# This function removes all occurences of a given element from a given list.
def removeAll(list,element):
	while element in list:
		list.remove(element)
	return list

# This block of code removes all punctuation marks (,;.) from the passage.
charList = []
for x in input: charList.append(x)
removeAll(charList,',')
removeAll(charList,';')
removeAll(charList,'.')
input = ''.join(charList)

# This statement returns a list containing all the words in the passage.
rawList = input.split()

# This block of code converts all the words in the rawList to lowercase
# and then stores them in a new wordList.
wordList = []
for word in rawList: wordList.append(word.lower())
del rawList

# This loop attempts to populate a list with all the words and their
# respective frequencies. It stores this information as a sequence
# of ordered pairs (2-element lists). The removeAll() function then removes
# all occurences of each word once it has been processed.
frequencyList = []
while len(wordList) > 0:
	word = wordList[0]
	frequency = wordList.count(word)
	frequencyList.append([word,frequency])
	removeAll(wordList,word)

# These statements attempt to sort the data in descending order. Some
# effort is needed here, as can be seen. The procedure is as follows. The goal 
# is to build a complete sorted list. First, I begin with an empty sorted list.
# Next, I take the frequency list (which is in fact a list of ordered pairs)
# and loop through it to find the maximum frequency. I loop through the list
# again to pick out the items corresponding to this maximum value and add them
# to the sorted list. Then, I filter out the max values from the frequencyList
# and store them in a tempList.  Finally, I empty the frequencyList and copy
# the tempList items back into it for another run of the loop. The process ends
# when the sortedList has got the same length as the original frequencyList.
n = len(frequencyList)
sortedList = []
while len(sortedList) < n:
	max	= 0
	tempList = []
	for item in frequencyList:
		if item[1] > max:
			max = item[1]
	for item in frequencyList:
		if item[1] == max:
			sortedList.append(item)
	for item in frequencyList:
		if (item[1] < max):
			tempList.append(item)
	frequencyList = []
	for item in tempList:
		frequencyList.append(item)

# This statement prints the sorted data to standard output.
for item in sortedList: print item[0], "\t\t", str(item[1])

# These statements write the sorted data to a text file.
# CAUTION: The file Words.txt must already exist in your current working directory!
try: 
	f = open("Words.txt","r+")
	for item in sortedList: f.write(item[0] + "\t\t" + str(item[1]) + "\n")
	f.close()
except IOError:
	print '\nThe file Words.txt does not exist! Create it and run the script again.'
	
# *****END OF SCRIPT*****