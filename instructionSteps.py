instructionSteps=[
  "turn left",
  "go straight for two blocks",
  "turn right",
  "keep going until you see the dog statue",
  "turn right",
  "turn right again",
  "park right on the sidewalk"
]

instructionStepsButScreemed = []

for nextInstruction in instructionSteps:
  upperInstruction = nextInstruction.upper()
  instructionStepsButScreemed.append(upperInstruction)

print (instructionStepsButScreemed)


instructionSteps=[
  "turn left",
  "go straight for two blocks",
  "turn right",
  "keep going until you see the dog statue",
  "turn right",
  "turn right again",
  "park right on the sidewalk"
]

instructions = "First,"

for nextInstruction in instructionSteps:
  instructions = instructions + nextInstruction + ", then "

print(instructions + "you're there!") 

