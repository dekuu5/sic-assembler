from src.file_reader import FileReader
from src.sic_assembler import PcGenerator,Assembler


def main():
    fileName = '/home/dekuu5/Code/myProjects/faculty-projects/sic-assembler/testEx/test1.txt'
    with FileReader(fileName) as fileReader:
        fileReader.read()
        instructions = fileReader.getInstructions()

    pcGenerator = PcGenerator(instructions)
    pcGenerator.generate()
    instructions = pcGenerator.getInstructions()
    labelMap = pcGenerator.getLabelMap()
    assembler = Assembler(instructions,labelMap)
    assembler.GenerateObjectCode()
    Assembler.Save("ob1.txt")
    

if __name__ == "__main__":
    main()