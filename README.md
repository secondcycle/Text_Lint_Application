# Text_Lint_Application

This python based application provides it's users with a facility to identify and correct plagiarism, grammatical errors in text documents.

0. Set environmental variable
    a. WORKSPACE=/home/nayan/workSpace/

1. Usage : 
	Main application python file

	A. Usage : text_lint_python_app.py  --name_of_test_run "testRun0" --input_text_files_folder_path_file "inputTextFolderPathFile.txt" --cfg_text_files_path_file "cfg_file_options" --output_pdf_files_folder_path_file "outputTextFolderPathFile.txt" --report_pdf_folder_path "../Text_Lint_Application/final_reports/"

	B. Fields Description :
		  1. name_of_test_run              : "Valid_text_input_for_filename"

	      2. inputTextFolderPathFile.txt   : [1,N] absolute path to input folder containing input files {Supported file formats : txt and pdf only} {Code can be extended to support other formats}

          3. cfg_file_options              : [1,N] Mention types of check {Limited to CopyLeaks, Grammarly, ...} or "All"

          4. outputTextPathFile.txt        : [1,N] Absolute path to output folder {Supported file format : txt only}, Contains comparison text per file for checking the differences {Meld, Kdiff3, BeyondCompare, etc ....}.

          5. report_pdf_filename.pdf       : [1] Summarized report for each of the run with [1,N] input files for text linting. {Include current time in the report}

    C. Default values :
		  1. name_of_test_run              : "temp_test"

		  2. inputTextFolderPathFile.txt   : ../Text_Lint_Application/input/  {*.txt, *.pdf}
			
		  3. cfg_file_options              : All
	
		  4. outputTextPathFile.txt        : ../Text_Lint_Application/output/
				  
		  5. report_pdf_folder_path        : ../Text_Lint_Application/final_reports/

2. Requirements : 
   
   1. Python version '3'
   2. 	
	
3.  