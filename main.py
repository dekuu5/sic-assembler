from src.file_reader import FileReader
from src.sic_assembler import PcGenerator,Assembler


def main():
    fileName = '/home/dekuu5/Code/myProjects/faculty-projects/sic-assembler/testEx/test1.txt'
    with FileReader(fileName, False, True) as fileReader:
        fileReader.read()
        instructions = fileReader.getInstructions()
    OpCodeFileName = '/home/dekuu5/Code/myProjects/faculty-projects/sic-assembler/testEx/test.txt'
    with FileReader(OPCodefileName, True, False) as fileReader:
        fileReader.read()
        opcodes = fileReader.getOpcodes()

    for i in instructions:
        print(i)
    print()
    for i in opcodes.keys():
        print(i,opcodes[i])
    pcGenerator = PcGenerator(instructions)
    pcGenerator.generate()
    instructions = pcGenerator.getInstructions()
    labelMap = pcGenerator.getLabelMap()
    for i in instructions:
        print(i)
    # assembler = Assembler(instructions,labelMap)
    # assembler.generateObjectCode()
    # Assembler.Save("ob1.txt")
    

if __name__ == "__main__":
    main()