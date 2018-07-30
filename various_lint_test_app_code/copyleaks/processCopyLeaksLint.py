#####################################################################
# @Description:  Class with processing functions of CopyLeaks
# 
# @Version: 0.1 - 30/07/2018
#  
# @FileName: processCopyLeaksLint.py
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

# input is dict {Common format, text of entire file}
# Based on each of the lint framework, fragment input text file differently
# Contraints on text based copyleaks API ||| to Grammarly
# [min, max] number of characters per call of API with text as input
# comparison final report has word pointer related information 
# multiprocessing, safe to call within the multiprocessing function

