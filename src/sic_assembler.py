class PcGenerator:
    def __init__(self,instructions):
        self.instructions = instructions
        self.start = hex((int)(instructions[0][2]))
        self.directives = ['BYTE', 'WORD', 'RESB', 'RESW']
        self.labelMap = {}

    def generate(self):
        currentPc = int(self.start, 16)  # Convert the hexadecimal string to an integer
        for index, instruction in enumerate(self.instructions[1:]):
            if len(instruction) < 3:
                self.instructions[index + 1].insert(0, hex(currentPc))
                currentPc += 3  # Increment the integer value
            elif instruction[2] in self.directives:
                self.labelMap[instruction[0]] = hex(currentPc)
                self.instructions[index + 1][0] = hex(currentPc)
                if instruction[2] == 'BYTE':
                    currentPc += len(instruction[3]) - 3
                elif instruction[2] == 'WORD':
                    currentPc += 3
                elif instruction[2] == 'RESB':
                    currentPc += int(instruction[3])
                elif instruction[2] == 'RESW':
                    currentPc += 3 * int(instruction[3])
            else:
                self.labelMap[instruction[0]] = hex(currentPc)
                self.instructions[index + 1][0] = hex(currentPc)
                currentPc += 3
        
    def getLabelMap(self):
        return self.labelMap
    
    def getInstructions(self):
        return self.instructions
        