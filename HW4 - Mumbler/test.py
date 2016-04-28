def test_file(startFile, endFile):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    fileName = "google_financial_ngrams.txt"
    with open(fileName, 'r') as f:
        fileData = f.read()
        fileData = fileData.lower()
        lines = fileData.split('\n')
        numLines = len(lines)
        print "numlines= " + str(numLines)
    
    for i in range(numLines):
        if lines[i][0] in alphabet:
            abcStartIndex = i
            break        
    print "abc start line= " + str(abcStartIndex)
    print lines[abcStartIndex]
        
    newFileName = "gfile" + str(startFile) + ".csv"
    with open(newFileName, 'w') as f:
        newNGram = True
        for i in range(abcStartIndex, numLines):
            wordLine = lines[i].split()
            curWords1st = wordLine[0]
            # if the 1st word starts with a letter
            if curWords1st[0] in alphabet:
                curWords2nd = wordLine[1]
                # if the 2nd word starts with a letter
                if curWords2nd[0] in alphabet:
                    if newNGram == True:
                        curNGram1st = curWords1st
                        curNGram2nd = curWords2nd
                        print curNGram1st + ' ' + curNGram2nd
                        curCount = int(wordLine[3])
                        newNGram = False
                    elif (curNGram1st == curWords1st) and (curNGram2nd == curWords2nd):
                        print curNGram1st + ' ' + curNGram2nd
                        curCount += int(wordLine[3])
                    else:
                        #write it to the file
                        f.write(curNGram1st + '\t' + curNGram2nd + '\t' + str(curCount) + '\n')
                        curNGram1st = curWords1st
                        curNGram2nd = curWords2nd
                        curCount = int(wordLine[3])
        f.write(curNGram1st + '\t' + curNGram2nd + '\t' + str(curCount) + '\n')
 
test_file(0, 0)