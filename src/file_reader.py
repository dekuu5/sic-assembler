class FileReader:
    
    def __init__(self, fileName, opcode=False, instruction=True) -> None:
        self.file_name = fileName
        self.opcode_flag = opcode
        self.instruction_flag = instruction
        self.file = None
        self.instructions = []
        self.opcodes = []

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

    def parse_instruction(self, line):
        parts = line.split(" ", 2)
        parts = [part.strip() for part in parts if part.strip()]

        if len(parts) > 1:
            return parts

    def parse_opcode(self, line):
        parts = line.split(" ", 2)
        parts = [part.strip() for part in parts if part.strip()]

        if len(parts) > 0:
            return parts[0]

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

        for line in self.file:
            if line.strip():
                opcode = self.parse_opcode(line.strip())
                if opcode:
                    self.opcodes.append(opcode)

    def getInstructions(self):
        return self.instructions
    
    def getOpcodes(self):
        return self.opcodes

# TODO : change read method to read opcode or instructions
# TODO : make a functions for parsing instructions and anther for parsing opcodes
# TODO : make to return opcode or instructions
        
