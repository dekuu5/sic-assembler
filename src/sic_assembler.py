class PcGenerator:
    def __init__(self,instructions):
        self.instructions = instructions
        self.start = int(instructions[0][2],16)
        self.directives = ['BYTE', 'WORD', 'RESB', 'RESW']
        self.labelMap = {}

    def generate(self):
        currentPc = self.start 
        for index, instruction in enumerate(self.instructions[1:]):
            if len(instruction) < 3:
                self.instructions[index + 1].insert(0, hex(currentPc))
                currentPc += 3
            elif instruction[1] in self.directives:
                self.labelMap[instruction[0]] = hex(currentPc)
                self.instructions[index + 1][0] = hex(currentPc)
                if instruction[1] == 'BYTE':
                    currentPc += len(instruction[2]) - 3
                elif instruction[1] == 'WORD':
                    currentPc += 3
                elif instruction[1] == 'RESB':
                    currentPc += int(instruction[2])
                elif instruction[1] == 'RESW':
                    currentPc += 3 * int(instruction[2])
            else: 
                self.labelMap[instruction[0]] = hex(currentPc)
                self.instructions[index + 1][0] = hex(currentPc)
                currentPc += 3
        
    def getLabelMap(self):
        return self.labelMap
    
    def getInstructions(self):
        return self.instructions
        


class Assembler:
    def __init__(self, instructions, labelMap, instructionMap):
        self.instructions = instructions
        self.labelMap= labelMap
        self.directives = ['BYTE', 'WORD', 'RESB', 'RESW']
        self.objectCode = []
        self.instruction_map = instructionMap
#         s = {
#     'ADD': '18',
#     'AND': '40',
#     'COMP': '28',
#     'DIV': '24',
#     'J': '3C',
#     'JEQ': '30',
#     'JGT': '34',
#     'JLT': '38',
#     'JSUB': '48',
#     'LDA': '00',
#     'LDB': '68',
#     'LDCH': '50',
#     'LDF': '70',
#     'LDL': '08',
#     'LDS': '6C',
#     'LDT': '74',
#     'LDX': '04',
#     'MUL': '20',
#     'OR': '44',
#     'RD': 'D8',
#     'RSUB': '4C',
#     'SIO': 'F0',
#     'SSK': 'EC',
#     'STA': '0C',
#     'STB': '78',
#     'STCH': '54',
#     'STF': '80',
#     'STI': 'D4',
#     'STL': '14',
#     'STS': '7C',
#     'STSW': 'E8',
#     'STT': '84',
#     'STX': '10',
#     'SUB': '1C',
#     'SUBF': '5C',
#     'SUBR': '94',
#     'SVC': 'B0',
#     'TD': 'E0',
#     'TIO': 'F8',
#     'TIX': '2C',
#     'TIXR': 'B8',
#     'WD': 'DC',
# }
        

    def generateObjectCode(self):
        for instruction in self.instructions[1:]:
            if ',X' in instruction[2]:
                instruction = [i.replace(',X', '') for i in instruction]
                self.GenerateObjectCodeIndexing(instruction)
            elif instruction[1] == 'RESW' or instruction[1] == 'RESB':
                continue
            elif instruction[1] == 'BYTE' or instruction[1] == 'WORD':
                self.generateObjectCodeByteOrWord(instruction)
            else :
                self.generateObjectCodeNonIndexing(instruction)
            
        print("Object Code Generated")
    
    def GenerateObjectCodeIndexing(self, instruction):
        labelAddress = self.labelMap[instruction[2]]
        opCode = self.instruction_map[instruction[1]]
        binaryAddress =  bin(int(labelAddress, 16))[2:]
        binaryAddress = '1' + binaryAddress.zfill(15)
        labelAddress = hex(int(binaryAddress,2))[2:]
        self.objectCode.append(opCode + labelAddress)
    
    def generateObjectCodeByteOrWord(self, instruction):
        if instruction[1] == 'BYTE':
            self.objectCode.append(self.byteToObjectCode(instruction[2]))
        else: 
            self.objectCode.append(self.wordToObjectCode(instruction[2]))
        
    def generateObjectCodeNonIndexing(self,instruction):
        labelAddres = self.labelMap[instruction[2]][2:]
        opCode = self.instruction_map[instruction[1]]
        self.objectCode.append(opCode + labelAddres)

    def byteToObjectCode(self, byteData):
        if byteData.startswith("X'") and byteData.endswith("'"):
            return int(byteData[2:-1], 16)
        elif byteData.startswith("C'") and byteData.endswith("'"):
            dataInput = [hex(ord(char))[2:] for char in byteData[2:-1]]
            dataOutput = ''.join(dataInput)
            return dataOutput.upper()

    def wordToObjectCode(self, wordData):
        return hex(int(wordData))[2:]
        
    def getObjectCode(self):
        return self.objectCode
    
    def save(self, filename):
        try:
            with open(filename, 'w') as file:
                for codeLine in self.objectCode:
                    file.write(str(codeLine) + '\n')
            print(f"Object code successfully saved to {filename}")
            return True
        except Exception as e:
            print(f"Error saving object code to {filename}: {e}")
            return False
                

