from Assembler.file_reader import FileReader
from Assembler.sic_assembler import PcGenerator,Assembler
import sys
import os


def find_file(file_path):
    if os.path.isfile(file_path):
        print(f"File found: {file_path}")
        return True
    else:
        print(f"File not found: {file_path}")
        return False

def getFilePath():
    if len(sys.argv)< 3:
        print(f"Usage: python {sys.argv[0]} <SIC_CODE> <OP_code_PatH>")
        sys.exit(1)
    sicCode = sys.argv[1]
    OPCode = sys.argv[2]

    if find_file(sicCode) and find_file(OPCode):
        return sicCode, OPCode  
    else:
        
        sys.exit(1)



def main():
    fileName, opCodeFile = getFilePath()
    with FileReader(fileName, False, True) as fileReader:
        fileReader.read()
        instructions = fileReader.getInstructions()
    
    with FileReader(opCodeFile, True, False) as fileReaderOpcode:
        fileReaderOpcode.read()
        opCodeMap = fileReaderOpcode.getOpcodes()

    pcGenerator = PcGenerator(instructions)
    pcGenerator.generate()
    instructions = pcGenerator.getInstructions()
    labelMap = pcGenerator.getLabelMap()
    for i in instructions:
        for j in i :
            print(j,end = "\t")
        print()
    assembler = Assembler(instructions,labelMap,opCodeMap)
    assembler.generateObjectCode()
    assembler.save("ob1.txt")
    print(assembler.FinalObjectCode)
    
    

if __name__ == "__main__":
    main()