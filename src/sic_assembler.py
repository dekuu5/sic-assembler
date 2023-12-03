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
    def __init__(self, instructions, labelMap):
        self.instructions = instructions
        self.labelMap= labelMap
        self.directives = ['BYTE', 'WORD', 'RESB', 'RESW']
        self.objectCode = []
        self.instruction_map = {
    'ADD': '18',
    'AND': '40',
    'COMP': '28',
    'DIV': '24',
    'J': '3C',
    'JEQ': '30',
    'JGT': '34',
    'JLT': '38',
    'JSUB': '48',
    'LDA': '00',
    'LDB': '68',
    'LDCH': '50',
    'LDF': '70',
    'LDL': '08',
    'LDS': '6C',
    'LDT': '74',
    'LDX': '04',
    'MUL': '20',
    'OR': '44',
    'RD': 'D8',
    'RSUB': '4C',
    'SIO': 'F0',
    'SSK': 'EC',
    'STA': '0C',
    'STB': '78',
    'STCH': '54',
    'STF': '80',
    'STI': 'D4',
    'STL': '14',
    'STS': '7C',
    'STSW': 'E8',
    'STT': '84',
    'STX': '10',
    'SUB': '1C',
    'SUBF': '5C',
    'SUBR': '94',
    'SVC': 'B0',
    'TD': 'E0',
    'TIO': 'F8',
    'TIX': '2C',
    'TIXR': 'B8',
    'WD': 'DC',
}
        

    def generateObjectCode(self):
        for instruction in self.instructions:
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
        labelAddres = self.labelMap[instruction[2]]
        opCode = self.instruction_map[instruction[1]]
        binaryAddress =  bin(int(labelAddres, 16))[2:]
        binaryAddress[0] = 1
        labelAddres = hex(int(binaryAddress,2))[2:]
        self.objectCode.append(opCode + labelAddres)
    
    def generateObjectCodeByteOrWord(self, instruction):
        if instruction[1] == 'BYTE':
            self.objectCode.append(self.byteToObjectCode(instruction[2]))
        else: 
            self.objectCode.append(self.wordToObjectCode(instruction[2]))
        


    def byteToObjectCode(byteData: str):
        if byteData.startswith("X'") and byteData.endswith("'"):
            return int(byteData[2:-1], 16)
        elif byteData.startswith("C'") and byteData.endswith("'"):
            return ord(byteData[2: -1])
        else:
            return int(byteData)

    def wordToObjectCode(wordData):
        if wordData.startswith("X'") and wordData.endswith("'"):
            return int(wordData[2:-1], 16)
        elif wordData.startswith("C'") and wordData.endswith("'"):
            return sum(ord(char) << (8 * index) for index, char in enumerate(wordData[2:-1]))
        else:
            return int(wordData)
                

