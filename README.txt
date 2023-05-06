This program communicates through a 'message.txt' file. Once the 'message.txt'
file reads 'run' on the first line, the program reads array data from a 'data.txt'
file. Data should be written to the 'data.txt' file in the form:
	1 1
	2 2
	3 3
	etc.
where column 1 is the first array and column 2 is the second array. The program
expects exactly 10 elements for each array. Once the calculations are performed,
'message.txt' is cleared and a message is written to it. To perform another calculation,
clear the 'message.txt' file and write 'run' again. The program will run until killed.

The program is written for Python 3 and will require numpy, which can be installed with the 
command 'pip install numpy' in terminal.

A UML diagram is included.