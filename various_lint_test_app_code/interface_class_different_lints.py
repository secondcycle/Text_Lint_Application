#####################################################################
# @Description:  Inteface class for selecting between various possible supported lints
# 
# @Version: 0.1 - 29/07/2018
#  
# @FileName: inteface_class_different_lints.py
# 
# @Author : Nayan Singh Ravindra
#####################################################################

tempVar = 0
try:
	import sys

	# import section
	from common_globals   import gPYTHON_VERSION as gPYTHON_VERSION

	from common_functions import appendStringsInAList
	from common_functions import generateInputArgumentDictFunc
	from common_functions import checkInputArgumentsDictFunc

	# lint process imports
	from copyleaks.processCopyLeaksLint import copyleaksProcessClass
	from grammarly.processGrammarlyLint import grammarlyProcessClass

	# lint output report generation, specific to lint
	from copyleaks. import copyleaksReportClass
	from grammarly. import grammarlyReportClass
	
	import os
	from collections import OrderedDict
	
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


# class for type of lint 
class selectLintTypeClass():
	
	def __init__(self, inputArgDict={}):
		a = 1 

	def lintCOPYLEAKS(self, inputArgDict={}):
		# input : handle different input file formats

		# Can be used for a [single sentence, page]
		# process 

		# output summary report gen dict

	def lintGRAMMARLY(self, inputArgDict={}):
		# input : handle different input file formats

		# process

		# output summary report gen dict
		
	#def lintOther(self, ):



if __name__=='__main__':

	print(" interface class different lints ")

	selectLintTypeClassObj =  selectLintTypeClass()

	baseString    = "lint"
	testLintsList = ["copyleaks", "gRammarly"] # user inputs

	for lintType in enumerate(testLintsList):
		lintType = lintType.upper()
		
		typeOfLintStr = appendStringsInAList(inputList=[baseString, lintType], delimiterStr="")

		inputArgDict = generateInputArgumentDictFunc(inputKeyList=inputKeyList, inputValueList=inputValueList, numOfElementsInList=1)

		retReportSummaryInfoDict = getattr(selectLintTypeClass(), typeOfLintStr)(inputArgDict=inputArgDict)