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
# 
# @Usage  : text_lint_python_app.py text_lint_python_app.py  --name_of_test_run "testRun0" --input_text_files_path_file "inputTextPathFile.txt" --cfg_text_files_path_file "cfg_file_options" 
# 			--output_pdf_files_path_file "outputTextPathFile.txt" --report_pdf_folder_path "../Text_Lint_Application/final_reports/"   
# 
# 
# 
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



def 
	





# main 
if __name__=='__main__':

	print(" In main \n ")


