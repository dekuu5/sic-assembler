class FileReader:
    
    def __init__(self, fileName, opcode = False, instructions= True) -> None:
        self.file = open(fileName, 'r')
        self.instructions = []
        self.opCode = opcode
        self.instructions = instructions

    def read(self) -> None:
        content = self.file.read()
        content = content.split("\n")
        
        for line in content:
            
            self.parse(line)
    
    def parse(self, line):
        instruction = []
        line = line.split(" ")
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
        
