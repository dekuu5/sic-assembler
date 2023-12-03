class FileReader:
    
    def __init__(self, fileName, opcode=False, instruction=True) -> None:
        self.file_name = fileName
        self.opcode_flag = opcode
        self.instruction_flag = instruction
        self.file = None
        self.instructions = []
        self.opcodes = {}

    def __enter__(self):
        try:
            self.file = open(self.file_name, 'r')
            return self
        except FileNotFoundError:
            print(f"Error: File '{self.file_name}' not found.")
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print("File closed")
        
    def read(self):
        if self.opcode_flag:
            self.read_opcodes()
        elif self.instruction_flag:
            self.read_instructions()

    def parse_instruction(self, line):
        parts = line.split(" ", 2)
        parts = [part.strip() for part in parts if part.strip()]

        if len(parts) > 0:
            self.instructions.append(parts)

    def parse_opcode(self, line):
        parts = line.split(" ", 1)
        parts = [part.strip() for part in parts if part.strip()]

        if len(parts) > 0:
            self.opcodes[parts[0]] = parts[1]

    def read_instructions(self) -> None:
        if not self.file:
            return

        for line in self.file:
            if line.strip():
                instruction = self.parse_instruction(line.strip())
                if instruction:
                    self.instructions.append(instruction)

    def read_opcodes(self) -> None:
        if not self.file:
            return
        lines = self.file.readlines()
        for line in lines:
            if line.strip():
                self.parse_opcode(line.strip())
                

    def getInstructions(self):
        return self.instructions
    
    def getOpcodes(self):
        return self.opcodes

# TODO : change read method to read opcode or instructions
# TODO : make a functions for parsing instructions and anther for parsing opcodes
# TODO : make to return opcode or instructions
        
