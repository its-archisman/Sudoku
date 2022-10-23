from typing import Tuple, List
# No other imports allowed

# PART OF THE DRIVER CODE

def input_sudoku() -> List[List[int]]:
	"""Function to take input a sudoku from stdin and return
	it as a list of lists.
	Each row of sudoku is one line.
	"""
	sudoku= list()
	for _ in range(9):
		row = list(map(int, input().rstrip(" ").split(" ")))
		sudoku.append(row)
	return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
	"""Helper function to print sudoku to stdout
	Each row of sudoku in one line.
	"""
	for i in range(9):
		for j in range(9):
			print(sudoku[i][j], end = " ")
		print()

# You have to implement the functions below

def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes a parameter position and returns
	the block number of the block which contains the position.
	"""
	i=pos[0]
	j=pos[1]
	if i in range(1,4):
		if j in range(1,4):
			return 1
		if j in range(4,7):
			return 2
		if j in range(7,10):
			return 3
	if i in range(4,7):
		if j in range(1,4):
			return 4
		if j in range(4,7):
			return 5
		if j in range(7,10):
			return 6
	if i in range(7,10):
		if j in range(1,4):
			return 7
		if j in range(4,7):
			return 8
		if j in range(7,10):
			return 9
	# your code goes here
	return 0

def get_block(sudoku:List[List[int]], x: int) -> List[int]:
	"""This function takes an integer argument x and then
	returns the x^th block of the Sudoku. Note that block indexing is
	from 1 to 9 and not 0-8.
	"""
	a=0
	b=0
	if x%3==1:
		b=1
	if x%3==2:
		b=4
	if x%3==0:
		b=7
	if x<4:
		a=1
	if x>3 and x<7:
		a=4
	if x>6:
		a=7
	list=[]

	list.append(sudoku[a-1][b-1])
	list.append(sudoku[a-1][b])
	list.append(sudoku[a-1][b+1])
	list.append(sudoku[a][b-1])
	list.append(sudoku[a][b])
	list.append(sudoku[a][b+1])
	list.append(sudoku[a+1][b-1])
	list.append(sudoku[a+1][b])
	list.append(sudoku[a+1][b+1])
	# your code goes here
	return list#()

def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes parameter position
	and returns the index of the position inside the corresponding block.
	"""
	a=0
	b=0
	n=get_block_num(sudoku,pos)
	if n==1 or n==2 or n==3:
		a=1
	if n==4 or n==5 or n==6:
		a=4
	if n==7 or n==8 or n==9:
		a=7
	if n==1 or n==4 or n==7:
		b=1
	if n==2 or n==5 or n==8:
		b=4
	if n==3 or n==6 or n==9:
		b=7
	a=pos[0]-a+1
	b=pos[1]-b+1
	return b+3*(a-1)
	# your code goes here
	return 0

def get_row(sudoku:List[List[int]], i: int)-> List[int]:
	"""This function takes an integer argument i and then returns
	the ith row. Row indexing have been shown above.
	"""
	list=sudoku[i-1]
	# your code goes here
	return list#()

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
	"""This function takes an integer argument i and then
	returns the ith column. Column indexing have been shown above.
	"""
	list=[]
	for i in range(0,9):
		list.append(sudoku[i][x-1])
	# your code goes here
	return list#()

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
	"""This function returns the first empty position in the Sudoku. 
	If there are more than 1 position which is empty then position with lesser
	row number should be returned. If two empty positions have same row number then the position
	with less column number is to be returned. If the sudoku is completely filled then return `(-1, -1)`.
	"""
	for i in range(0,9):
		for j in range(0,9):
			if sudoku[i][j]==0:
				return (i+1,j+1)
	# your code goes here
	return (-1,-1)

def valid_list(lst: List[int])-> bool:
	"""This function takes a lists as an input and returns true if the given list is valid. 
	The list will be a single block , single row or single column only. 
	A valid list is defined as a list in which all non empty elements doesn't have a repeating element.
	"""
	for i in range(1,10):
		if lst.count(i)>1 or (lst[i-1]>9 and lst[i-1]<0):
			return False
	# your code goes here
	return True

def valid_sudoku(sudoku:List[List[int]])-> bool:
	"""
	This function returns True if the whole Sudoku is valid.
	"""
	for i in range(1,10):
		if not(valid_list(get_row(sudoku,i))):
			return False
	for i in range(1,10):
		if not(valid_list(get_column(sudoku,i))):
			return False
	for i in range(1,10):
		if not(valid_list(get_block(sudoku,i))):
			return False
	# your code goes here
	return True

def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
	"""This function takes position as argument and returns a list of all the possible values that 
	can be assigned at that position so that the sudoku remains valid at that instant.
	"""
	a=pos[0]-1
	b=pos[1]-1
	list=[]
	c=sudoku[a][b]
	sudoku[a][b]=1
	if valid_sudoku(sudoku):
		list.append(1)
	sudoku[a][b]=2
	if valid_sudoku(sudoku):
		list.append(2)
	sudoku[a][b]=3
	if valid_sudoku(sudoku):
		list.append(3)
	sudoku[a][b]=4
	if valid_sudoku(sudoku):
		list.append(4)
	sudoku[a][b]=5
	if valid_sudoku(sudoku):
		list.append(5)
	sudoku[a][b]=6
	if valid_sudoku(sudoku):
		list.append(6)
	sudoku[a][b]=7
	if valid_sudoku(sudoku):
		list.append(7)
	sudoku[a][b]=8
	if valid_sudoku(sudoku):
		list.append(8)
	sudoku[a][b]=9
	if valid_sudoku(sudoku):
		list.append(9)
	sudoku[a][b]=c
	

	# your code goes here
	return list#()

def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
	"""This function fill `num` at position `pos` in the sudoku and then returns
	the modified sudoku.
	"""
	sudoku[pos[0]-1][pos[1]-1]=num
	# your code goes here
	return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
	"""This function fills `0` at position `pos` in the sudoku and then returns
	the modified sudoku. In other words, it undoes any move that you 
	did on position `pos` in the sudoku.
	"""
	sudoku[pos[0]-1][pos[1]-1]=0
	# your code goes here
	return sudoku

def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
	""" This is the main Sudoku solver. This function solves the given incomplete Sudoku and returns 
	true as well as the solved sudoku if the Sudoku can be solved i.e. after filling all the empty positions the Sudoku remains valid.
	It return them in a tuple i.e. `(True, solved_sudoku)`.

	However, if the sudoku cannot be solved, it returns False and the same sudoku that given to solve i.e. `(False, original_sudoku)`
	"""
	a=-1
	b=-1
	pos=find_first_unassigned_position(sudoku)
	if pos==(-1,-1) and valid_sudoku(sudoku):
		return (True,sudoku)
	else:
		a=pos[0]-1
		b=pos[1]-1
	for i in get_candidates(sudoku,find_first_unassigned_position(sudoku)):
		sudoku[a][b]=i
		if not valid_sudoku(sudoku):
			sudoku[a][b]=0
		else:
			if sudoku_solver(sudoku)[0]:
				return (True,sudoku)
			sudoku[a][b]=0
	return (False,sudoku)


# PLEASE NOTE:
# We would be importing your functions and checking the return values in the autograder.
# However, note that you must not print anything in the functions that you define above before you 
# submit your code since it may result in undefined behaviour of the autograder.

def in_lab_component(sudoku: List[List[int]]):
	print("Testcases for In Lab evaluation")
	print("Get Block Number:")
	print(get_block_num(sudoku,(4,4)))
	print(get_block_num(sudoku,(7,2)))
	print(get_block_num(sudoku,(2,6)))
	print("Get Block:")
	print(get_block(sudoku,3))
	print(get_block(sudoku,5))
	print(get_block(sudoku,9))
	print("Get Row:")
	print(get_row(sudoku,3))
	print(get_row(sudoku,5))
	print(get_row(sudoku,9))
#in_lab_component([[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]])

# Following is the driver code
# you can edit the following code to check your performance.
if __name__ == "__main__":
	
	# Input the sudoku from stdin
	sudoku = input_sudoku()
	# Try to solve the sudoku
	possible, sudoku = sudoku_solver(sudoku)

	# The following line is for the in-lab component
	in_lab_component(sudoku)
	# Show the result of the same to your TA to get your code evaulated
	
	# Check if it could be solved
	if possible:
		print("Found a valid solution for the given sudoku :)")
		print_sudoku(sudoku)

	else:
		print("The given sudoku cannot be solved :(")
		
		print_sudoku(sudoku)