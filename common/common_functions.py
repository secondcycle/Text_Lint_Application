#####################################################################
# @Description:  Common functions for python coding
# 
# @Version: 0.1 - 29/07/2018
#  
# @FileName: common_functions.py
# 
# @Author : Nayan Singh Ravindra
#####################################################################

tempVar = 0
try:
	import sys

	# import section
	from common_globals import gPYTHON_VERSION as gPYTHON_VERSION

	import os
	import numpy as np
	from collections import OrderedDict
	import mimetypes

	# check python version
	if(gPYTHON_VERSION != sys.version_info.major):
		tempVar = 1
		a = 1/0
except:

	if(1 == tempVar):
		print("{}:{} : Mismatch in version of Python :: Current Python Version !=  Required Python Version :: {} != {} \n ".format( os.path.basename(__file__), sys._getframe().f_lineno, sys.version[0], '3'))
	else:
		print("{}:{} : Caught error with info : {} \n".format( os.path.basename(__file__), sys._getframe().f_lineno, sys.exc_info()))
		sys.exit()


'''
	Input: inputText, characterToBeMatched and return back respective locations
	Returns a list of position related to matching char
'''
def findCharPositionOfMatchingCharFunc(inputText="\n", charToBeMatched='\n'):
	retList = []

	newCurPos = inputText.find(charToBeMatched)
	inputText = inputText[newCurPos + 1 : ] 
	curPos    = newCurPos

	while(newCurPos != -1):
		retList.append(curPos)

		newCurPos = inputText.find(charToBeMatched)

		curPos   += (newCurPos + 1)   
		
		inputText = inputText[(newCurPos+1):] 
		
	return retList

'''
	Input: [1,N] input text obj list
	Replaces 'new line' char with equivalent white spaces
'''
def filtersNewLineTextFunc(inputTextList=[]):
		retTextList = []

		nextLineChar = '\n'

		for index, textData in enumerate(inputTextList):
			
			curPosList = findCharPositionOfMatchingCharFunc(inputText=textData, charToBeMatched=nextLineChar)

			for posIdx, curPos in enumerate(curPosList):
				
				curPos = (curPos <= 80) * (curPos) +  (curPos - int(np.floor(curPos/80) * 80))

				equivalentVacantSpace = [' ' for i in range(0, max(80, 80 - (curPos + len(textData) * (curPos > 0) ))) ]

				equivalentVacantSpace = "".join(equivalentVacantSpace)

				textData.replace(nextLineChar, equivalentVacantSpace)

			retTextList.append(textData)

		return retTextList

'''
	Parse input text files and return dict of lists with text lines
	[1::1]
'''
def parseInputTextFileAndRetListFunc(inputTextFile=""):
	retList = []
	
	with open(inputTextFile) as fp:
		for line in fp:
			retList.append(line)
			
	return retList

'''
 @ Error handling and print func
 callingFuncInfoTuple = (FileName, CallerFuncName, Line number)
'''
def printErrorFunc(inputErrorString="", callingFuncInfoTuple=(), numOfElements=2):
	delimiterStr = "::"

	callingFuncInfoStr = str(callingFuncInfoTuple[0]) + delimiterStr + str(callingFuncInfoTuple[1]) + delimiterStr + str(callingFuncInfoTuple[2])

	stringToPrint = "\033[1;31;40m Error: {}   @   {} \n ".format(inputErrorString, callingFuncInfoStr)
	
	print(stringToPrint)

	exit(0)

	return

# @ Generates input argument dict for compactness and readability
def generateInputArgumentDictFunc(inputKeyList=[], inputValueList=[], numOfElementsInList=1):
	retDict  = {}
	funcName = sys._getframe().f_code.co_name

	numOfElementsInInputKeyList   = len(inputKeyList)
	numOfElementsInInputValueList = len(inputValueList)

	if(numOfElementsInInputValueList != numOfElementsInList):
		print("Function : {}: has erroneous number of input values and numOfElements {} != {} \n".format(funcName, numOfElementsInInputValueList, numOfElementsInList))
		sys.exit()

	elif(numOfElementsInInputKeyList != numOfElementsInList):
		print("Function : {}: has erroneous number of input keys and numOfElements {} != {} \n".format(funcName, numOfElementsInInputKeyList, numOfElementsInList))
		sys.exit()

	elif(numOfElementsInInputValueList != numOfElementsInInputKeyList):	
		print("Function : {}: has erroneous number of input keys and values {} != {} \n".format(funcName, numOfElementsInInputKeyList, numOfElementsInInputValueList))
		sys.exit()

	else:
		
		for keyNum, inputKey in enumerate(inputKeyList):
			retDict[inputKey] = inputValueList[keyNum]

	return retDict
	
# @ check input arguments in the dictionary{Not nested dictionary} and returns each updated input element in the output list
def checkInputArgumentsDictFunc(inputDict={}, callingFuncName="", numOfElements=1):

	numOfActualElements = len(inputDict)

	if(numOfActualElements != numOfElements):
		print("Function : {}: has erroneous number of function arguments {} != {} \n".format(callingFuncName, numOfActualElements, numOfElements))
		sys.exit()
	
	return  

# Input : [1,N] strings, delimiterStr
# Output: an appended string with delimiterStr
def appendStringsInAListFunc(inputList=[], delimiterStr=""):

	numOfElements = len(inputList)

	if(0 == numOfElements):
		inputErrorString     = " Number of elements in input list is Zero "
		frame 				 = sys._getframe()
		callingFuncInfoTuple = (frame.f_code.co_filename, frame.f_code.co_name, frame.f_lineno)
		printErrorFunc(inputErrorString=inputErrorString, callingFuncInfoTuple=callingFuncInfoTuple, numOfElements=2)

	retString = ""

	for index, listElement in enumerate(inputList[:-1]):
		retString += str(listElement) + delimiterStr

	retString += str(inputList[numOfElements-1])

	return retString

'''
Input : files [1,N] 
Output: Dict with mimeType [1,N]
'''
def getFilesWithMimeTypeInInputFilesListFunc(inputList=[], inputMimeType=""):
	retDict = {}

	for index, filePath in enumerate(inputList):
		mimeType  		  = mimetypes.guess_type(filePath)[0]
		if(inputMimeType == mimeType):
			retDict[filePath] = mimeType

	return retDict

'''
Input : files [1,N] 
Output: Dict with mimeType [1,N]
'''
def	createFiles(inputFileNameList=[]):

	for numOfCreatedFiles, fileName in enumerate(inputFileNameList):
		if(not os.path.exists(fileName)):
			os.mknod(fileName)

	numOfCreatedFiles += 1
	retFlag = (numOfCreatedFiles == len(inputFileNameList))
	return retFlag

'''
Input : files [1,N] 
Output: Dict with mimeType [1,N]
'''		
def	deleteFiles(inputFileNameList=[]):

	for numOfDeletedFiles, fileName in enumerate(inputFileNameList):
		if(os.path.exists(fileName)):
			os.remove(fileName)

	numOfDeletedFiles += 1 
	retFlag = (numOfDeletedFiles == len(inputFileNameList))
	return retFlag 


if __name__=='__main__':
	
	print(" 1 ")
	
	inputTextFile = "/home/nayan/workSpace/Essentials_Linux/essential_scripts/plagiarism_checker/Text_Lint_Application/cfg_files/cfgFileOptions.txt"
	
	#retList = parseInputTextFileAndRetListFunc(inputTextFile)
	
	#print("retList = {} ".format(retList))

	text = "ab\naaaaaaca\nn"

	retList = findCharPositionOfMatchingCharFunc(inputText=text, charToBeMatched='\n')

	print(" retList = {} ".format(retList))

	retList = filtersNewLineTextFunc(inputTextList=[text])

	print(" text = {} ".format(retList[0]))