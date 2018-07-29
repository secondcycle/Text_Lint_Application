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
	import inspect
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

# parse input text files and return dict of lists with text lines
def a():
	
	retDict = {}
	
	#for 

	return retDict

# @ Error handling and print func
# callingFuncInfoTuple = (FileName, CallerFuncName, Line number)
def printErrorFunc(inputErrorString="", callingFuncInfoTuple=(), numOfElements=2):
	delimiterStr = "::"

	callingFuncInfoStr = str(callingFuncInfoTuple[0]) + delimiterStr + str(callingFuncInfoTuple[1]) + delimiterStr + str(callingFuncInfoTuple[2])

	stringToPrint = "\033[1;31;40m Error: {}   @   {} \n ".format(inputErrorString, callingFuncInfoStr)
	
	print(stringToPrint)
	
	return

# @ Generates input argument dict for compactness and readability
def generateInputArgumentDictFunc(inputKeyList=[], inputValueList=[], numOfElements=1):
	retDict  = {}
	funcName = sys._getframe().f_code.co_name

	numOfElementsInInputKeyList   = len(inputKeyList)
	numOfElementsInInputValueList = len(inputValueList)

	if(numOfElementsInInputValueList != numOfElements):
		print("Function : {}: has erroneous number of input values and numOfElements {} != {} \n".format(funcName, numOfElementsInInputValueList, numOfElements))
		sys.exit()

	elif(numOfElementsInInputKeyList != numOfElements):
		print("Function : {}: has erroneous number of input keys and numOfElements {} != {} \n".format(funcName, numOfElementsInInputKeyList, numOfElements))
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

if __name__=='__main__':
	
	print(" 1 ")
	
	testPrintErrorFunc()