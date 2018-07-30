#####################################################################
# @Description: Convert supported input file formats to formats required by the linting framework
# Version 0.1 - 30/07/2018
#  
# @FileName: handleInputFileFormats.py
# 
# @Author : Nayan Singh Ravindra
#####################################################################

# Usual header for checking python version
tempVar = 0
try:
	import os
	import sys

	# import section
	sys.path.insert(0, os.path.join("",os.environ['WORKSPACE'], "Essentials_Linux/essential_scripts/plagiarism_checker/Text_Lint_Application/common/"))

	from common_globals   import gPYTHON_VERSION as gPYTHON_VERSION
	from common_functions import *

	import argparse
	import fitz
	
	from reportlab.platypus   import SimpleDocTemplate, Paragraph, Spacer
	from reportlab.lib.styles import getSampleStyleSheet
	from reportlab.lib.units  import inch

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

# class for converting between filetypes 
class convertBetweenFileTypesClass():
	
	def __init__(self, inputArgDict={}):
		self.inputFileNameKey    = "inputFileNameKey"
		self.inputFilePathKey    = "inputFilePathKey"
		self.outputFolderPathKey = "outputFolderPathKey"

	'''
	@ Error handling and print func
	callingFuncInfoTuple = (inputTextObj, outputFilePathAndName)
	'''
	def createPDFFromTextFileOBjFunc(self, inputTextObj, outputFilePathAndName): 
		styles       = getSampleStyleSheet()
		outputDoc    = SimpleDocTemplate(outputFilePathAndName)
		textInPDF    = [Spacer(1,0.5*inch)]
		style        = styles["Normal"]
		paraGraphObj = Paragraph(inputTextObj.decode("utf8"), style)
		textInPDF.append(paraGraphObj)
		outputDoc.build(textInPDF)
		return 

	'''
	@ Error handling and print func
	callingFuncInfoTuple = (FileName, CallerFuncName, Line number)
	'''
	def printErrorFunc(self, inputErrorString="", callingFuncInfoTuple=(), numOfElements=2):
		delimiterStr = "::"
		callingFuncInfoStr = str(callingFuncInfoTuple[0]) + delimiterStr + str(callingFuncInfoTuple[1]) + delimiterStr + str(callingFuncInfoTuple[2])
		stringToPrint = "\033[1;31;40m Error: {}   @   {} \n ".format(inputErrorString, callingFuncInfoStr)
		print(stringToPrint)
		exit(0)
		return

	'''
	Input : files [1,N] 
	Output: Dict with mimeType [1,N]
	'''
	def getFilesWithMimeTypeInInputFilesListFunc(self, inputList=[], mimeType=""):
		retList = []

		for index, filePath in enumerate(inputList):

			print(" filePath = {} ".format(filePath))

			# Error Handling
			if(not os.path.exists(filePath)):
				inputErrorString     = " File {} does not exists ".format(filePath)
				frame 				 = sys._getframe()
				callingFuncInfoTuple = (frame.f_code.co_filename, frame.f_code.co_name, frame.f_lineno)
				self.printErrorFunc(inputErrorString=inputErrorString, callingFuncInfoTuple=callingFuncInfoTuple, numOfElements=2)

			mimeType  		  = mimetypes.guess_type(filePath)[0]
			retDict[filePath] = mimeType
		return retDict

	'''
	Input: inputText, characterToBeMatched and return back respective locations
	Returns a list of position related to matching char
	'''
	def findCharPositionOfMatchingCharFunc(self, inputText="\n", charToBeMatched='\n'):
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
	def filtersNewLineTextFunc(self, inputTextList=[]):
		retTextList = []

		nextLineChar = '\n'

		for index, textData in enumerate(inputTextList):

			curPosList = self.findCharPositionOfMatchingCharFunc(inputText=textData, charToBeMatched=nextLineChar)

			for posIdx, curPos in enumerate(curPosList):
				
				curPos = (curPos <= 80) * (curPos) +  (curPos - int(np.floor(curPos/80) * 80))

				equivalentVacantSpace = [' ' for i in range(0, max(80, 80 - (curPos + len(textData) * (curPos > 0) ))) ]

				equivalentVacantSpace = "".join(equivalentVacantSpace)

				textData.replace(nextLineChar, equivalentVacantSpace)

			retTextList.append(textData)
		
		return retTextList

	'''
		Input: outputFilePathAndName, outputTextObject, mode for writing the text into file
	'''
	def writeOutputToAFile(self, outputFilePathAndName="", outputTextObj="", mode="w+"):

		with open(outputFilePathAndName, mode) as fp:
			fp.write(outputTextObj)

		return 

	'''
	   Input : filename
	   Output: temporary folder path
	'''
	def PDFFileTypeToTXT(self, inputArgDict={}):
		retDict = {}

		mimeTypePDF     = "application/pdf"
		outputExtension = ".txt" 

		print(" inputArgDict = {} ".format(inputArgDict))

		inputFilePath    = inputArgDict[self.inputFilePathKey]
		outputFolderPath = inputArgDict[self.outputFolderPathKey]

		inputFileName    = inputFilePath.rsplit('/')[::-1][0].split('.')[0]

		inputDocumentFObj = fitz.open(filePath)
		outputTextObj 	  = ""

		for eachPage in inputDocumentFObj:
			pageText 	   = eachPage.getText()
			outputTextObj += "".join(self.filtersNewLineTextFunc([pageText])[0])

		#print("\n pageText = {} ".format(outputTextObj))
		
		retDict[inputFileName] = outputTextObj

		outputFilePathAndName = os.path.join(outputFolderPath, inputFileName) + outputExtension

		self.writeOutputToAFile(outputFilePathAndName=outputFilePathAndName, outputTextObj=outputTextObj, mode="w+")

		return retDict

	'''
	   Input : filename
	   Output: output folder path
	'''
	def TXTFileTypeToPDF(self, inputArgDict={}):
		retDict = {}
		
		mimeTypePDF     = "text/plain"
		outputExtension = ".pdf"
		outputFileType  = "pdf"

		inputFilePath    = inputArgDict[self.inputFilePathKey]
		outputFolderPath = inputArgDict[self.outputFolderPathKey]

		outputFileName   = inputFilePath.rsplit('/')[::-1][0].split('.')[0]
		outputFilePathAndName = os.path.join(outputFolderPath, outputFileName) + outputExtension

		with open(inputFilePath, "rb") as textFileObj:
			inputTextObj = textFileObj.read()
			self.createPDFFromTextFileOBjFunc(inputTextObj, outputFilePathAndName)

		return

	#def typeAFileTypeToTypeB(self, ):


def getMimeTypeFromFileExtension(inputFileExtension="txt"):
	
	inputFileExtension = inputFileExtension.lower()

	tempFilePath  = "temp" + "." + inputFileExtension

	createFiles(inputFileNameList=[tempFilePath])

	mimeType      = mimetypes.guess_type(tempFilePath)[0]

	deleteFiles(inputFileNameList=[tempFilePath])

	return mimeType

# dummy test
if __name__=='__main__':

	print(" convert Between FileTypes ")

	baseString          = "FileTypeTo"
	inputFileTypeList   = ["PDF", "TXT"] # user inputs
	outputFileTypeList  = ["TXT", "PDF"]

	inputFileFolderPath = "/home/nayan/workSpace/Essentials_Linux/essential_scripts/plagiarism_checker/Text_Lint_Application/input/"
	outputFolderPath    = "/home/nayan/workSpace/Essentials_Linux/essential_scripts/plagiarism_checker/Text_Lint_Application/output/"

	for index, inputFileType in enumerate(inputFileTypeList):

		inputFileType = inputFileType.upper()
		
		typeOfConvertFuncStr = appendStringsInAListFunc(inputList=[ inputFileType, baseString, outputFileTypeList[index] ], delimiterStr="")

		#print(" typeOfConvertFuncStr = {} ".format(typeOfConvertFuncStr))

		mimeType = getMimeTypeFromFileExtension(inputFileExtension=inputFileType)

		for filePath, dummy in getFilesWithMimeTypeInInputFilesListFunc(inputList=[ os.path.join(inputFileFolderPath,fileName) for fileName in os.listdir(inputFileFolderPath)], inputMimeType=mimeType).items():

			inputKeyList   = [ "inputFilePathKey", "outputFolderPathKey" ]

			inputValueList = [ os.path.join( filePath, inputFileFolderPath, filePath), outputFolderPath]

			inputArgDict   = generateInputArgumentDictFunc(inputKeyList=inputKeyList, inputValueList=inputValueList, numOfElementsInList=len(inputValueList))

			retConvertedFileInfoDict = getattr(globals()['convertBetweenFileTypesClass'](), typeOfConvertFuncStr)(inputArgDict=inputArgDict)

			#print("retConvertedFileInfoDict = {} ".format(retConvertedFileInfoDict))
				
			#exit(0)