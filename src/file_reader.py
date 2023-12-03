class FileReader:
    
    def __init__(self, fileName, opcode = False, instruction= True) -> None:
        self.file = open(fileName, 'r')
        self.instructions = []
        self.opCode = opcode
        self.instruction = instruction

    def read(self) -> None:
        content = self.file.read()
        content = content.split("\n")
        
        for line in content:
            if line == '':
                continue
            self.parse(line)
    
    def parse(self, line):
        instruction = []
        line = line.split(" ", 2)
        for i in line:
            if i == '':
                continue
            i.strip(" ")
            instruction.append(i)
        
        self.instructions.append(instruction)
    
    def getInstructions(self):
        return self.instructions
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File closed")


# TODO : change read method to read opcode or instructions
# TODO : make a functions for parsing instructions and anther for parsing opcodes
# TODO : make to return opcode or instructions
        
