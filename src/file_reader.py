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

    def read(self) -> None:
        if not self.file:
            return

        content = self.file.read()
        content = content.split("\n")
        
        for line in content:
            if line == '':
                continue
            self.parse(line)

    def parse(self, line):
        parts = line.split(" ", 2)
        parts = [part.strip() for part in parts if part.strip()]

        if self.instruction_flag and len(parts) > 1:
            self.instructions.append(parts)

        if self.opcode_flag and len(parts) > 0:
            self.opcodes.append(parts[0])

    def getInstructions(self):
        return self.instructions
    
    def getOpcodes(self):
        return self.opcodes


# TODO : change read method to read opcode or instructions
# TODO : make a functions for parsing instructions and anther for parsing opcodes
# TODO : make to return opcode or instructions
        
