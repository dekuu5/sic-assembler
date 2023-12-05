from src.file_reader import FileReader
from src.sic_assembler import PcGenerator,Assembler


def main():
    fileName = '/home/dekuu5/Code/myProjects/faculty-projects/sic-assembler/testEx/test1.txt'
    with FileReader(fileName, False, True) as fileReader:
        fileReader.read()
        instructions = fileReader.getInstructions()
    
    opCodeFile = '/home/dekuu5/Code/myProjects/faculty-projects/sic-assembler/testEx/opCode.txt'
    with FileReader(opCodeFile, True, False) as fileReaderOpcode:
        fileReaderOpcode.read()
        opCodeMap = fileReaderOpcode.getOpcodes()

    pcGenerator = PcGenerator(instructions)
    pcGenerator.generate()
    instructions = pcGenerator.getInstructions()
    labelMap = pcGenerator.getLabelMap()
    assembler = Assembler(instructions,labelMap,opCodeMap)
    objectCode = assembler.getObjectCode()
    assembler.generateObjectCode()
    assembler.save("ob1.txt")
    
    

if __name__ == "__main__":
    main()