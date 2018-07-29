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
	import os

	sys.path.insert(0, os.path.join("",os.environ['WORKSPACE'], "Essentials_Linux/essential_scripts/plagiarism_checker/Text_Lint_Application/common/"))

	# import section
	from common_globals   import gPYTHON_VERSION as gPYTHON_VERSION
	from common_functions import printErrorFunc as printErrorFunc
	
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

		print(" sys.path :: {}".format(sys.path))

		sys.exit()

def testPrintErrorFunc():
	inputErrorString   = "123213213"
	frame = sys._getframe()
	callingFuncInfoTuple = (frame.f_code.co_filename, frame.f_code.co_name, frame.f_lineno)
	printErrorFunc(inputErrorString=inputErrorString, callingFuncInfoTuple=callingFuncInfoTuple, numOfElements=2)
	return

if __name__=='__main__':
	
	testPrintErrorFunc()