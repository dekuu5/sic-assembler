from src.file_reader import FileReader
from src.sic_assembler import PcGenerator,Assembler


def main():
    fileName = '/home/dekuu5/Code/myProjects/faculty-projects/sic-assembler/testEx/test1.txt'
    with FileReader(fileName) as fileReader:
        fileReader.read()
        instructions = fileReader.getInstructions()

    for i in instructions:
        print(i)
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