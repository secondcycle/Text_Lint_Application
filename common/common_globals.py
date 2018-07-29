#####################################################################
# @Description:  Application for linting text files
# 
# @Version: 0.1 - 29/07/2018
#  
# @FileName: common_globals.py
# 
# @Author : Nayan Singh Ravindra
#####################################################################

# global python version variable
gPYTHON_VERSION=3

tempVar = 0
try:
	import sys

	# import section
	import os

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

# rest of the globals