#!/usr/bin/env python

# Clear, Easy Syntax
print "Hello World"

for i in range(1,10):
    print 2 * i

# High Level Data Type Decision
def add(a,b):
    return a+b

print add(1,2)
print add("CPB","MI")
print add([1,2,3],[4,5,6])
    
# Simple Calculation
2 + 4
(4 + 6) * 2
11/3
11/3.
11%3
divmod(1,3)
a,b = divmod(11,3)
a
b
3.4e4
3.4e-4
2 ** 3

# Expansion with Other Language
## Expansion with R
import rpy
x = [5.05, 6.75, 3.21, 2.66]
y = [1.65, 26.5, -5.93, 7.96]
z = [1.65, 2.64, 2.64, 6.95]
print rpy.r.cor(x,y, method="spearman")
print rpy.r.cor(x,z, method="spearman")

## Expansion with MySQL
import MySQLdb
db=MySQLdb.connect(host="localhost", user="python-test", passwd="python", db="python-test")
cursor=db,cursor()
stmt="SELECT * from books"
cursor.execute(stmt)
rows=cursor.fetchall()
for row in rows:
    print "Row:"
    for col in row:
        print "Column %s" % (col)
    print "End of Row"
print "Number of rows returned: %d" % cursor.rowcount
cursor.close()
db.close()

# Library
## Biopython
from Bio import Entrez
from Bio import Medline
Entrez.email = 'A.N.Other@example.com'
handle = Entrez.esearch(db="pubmed", term="Type 2 Diabetes Korean", retmax=3)
record = Entrez.read(handle)
idlist = record["IdList"]

handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
records = Medline.parse(handle)

for record in records:
    print "PutMed ID: ", record.get("PMID","?")
    print "TITLE: ", record.get("TI","?")
    print "ABSTRACT: ", record.get("AB","?")

# Indentation
a = 1
 a = 1 # Error

# Syntax Error vs Logical Error
## Syntax Error
prin "Hello Python"

## Logical Error
result = "
grade = 95
if grade >= 90:
    result = "F"
print result

# Variable
## Variable Declaration
@email = "gnsljw@gmail.com"
email = "gnsljw@gmail.com"
Email = "test@test.com"
Email
email

## Reserved Words
import keyword
keyword.kwlist

## Built in Functions : http://docs.python.org/2/library/functions.html
divmod
divmod(10,3)
divmod = "Division and Modules"
divmod(10,3) # Error

## Good vs Bad Variable Name
a = 160.4
aa = 71.1
print a, aa

height = 160.4
weight = 71.1
print height, weight

x = 90
xx = 77
xxx = 93
y = x + xx + xxx
y/3.

english  = 90
math = 77
computer = 93
total = english + math + computer
total / 3.

## Annotation on Code
# The Score of English
english = 90
# The Score of Math
math = 77
# The Score of Computer
computer = 93
# The Total Score of English, Math, and Computer
total = english + math + computer
# Average Score
total / 3.

# Data Type : Number, String, List, Dictionary, Tuple, File
variable = 1
type(variable)
variable = 3.141592
type(variable)
variable = "CPBMI"
type(variable)
variable = ["CPBMI","Python"]
type(variable)
variable = {"CPBMI":1, "Python":2}
type(variable)
variable = ("CPBMI","Python")
type(variable)
fp = open("D://Work/CPBMI/hello.py")
type(fp)

## Numeric : int, float, long, complex
import sys
sys.maxint
2**63 -1

a = 4.5
b = 3.5e3
c = -0.3e-4
print a, b, c

import sys
sys.float_info.max

c = 5+8j
d = 2-6j
c + d
c.real
c.imag
c.conjugate()

# Math module
import math
math.sqrt(16)
math.exp(3)
math.log(10)
math.log10(10)
math.pi
math.e
math.fabs(-11.5)
round(3.54)

# Numeric Operator
4 + 6
4 + 6.0
6 / 4.0
6 . 4

## Order of Priority
3*-2
2 + 3*4
(2 + 3) *4
4 / 2 * 2
4 / (2 * 2)
2 ** 3 ** 4
(2 ** 3) ** 4

# Relational Operator
8 == 9
8 != 9
3 > 6
5 <= 6
a = 2
b = 3
a > b
0 < a < b

# Logical Operator
a = 10
b = 20
a > 10 and b < 50
a >= 10 and b < 50
a > 6 or b < 0
a > 20 or b < 10
(a > 20 or b < 50) and a > 100
not 1
not 0



