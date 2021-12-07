from typing import ValuesView
from Input.Day2 import day2InputData

def SolveDay2():
	input0 = day2InputData.copy()

	print("Day 2.1: " + SolutionDay2_1(input0))

def SolutionDay2_1(input):
	depth = 0
	horizontalPosition = 0

	for i in input:
		splitInput = i.split()
		direction = splitInput[0]
		value = int(splitInput[1])

		match direction:
			case "forward":
				horizontalPosition += value
			case "down":
				depth += value
			case "up":
				depth -= value
			case _:
				print("match error")

	ProblemResult = horizontalPosition * depth

	return (f"{horizontalPosition} x {depth} = {ProblemResult}")

