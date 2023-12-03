from src.file_reader import FileReader
from src.sic_assembler import PcGenerator,Assembler


def main():
    fileName = '\\Users\\ahmed\Downloads\\sic-assembler-main (1)\\sic-assembler-main\\testEx\\test1.txt'
    with FileReader(fileName, False, True) as fileReader:
        fileReader.read()
        instructions = fileReader.getInstructions()
    
    pcGenerator = PcGenerator(instructions)
    pcGenerator.generate()
    instructions = pcGenerator.getInstructions()
    labelMap = pcGenerator.getLabelMap()
    for i in instructions:
        print(i)
    assembler = Assembler(instructions,labelMap)
    assembler.generateObjectCode()
    assembler.save("result//ob1.txt") #create a folder  for result ignore it in testing:" !!!!!!
    objectCode = assembler.getObjectCode()
    print(objectCode)
    
    

if __name__ == "__main__":
    main()
