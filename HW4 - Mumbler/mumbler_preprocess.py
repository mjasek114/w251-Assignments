#!/usr/bin/env python

import sys
import zipfile

def mumbler_preprocess (startFile, endFile):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for fileNum in range(startFile, endFile+1):
        fileName = "googlebooks-eng-all-2gram-20090715-" + str(fileNum) + ".csv"
        zipFileName = "googlebooks-eng-all-2gram-20090715-" + str(fileNum) + ".csv.zip"
    
        newFileName = "gfile" + str(fileNum) + ".csv"
        zipFile = zipfile.ZipFile(zipFileName)

        newNGram = True
        count = 0
        writeCount = 0
        with open(newFileName, 'w') as f:
            zipFile = zipfile.ZipFile(zipFileName)
            zf = zipFile.open(fileName, 'r')
            for zLine in zf.readlines():
                zLine = zLine.lower()
                wordLine = zLine.split()
                curWords1st = wordLine[0]
                 # if the 1st word starts with a letter
                if curWords1st[0] in alphabet:
                    curWords2nd = wordLine[1]
                    # if the 2nd word starts with a letter
                    if curWords2nd[0] in alphabet:
                        if newNGram == True:
                            curNGram1st = curWords1st
                            curNGram2nd = curWords2nd
                            curCount = int(wordLine[3])
                            newNGram = False
                        elif (curNGram1st == curWords1st) and (curNGram2nd == curWords2nd):
                            curCount += int(wordLine[3])
                        else:
                            #write it to the file
                            f.write(curNGram1st + '\t' + curNGram2nd + '\t' + str(curCount) + '\n')
                            writeCount += 1
                            curNGram1st = curWords1st
                            curNGram2nd = curWords2nd
                            curCount = int(wordLine[3])
                count += 1
            zf.close()
            f.write(curNGram1st + '\t' + curNGram2nd + '\t' + str(curCount) + '\n')
            writeCount += 1
            print "count= " + str(count)
            print "writeCount= " + str(writeCount)

#mumbler_preprocess(0, 0)
mumbler_preprocess(int(sys.argv[1]),int(sys.argv[2]))
