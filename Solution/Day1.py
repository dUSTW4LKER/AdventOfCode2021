from Input.Day1 import inputMeasurements

def SolveDay1():
	print (CalculateIncreses(inputMeasurements))

def CalculateIncreses(input):
	previousInput = input.pop()
	n = 0
	for i in input:
		if i > previousInput:
			n += 1
		previousInput = i
	return n
