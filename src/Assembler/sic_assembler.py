

class PcGenerator:
    def __init__(self,instructions):
        self.instructions = instructions
        try:
            self.start = int(instructions[0][2],16)
        except:
            self.start = int('0',16)

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
        
        

    def generateObjectCode(self):
        for instruction in self.instructions[1:]:
            if ',X' in instruction[-1]:
                instruction = [i.replace(',X', '') for i in instruction]
                self.GenerateObjectCodeIndexing(instruction)
            elif instruction[1] == 'RESW' or instruction[1] == 'RESB' or instruction[1] == 'END':
                continue
            elif instruction[1] == 'BYTE' or instruction[1] == 'WORD':
                self.generateObjectCodeByteOrWord(instruction)
            else :
                self.generateObjectCodeNonIndexing(instruction)
            
        print("Object Code Generated")
        print(self.objectCode)
        self.formatObjectCode()
    
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
        if instruction[1] == 'RSUB':
            self.objectCode.append(self.instruction_map[instruction[1]] + '0000')
            return
        print(instruction)
        labelAddres = self.labelMap[instruction[-1]][2:]
        opCode = self.instruction_map[instruction[1]]
        self.objectCode.append(opCode + labelAddres.zfill(4))

    def byteToObjectCode(self, byteData):
        print(byteData)
        if byteData.startswith("X'") and byteData.endswith("'"):
            return byteData[2:-1]
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
                file.write("\t SYM_table\n")
                for i, j in self.labelMap.items():
                    file.write(f"{i}: {j}\n") 
                file.write("\t Op_table\n")
                for i in self.instructions[1:]:
                    if i[1] in self.directives or i[1] == 'END': continue
                    file.write(f"{i[1]}: {self.instruction_map[i[1]]}\n") 
                for codeLine in self.objectCode:
                    file.write(str(codeLine) + '\n')
                file.write(self.FinalObjectCode)
            print(f"Object code successfully saved to {filename}")
            return True
        except Exception as e:
            print(f"Error saving object code to {filename}: {e}")
            return False
    
    def formatObjectCode(self):
        index =0
        obj=[]
        textRecord=[]
        length = hex(int(self.instructions[-1][0][2:], 16) - int(self.instructions[1][0][2:], 16))[2:].zfill(6)
        header = f"H^{self.instructions[0][0]}^{self.instructions[1][0][2:]}^{length}"
        end = f"E^{self.instructions[1][0][2:]}"
        j=self.instructions[1][0][2:]
        for i, item in enumerate(self.objectCode):
            print(item)
            index += len(item)
            if index<=60:
                obj.append(item)
            else:
                index -=len(item)
                text=f"T^{j.zfill(6)}^{hex(int(index/2))[2:].zfill(2)}^{'^'.join(obj)}"
                textRecord.append(text)
                j=self.instructions[i+1][0][2:]
                obj=[item]
                index=len(item)
        text=f"T^{j.zfill(6)}^{hex(int(index/2))[2:].zfill(2)}^{'^'.join(obj)}"
        textRecord.append(text)
        t='\n'.join(textRecord)
        self.FinalObjectCode = f"{header}\n{t}\n{end}"
                

