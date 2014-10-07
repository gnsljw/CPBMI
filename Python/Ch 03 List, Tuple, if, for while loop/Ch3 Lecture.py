#!/usr/bin/env python

# List
## List Making, Indexing and Slicing
list_sample = []
list_sample = ["Chapter", 2, "List", "Tuple"]

print list_sample[0], list_sample[1]
print list_sample[1:3]
print list_sample * 2
print ["CPBMI", "Python"] + list_sample  # Concatenation
print len(list_sample)
"Chapter" in list_sample

list_sample[0] = "Lecture"
print list_sample

list_sample[1] = list_sample[1] + 1
print list_sample

list_sample[2:4] = ["Dictionary","Set"]
print list_sample
list_sample[2:2] = ["Files","Function"]
print list_sample

del list_sample[5]
print list_sample

del list_sample[1:3]
print list_sample

## Nested List
lecture_no = [1,2,3]
lecture_list = ["CPBMI", lecture_no, "Python"]
lecture_list
lecture_list[0]
lecture_list[1]
lecture_list[2]
lecture_list[1][0]
lecture_list[1][1]
lecture_list[1][2]

lecture_no [1] = 11
lecture_list

lecture_no = [4,5,6]
lecture_list
lecture_list = ["CPBMI", lecture_no, "Python"]
lecture_list

## List Methods
list_example = [10, 20, 30]
list_example.append(50)
list_example
list_example.insert(3, 40)
list_example
list_example.index(40)
list_example.count(20)
list_example.reverse()
list_example
list_example.sort()
list_example
list_example.extend([60,70])
list_example

sequence = "ATGC"
sequence_list = list(sequence)
sequence_list
sequence_list.reverse()
sequence_list

## Stack
stack_example = [10, 20, 30, 40, 50]
stack_example.append(60)
stack_example
stack_example.pop()
stack_example

## Queue
queue_example = [10, 20, 30, 40, 50]
queue_example.append(60)
queue_example
queue_example.pop(0)
queue_example

# If statement
score = 88
if score >= 90:
    print "A"
elif score < 90 and score >= 80 :
    print "B"
else:
    print "C"
    
n = -1
if n > 0 :
    print "Positive"
elif n < 0 :
    print "Negative"
else :
    print "Zero"

a = 8
if a > 5:
    if a == 8:
        print "a=8"
    else :
        print "a!=8"

# For loop
for x in [1,2,3] :
    print 2 * x

## Print String and String Length
list_example = ["CPBMI", "Python", "for loop"]
for s in list_example:
    print s, len(s)

## Numbering
i = 0
list_example = ["CPBMI", "Python", "for loop"]
for s in list_example:
    print i, s, len(s)
    i = i + 1

## Get Average
total = 0.0
scores = [77, 94, 30, 75, 32, 99]
for x in scores:
    total = total + x
print total / len(scores)
print sum(scores) / float (len(scores))

## Multiple for loop
for x in [2,3]:
    for y in [1,2]:
        print x, "*", y, "=", x*y
    print "*********"

## range()
for i in range (2, 10) :
    for j in range (1, 10) :
        print "%d * %d = %d" % (i, j, i*j)
    print

## Tips
for i in range(1,10):
    print i

for i in range(1,10):
    print i,

for i in range(1,3) :
    for j in range(1,3) :
        print i*j

for i in range(1,3):
    for j in range(1,3):
        print str(i) + "*" + str(j) + " = " + str(i*j)

for i in range(1,3):
    for j in range(1,3):
        print "%d * %d = %d" %(i, j, i*j),
    print

# While, Break
a = 1
while a < 5:
    print a
    a = a + 1

while True:
    which_one = raw_input ("What month (1-12)? Type 0 to exit. ")
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if (int(which_one) == 0) :
        break
    elif ( 1<= int(which_one) <= 12):
        print "The month is ", months[int(which_one) -1]
    else :
        print "Incorrect month range"

# List Comprehensions
list_example_pow = []
list_example = [1,2,3,4,5]
for i in list_example:
    list_example_pow.append(i ** 2)
list_example_pow

list_example_pow = [ i**2 for i in list_example ]
list_example_pow

list_example_pow = []
list_example = [1,2,3,4,5]
for i in list_example:
    if i > 3 :
        list_example_pow.append(i**2)

list_example_pow

list_example_pow = [ i**2 for i in list_example if i >3]
list_example_pow

# Case Control Example
case_control = "1,3,2,4,5,6,7,3,2,3"   # 1-5 : case, 6-10 : control
case_control_list = case_control.split(",")
sum(case_control_list [0:5])  # type error

case_control_list
type(case_control_list[0])  # type : str

case_sum = 0
for i in range (5):
    case_sum = case_sum + int(case_control_list[i])
case_sum

control_sum = 0
for i in range (5, len(case_control_list)):
    control_sum = control_sum + int(case_control_list[i])
control_sum

case_control = "1,3,2,4,5,6,7,3,2,3"
case_control_list = case_control.split(",")
sum([int(case_control_list[i]) for i in range(5)])
sum([int(case_control_list[i]) for i in range(5, len(case_control_list))])

# Tuple
print "id : %d name : %s" % ("1","Park")
args = (4,5)
calc(*args)
d = {'one':1, 'two':2}
d.items()
