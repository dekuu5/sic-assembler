from src.file_reader import FileReader

def main():
    fileName = '/home/dekuu5/Code/myProjects/faculty-projects/sic-assembler/testEx/test1.txt'
    with FileReader(fileName) as fileReader:
        fileReader.read()
        instructions = fileReader.getInstructions()
        for i in instructions:
            for j in i:
                print(j, end=" ")
            print("\n")


if __name__ == "__main__":
    main()