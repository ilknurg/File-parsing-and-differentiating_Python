
import sys
import string
import itertools
import homework_5_solution_module


###############################################################################
# NAME: Run()
#
# DESCRIPTION: Function that calls all functions from the homework_5_solution_module.py and DifferenceTwoFiles()
# PARAMETERS:
#   INPUT: None
#
#   OUTPUT: None
#
#   RETURN: None
#       
#
# NOTES:
#   None
################################################################################

def Run():
	file_name = homework_5_solution_module.AskforFileName()
	all_file_contents = homework_5_solution_module.ReadFileContents(file_name)
	atom_list = homework_5_solution_module.BuildAtomList(all_file_contents)
	head_list = homework_5_solution_module.BuildHeadList(all_file_contents)
	tail_list = homework_5_solution_module.BuildTailList(all_file_contents)
	homework_5_solution_module.WriteNewFile(head_list, atom_list, tail_list)
	file_2 = 'output.txt'
	diff_list = DifferenceTwoFiles(file_name, file_2)
	
    
###############################################################################
# NAME: DifferenceTwoFiles()
#
# DESCRIPTION: Difference between twor files
#
# PARAMETERS:
#   INPUT: Both the files
#
#   OUTPUT: print differences count
#
#   RETURN: diff_list
#       
#
# NOTES:
#   None
################################################################################

def DifferenceTwoFiles(file_1, file_2):
	file1 = open(file_1, 'r')
	file2 = open(file_2, 'r')
	diff_list = []
	diff_count = 0
	
	with open(file_1) as f1:
		with open(file_2) as f2:
			for i, (lineA, lineB) in enumerate(itertools.izip_longest(f1,f2)):
				if lineA != lineB:
					print lineB
					diff_list.append(lineA)
					diff_count += 1
	print diff_count
	return diff_list
		


 
###############################################################################
# Function calls
################################################################################

Run()