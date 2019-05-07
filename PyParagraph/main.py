import re
import os
docpath = input("Which file would you like to read?  Choose 1 or 2 ")
doc = os.path.join(".", "Resources", "paragraph_" + str(docpath) + ".txt")
print("You choose: " + doc)

# Read CSV file as a series of lists

with open(doc, "r", newline='') as f:

#f = open(doc, "r")
    raw = f.read()

#remove all carriage returns, apostrophes, and quotes
text = raw.replace("\r", "")
text = text.replace("\n", "")
text = text.replace("'", "")
text = text.replace('"', ' ')

# count the remaining end of sent. punctuation
sentcount = text.count(".") +text.count("?")+text.count("!")

#remove remaining punctuation
text = text.replace(".", " ")
text = text.replace("?", " ")
text = text.replace("!", " ")
text = text.replace(",", "")
text = text.replace("-", " ")
text = text.replace("  ", " ")
text = text.replace("(", "")
text = text.replace(")", "")

#create a list of words split on the spaces
wordsplit = re.split(" ", text)

#count how many elements in the list of words for extra element at end of word list
wordcount = len(wordsplit) - 1 

#calculate the average sentence length
avsent = round(wordcount/sentcount, 1)

#create a running total of the number of letters in each element
totalword = 0
for word in wordsplit:
    runword = len(word)
    totalword = runword + totalword

#calculate the average length of the words
avword = round(totalword / wordcount, 2)

#print the desired output
print("\n")
print("Approximate Word Count: " + str(wordcount))
print("Approximate Sentence Count: " + str(sentcount))
print("Average Letter Count: "+ str(avword))
print("Average Sentence Length: "+ str(avsent))

#create path to output folder
output_path = os.path.join(".", "output", "paragraph_" + docpath + "_output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w", newline="") as results:
    #Linux/Unix line endings
    results.writelines("\n")
    results.writelines("Approximate Word Count: " + str(wordcount))
    results.writelines("Approximate Sentence Count: " + str(sentcount))
    results.writelines("Average Letter Count: "+ str(avword))
    results.writelines("Average Sentence Length: "+ str(avsent))



