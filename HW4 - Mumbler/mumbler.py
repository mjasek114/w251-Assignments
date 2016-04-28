import sys
#from numpy.random import choice
import numpy as np
import zipfile

def mumbler_app (word, max_words):
    word = word.lower()
    max = 1000000

    # Base case
    if max_words == "0":
        print "Maximum number of words has been reached."
        return
    else:
        print "Next word is: " + word
        fileName = "googlebooks-eng-all-2gram-20090715-0.csv"
        zipFileName = "googlebooks-eng-all-2gram-20090715-0.csv.zip"
        zipFile = zipfile.ZipFile(zipFileName)
        fileData = zipFile.read(fileName)
        #print type(fileData)
        #print fileData[:10000]
        lines = fileData.split('\n')
        for i in range(10):
            print lines[i]
            print type(lines[i])
        return

        # initialize variables
        uniqueNGrams = {}
        currentNGram = ""

        # open file and look for word
        with open(fileName, 'r') as f:
            count = 0
            for line in f:
                # store the first word of the line
                line = line.lower()
                #print line
                words = line.split()
                #print words
                curWord = words[0]
                #print curWord
                if curWord == word:
                    #print words[3]
                    curCount = int(words[3])
                    if words[1] == currentNGram:
                        #add counts
                        uniqueNGrams[currentNGram] += curCount
                    else:
                        currentNGram = words[1]
                        uniqueNGrams[currentNGram] = curCount
                else:
                    # check about alphabetically, if past order then break and return
                    pass
                count += 1
#                if count > max:
#                    return("")
    
        #print uniqueNGrams
    
        if uniqueNGrams != {}:
            listNGrams = []
            listProbs = []
            probSum = 0.0
            numSum = 0.0
            for ng in uniqueNGrams:
                numSum += uniqueNGrams[ng]
            for ng in uniqueNGrams:
                prob = uniqueNGrams[ng]/numSum
                probSum += prob
                listNGrams.append(ng)
                listProbs.append(prob)

            #print listNGrams
            #print listProbs
            print probSum
            print numSum
            #select new word
#            nextWord = ""
#            nextWord = choice(listNGrams, 1, p=listProbs)[0]
            nextWord = np.random.choice(listNGrams, 1, p=listProbs)[0]
            mumbler_app (nextWord, str(int(max_words)-1))
        else:
            print "There are no 2-grams that start with that word."
            return


if len(sys.argv) == 1:
    print "Please enter a starting word and maximum number of words"
elif len(sys.argv) == 2:
    print "Setting maximum number of words to 10"
    word = sys.argv[1]
    max_words = 10
    mumbler_app(word, max_words)
elif len(sys.argv) == 3:
    word = sys.argv[1]
    max_words = sys.argv[2]
    mumbler_app(word, max_words)

mumbler_app("financial", "2")
#print mumbler_app("financial", "google_financial_ngrams.txt")
#print mumbler_app("Goals", "googlebooks-eng-all-2gram-20090715-0.csv")
#print mumbler_app("To", "googlebooks-eng-all-2gram-20090715-0.csv")
#print mumbler_app("To", "googlebooks-eng-all-2gram-20090715-1.csv")
#print mumbler_app("To", "googlebooks-eng-all-2gram-20090715-90.csv")
#print mumbler_app("financial", "googlebooks-eng-all-2gram-20090715-0.csv")
#print mumbler_app("financial", "googlebooks-eng-all-2gram-20090715-1.csv")
#print mumbler_app("financial", "googlebooks-eng-all-2gram-20090715-90.csv")
