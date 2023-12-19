# file_splitter v1.0 Help Fiile
# Description:
This program splits extremly large files (tested up to 150GB) into smaller ones by the specified number of lines. 
Reference: The program is a variation of an example by user "yurib" on Stack Overfow at https://stackoverflow.com/questions/8096614/split-large-files-using-python.

# Why is this program needed?:
This program is used to take extremly large files, that are large to process themselves, and split the file into much smaller segments that can be processed eaiser individually.  This process works well for raw data files, wordlists, or other file types where the contents can be seperated without impacting the larget data set.

# Prerequisites:
   Python v2 is needed to execute the program.  The following provides basic directions
   on installing Python on your respective operating system.

   Windows users: As of Windows 8.1 you will need to install Python v2.
   1. Download and install python from https://www.python.org/downloads/ . Note: Choose any version of Python that starts with "2", not "3".
   1. Select all default settings, except for on the 'Customize Python'
   screen click "Add python.exe to Path" and choose "Will be installed to local hard-drive".

   MacOS users:  None, both python and the necessary libraries should be natively installed.
		
   Linux users:  None, both python and the necessary libraries should be natively installed.

# Execution instructions  
  Run file_splitter from a command prompt or terminal window with:
  
    python file_splitter.py inputfile.txt number-of-lines-to-split-by

# Latest Updates
* Initial version.
