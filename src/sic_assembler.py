class PcGenerator:
    def __init__(self,instructions):
        self.instructions = instructions
        self.start = instructions[0][2]
        