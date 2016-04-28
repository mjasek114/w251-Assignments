import zipfile

def mumbler_preprocess (startFile, endFile):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for fileNum in range(startFile, endFile+1):
        fileName = "googlebooks-eng-all-2gram-20090715-" + str(fileNum) + ".csv"
        zipFileName = "googlebooks-eng-all-2gram-20090715-" + str(fileNum) + ".csv.zip"
    
        zipFile = zipfile.ZipFile(zipFileName)
        fileData = zipFile.read(fileName)
        zipFile.close()
        fileData = fileData.lower()
        lines = fileData.split('\n')
        numLines = len(lines)-1
        print "numlines= " + str(numLines)

        #find the first alphabetical character
        for i in range(numLines):
            if lines[i][0] in alphabet:
                abcStartIndex = i
                break        
        print "abc start line= " + str(abcStartIndex)
        print lines[abcStartIndex]
                
        newFileName = "gfile" + str(fileNum) + ".csv"
        with open(newFileName, 'w') as f:
            newNGram = True
            count = 0
            writeCount = 0
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
                            #print curNGram1st + ' ' + curNGram2nd
                            curCount = int(wordLine[3])
                            newNGram = False
                        elif (curNGram1st == curWords1st) and (curNGram2nd == curWords2nd):
                            #print curNGram1st + ' ' + curNGram2nd
                            curCount += int(wordLine[3])
                        else:
                            #write it to the file
                            f.write(curNGram1st + '\t' + curNGram2nd + '\t' + str(curCount) + '\n')
                            writeCount += 1
                            curNGram1st = curWords1st
                            curNGram2nd = curWords2nd
                            curCount = int(wordLine[3])
                count += 1
            f.write(curNGram1st + '\t' + curNGram2nd + '\t' + str(curCount) + '\n')
            writeCount += 1
            print "count= " + str(count)
            print "writeCount= " + str(writeCount)
                
#mumbler_preprocess(0,1)
