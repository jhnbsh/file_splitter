# file_splitter v1.0 Help Fiile
# Description:
This program splits extremly large files (tested up to 150GB) into smaller ones by the specified number of lines. 
Reference: The program is a variation of an example by user "yurib" on Stack Overfow at https://stackoverflow.com/questions/8096614/split-large-files-using-python.

The below is in progress..

# Why is this program needed?:
This program is used to take extremly large files, that are large to process themselves, and split the file into much smaller segments that can be processed eaiser individually.  This process works well for raw data files, wordlists, or other file types where the contents can be seperated without impacting the larget data set.

# Disclaimer:
This program should only be used to test authentication systems for which you own or have been given permission to test.  Do not use this program to edit wordlists which you intend to use for committing a crime.

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
  Run wordlist_mod from a command prompt or terminal window with:
  
    python wordlist_mod.py inputfile.txt outputfile.txt
   
  During initial execution of the program a user will be prompted for two items: steps and timing delay.
  
  The steps value is how many items you wish to process at a time.  For example, process 10 items then wait, or process 10,000 items then wait.  The timing delay value is how long the program should wait between steps.  Depending on the speed of your computer and size of your wordlist you may need to experiment with providing a timing delay to prevent a system lockup caused by exhausting system resources.  For small wordlists (<1Gb) it is generally safe to leave the timing delay to 0.

# Latest Updates
* Added option to split strings between a specified character (ex: "/" or ".").

# Planned Updates:
* Python v3 support.
* Add status indicators for each action's progress.
* Implement additional hashing algorithms.
