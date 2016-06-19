############################################
# Author: ilknur Gokcuoglu
# UCSC_Python_Course
# 11/24/2015
#######################################



import sys
import string


###############################################################################
# NAME: AskForFileName()
#
# DESCRIPTION: Ask the user for the name of the input file.
# PARAMETERS:
#   INPUT: file Name
#
#   OUTPUT: 
#
#   RETURN: File name
#       
#
# NOTES:
#   None
################################################################################

def AskforFileName():
	file_name = raw_input('Enter a file name:')
	
	return file_name
    
###############################################################################
# NAME: ReadFileContents()
#
# DESCRIPTION: Open the file and read all the lines in the file into the memory
#
# PARAMETERS:
#   INPUT: Filename
#
#   OUTPUT: all_file_contents
#
#   RETURN: all_file_contents
#       
#
# NOTES:
#   None
################################################################################

def ReadFileContents(file_name):
	with open(file_name) as f:
		all_file_contents = f.readlines()
		
	return all_file_contents 
 
###############################################################################
# NAME: BuildHeadList
#
# DESCRIPTION: Function that iterates through all_file_contents and create a list of lines before the first line which starts with "ATOM"
#
# PARAMETERS:
#   INPUT: Contents of the file
#
#   OUTPUT: List of lines before the lines which start with "ATOM"
#
#   RETURN: head_list
#       
#
# NOTES:
#   None
################################################################################

def BuildHeadList(all_file_contents):
	head_list = []
	for i,line in enumerate(all_file_contents):			
		if line.startswith("ATOM"):
			line_no =i
			break
			
	for j,line in enumerate(all_file_contents):
		if j < line_no:
			head_list.append(line)
	
	return head_list

 
###############################################################################
# NAME: BuildAtomList
#
# DESCRIPTION: Function that iterates through all_file_contents and create a list of lines which start with "ATOM"
#
# PARAMETERS:
#   INPUT: Contents of the file 
#
#   OUTPUT: List of lines which start with "ATOM"
#
#   RETURN: atom_list
#       
#
# NOTES:
#   None
################################################################################

def BuildAtomList(all_file_contents):
	atom_list = []
	for line in all_file_contents:
		if line.startswith("ATOM"):
			atom_list.append(line)
	
	return atom_list
	

 
###############################################################################
# NAME: BuildTailList
#
# DESCRIPTION: Create list of lines after the lines starting with "ATOM"
#
# PARAMETERS:
#   INPUT: Contents of the file
#
#   OUTPUT: List of lines after the lines starting with "ATOM"
#
#   RETURN: tail_list
#       
#
# NOTES:
#   None
################################################################################

def BuildTailList(all_file_contents):
	tail_list = []
	for i,line in enumerate(all_file_contents):			
		if line.startswith("ATOM"):
			line_no =i
	
	for j,line in enumerate(all_file_contents):
		if j > line_no:
			tail_list.append(line)
	
	return tail_list		


###############################################################################
# NAME: WriteNewFile
#
# DESCRIPTION: Function that writes head_list, atom_list, tail_list to new file output.tt	
#
# PARAMETERS:
#   INPUT: Lists head_list, atom_list, tail_list
#
#   OUTPUT: output.txt
#
#   RETURN: None
#       
#
# NOTES:
#   None
################################################################################

def WriteNewFile(head_list, atom_list, tail_list):
	f = open('output.txt','wb')
	for item in head_list:
		f.write("%s" %item)
	for item in atom_list:
		f.write("%s" %item)
	for item in tail_list:
		f.write("%s" %item)

	
###############################################################################
# Function calls - for testing this file by itself
################################################################################

#file_name = AskforFileName()
#all_file_contents = ReadFileContents(file_name)
#atom_list = BuildAtomList(all_file_contents)
#head_list = BuildHeadList(all_file_contents)
#tail_list = BuildTailList(all_file_contents)
#WriteNewFile(head_list, atom_list, tail_list)
