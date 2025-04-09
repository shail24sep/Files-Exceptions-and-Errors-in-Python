# Files-Exceptions-and-Errors-in-Python

**Task 1: Read a File and Handle Errors **

myfile = 'sample.txt'
This defines a string variable named myfile that stores the name of the file which I want to read.

In this case, it's "sample.txt".
try:
This begins a try block, which is used to catch and handle exceptions (errors) that may occur during execution.

If any error occurs inside this block, the program will jump to the corresponding except block.


f = open(myfile, 'r')
Tries to open the file 'sample.txt' in read mode ('r').

If the file doesn't exist, this line will raise a FileNotFoundError.


Read_all = f.readlines()
Reads all lines from the file and stores them in a list called Read_all.

Each element of the list is one line (as a string) from the file.


f.close()
Closes the file after reading.

This is important to free up system resources.


i = 0
Initializes a counter variable i to keep track of line numbers.

print("Reading file content:")

Print the above message.

for x in Read_all:
Starts a for loop to iterate through each line x in the list Read_all.


i += 1
Increments the line number counter by 1 with each loop iteration.


print('line', i, ":", x)
Prints the line number and the content of the line.

Example output: line 1 : This is the first line.


except FileNotFoundError:
This block catches the FileNotFoundError, which happens if the file 'sample.txt' doesn't exist when trying to open it.


print('Error: The file', myfile, 'was not found.')
If the exception is caught, the above line print.

Expected Output is given below:

Reading file content:
line 1 : This is a sample text file.

line 2 : It contains multiple lines.



**Task 2: Write and Append Data to a File**

myfile = 'output.txt'
This defines a variable myfile and assigns it the string 'output.txt', which is the name of the file you're going to write to, append to, and read from.


myinput = input("Enter text to write in the file:")
Prompts the user to enter some text.

The entered text is stored in the variable myinput.


try:
Starts a try block to catch and handle any file-related errors (like permission denied, disk error, etc.).

If an error occurs anywhere inside this block, Python will jump to the except block at the bottom.


f = open(myfile, 'w')
Opens (or creates) the file named 'output.txt' in write mode ('w').

If the file already exists, it will be overwritten.


outputWrite = f.write(myinput)
Writes the user's input (myinput) to the file.

Returns the number of characters written, which is stored in outputWrite.


f.close()
Closes the file after writing. This is important to save the changes and release system resources.


if outputWrite > 0:
print("Data successfully written to", myfile, "\n")
Checks if something was actually written to the file (i.e., outputWrite is greater than 0).

If so, it prints a success message.


secondInput = input("Enter additional text to append:")
Prompts the user for more text to append to the file.

Stores that input in secondInput.


f = open(myfile, 'a')
Opens the file again, this time in append mode ('a'), so that new content will be added to the end without erasing the existing content.


secondOutputWrite = f.write('\n' + secondInput)
Appends a newline (\n) followed by the user's new input to the file.

Returns the number of characters written and stores it in secondOutputWrite.


f.close()
Closes the file again after appending.


if secondOutputWrite > 0:
print("Data successfully appended." + "\n")
Checks if something was appended.

If so, prints a success message.


f = open(myfile, 'r')
Opens the file in read mode to check its final contents.


reading_Text = f.read()
Reads the entire contents of the file into the variable reading_Text.


f.close()
Closes the file after reading.


print("Final content of", myfile)
print(reading_Text)
Displays the final contents of the file to the user.


except (IOError, OSError) as e:
print("An error occurred while handling the file:", e)
If any input/output error or OS-level error occurs in the try block, this block catches it.

It prints an error message along with the actual error (e) for debugging or user info.

Expected output:

Enter text to write in the file:Hello, Python!
Data successfully written to output.txt 

Enter additional text to append:Learning file handling in Python.
Data successfully appended.

Final content of output.txt
Hello, Python!
Learning file handling in Python.




