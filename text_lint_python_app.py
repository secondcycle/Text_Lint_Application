#####################################################################
# Application for linting text files
# Version 0.1 - 29/07/2018
#  
# @FileName: text_lint_python_app.py
# 
# @Author : Nayan Singh Ravindra
#  
# @Inputs : 
# 
# 
# @Outputs: 
# 
#
# @Usage  : text_lint_python_app.py  --name_of_test_run "testRun0" --input_text_files_folder_path_file "inputTextFolderPathFile.txt" 
#                                    --cfg_text_files_path_file "cfgFileOptions" --output_pdf_files_folder_path_file "outputTextFolderPathFile.txt" 
#                                    --report_pdf_folder_path "../Text_Lint_Application/final_reports/"
#####################################################################

# Usual header for checking python version
tempVar = 0
try:
	import os
	import sys

	# import section
	from common.common_globals import gPYTHON_VERSION as gPYTHON_VERSION
	import argparse

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


# returns input argument dict
def parseAndGetInputArgumentsDict():

	parser = argparse.ArgumentParser(description='Process input arguments ')

	parser.add_argument('--name_of_test_run', metavar='N', type=str, nargs='+', 			      default="testRun0", help='name of the test run')

	parser.add_argument('--input_text_files_folder_path_file', metavar='N', type=str, nargs='+',  default="../Text_Lint_Application/input/inputTextFolderPathFile.txt", help='input_text_files_path_file')

	parser.add_argument('--cfg_text_files_path_file', metavar='N', type=str, nargs='+', 	      default="All", help='cfgFileOptions')
	
	parser.add_argument('--output_pdf_files_folder_path_file', metavar='N', type=str, nargs='+',  default="../Text_Lint_Application/output/outputTextFolderPathFile.txt", help='output_pdf_files_folder_path_file')

	parser.add_argument('--report_pdf_folder_path', metavar='N', type=str, nargs='+', 		      default="../Text_Lint_Application/final_reports/", help='report_pdf_folder_path')		

	argsDict = vars(parser.parse_args())

	return argsDict


# main 
if __name__=='__main__':

	print(" In main \n ")

	inputArgumentDict = parseAndGetInputArgumentsDict()

	print(" Input argument dict = {} ".format(inputArgumentDict))