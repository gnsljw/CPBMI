#!/usr/bin/env python

# Indexing and Slicing
string_test = "CPBMI Python"
string_test[0]
string_test[5]
string_test[8]
string_test[-1]
string_test[-3]
string_test[-4]
string_test[100]

string_test[1:4]
string_test[6:]
string_test[:]
string_test[:-1]
string_test[0:5]
string_test[5:12]
string_test[-100:100]

# Concatenation, Repeat, Membership Test, Length
string_concat = "CPBMI" + " " + "Python"
string_concat

string_repeat = "Python"
string_repeat * 3

string_repeat + string_repeat + string_repeat

string_test = "CPBMI Python"
"Python" in string_test
"python" in string_test

len(string_test)

# Define String
string1 = "Python is simple"
string1 = 'Python is simple'
string2 = "Python is great"
string3 = "It's extraordinary"
string4 = 'It\'s extraordinary'
string4 = 'It's extraordinary'

long_string = "File parsing is the computational method \ of reading a file, piece by piece. \n The size of the pieces can be ..."
pring long_string

long_string = """Python's standard documentation is substantial; download your own copy or browse it online !
See also the complete list of documentation by Python version.
If you're not sure where to go, try the help page."""
print long_string

# String is Immutable. Only List and Dictionary datatype can be mutable.
string1 = "CPBMI Python"
string1[0]
string1[0] = "A"

# String Formating
text = "Python"
"Hello %s" % text

"The number of students : %d" %36

"Hello %s. The number of students are %d" %("CPBMI Python Course", 36)

"t = %f , df = %f , p-value = %e" % (-3.4325, 8.791, 0.007745)

"t = %.3f , df = %.3f , p-value = %.3e" %(-3.4325, 8.791, 0.00745)

"%d" %2
"%5d" %2
"%-5d" %2
"%05d" %2
"%.2e" %1200
"%.3f" %1246.89768

# String Method
text = "i like python"
text.upper()
text = "I like python"
text.swapcase()
text.capitalize()
text.title()

text = "I like python. I like Programming"
text.count("like")
text.find("python")
text.startswith("I like")
text.endswith("swimming")

text = "CPBMI Python Programming"
text.strip()
text.rstrip()
text.lstrip()
text.replace("Python","JAVA")
text.replace(" ", "")

text.split()
text.split("Python")
t = text.split()
t
":".join(t)
print "\n".join(t)

lines = """first line
second line
third line"""
lines.splitlines()

# Type Casting
a = "1"
type(a)
a = int(a)
type(a)

a = 1
b = 2
c = 5
(a + b)/c
float (a + b) / c

a = 1
b = 2
print "a + b = " + a + b
print "a + b = " + str(a + b)
