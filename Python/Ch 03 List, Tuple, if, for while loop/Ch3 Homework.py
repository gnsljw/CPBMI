# Q1.

patient_room = []

patient_room.append('John')
patient_room.append('Taylor')
patient_room.append('Smith')
patient_room.pop(0)
patient_room.append('Anderson')
patient_room.remove('Smith')


# Q2.

while 1: 
	height = raw_input("Input Height(cm) (input 0 to exit):") 
	if height == "0": 
		break

	weight = raw_input("Input Weight(kg) (input 0 to exit):")
	if weight == "0": 
		break 

	height = float(height) 
	weight = float(weight) 
	bmi = weight / ( (height/100)**2 )

	if bmi < 18.5: 
		result = "Underweight" 
	elif 18.5 <= bmi < 25: 
		result = "Normal weight" 
	elif 25 <= bmi < 30: 
		result = "Overweight" 
	elif bmi >= 30: 
		result = "Obesity" 

	print "BMI= %.2f %s" % (bmi, result)

# Q3.

for height in range(170,175):
        print "%d cm" % height,
        for weight in range(60,65):
                bmi = weight / ( (float(height) / 100)**2 )
                print "%.1f(%d kg)" % (bmi, weight),
        print

# Q4.

sequence = 'TGTAATC'
rev_strand = []

sequence_list = list(sequence)
sequence_list.reverse()

for x in sequence_list:
    if x == 'A':
        rev_strand.append('T')
    elif x == 'T':
        rev_strand.append('A')
    elif x == 'G':
        rev_strand.append('C')
    elif x == 'C':
        rev_strand.append('G')

print ''.join( rev_strand )
