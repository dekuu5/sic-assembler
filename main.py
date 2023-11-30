from src.file_reader import FileReader
from src.sic_assembler import PcGenerator

def main():
    fileName = '/home/dekuu5/Code/myProjects/faculty-projects/sic-assembler/testEx/test1.txt'
    with FileReader(fileName) as fileReader:
        fileReader.read()
        instructions = fileReader.getInstructions()

    pcGenerator = PcGenerator(instructions)
    pcGenerator.generate()
    instructions = pcGenerator.getInstructions()
    labelMap = pcGenerator.getLabelMap()
    for i in instructions:
        print(i)
    print(labelMap)
    

if __name__ == "__main__":
    main()