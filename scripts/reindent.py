import sys

def help(file=sys.stdout):
    print("Ex: retab file_name old_format size new_format size", file=file)
    print('format must be described as "spaces" or "tabs"', file=file)
    print('indeed if you want tabs as format it doesn\'t make sense to ask for a numeric string as size but just put one for goodness sake')
    sys.exit(0)

def error():
    help(file=sys.stderr)
    sys.exit(1)

class checkValid:
    @staticmethod
    def isFormat(word:str):
        if(word == "spaces" or word == "tabs"):
           return True
        return False
    @staticmethod
    def validArgs():
        if len(sys.argv) == 1 or (len(sys.argv) == 2 and (sys.argv[1] == "--help" or sys.argv[1] == "-h")):
            help()
        if len(sys.argv) != 6:
            error()
        if not (sys.argv[3].isdigit() and sys.argv[5].isdigit() and int(sys.argv[3]) > 0 and int(sys.argv[5]) > 0):
            error()

checkValid.validArgs();

class replaceIndent:
    old_format = sys.argv[2]
    new_format = sys.argv[4]
    target = int(sys.argv[3])
    new_size = int(sys.argv[5])
    indent = " " * target if old_format == "spaces" else "\t"
    new_indent = "\t" if new_format == "tabs" else " " * new_size

    @staticmethod
    def replace(line: str):
        blocks = 0
        i = 0
        if replaceIndent.old_format == "tabs":
            while i < len(line) and line[i] == "\t":
                blocks += 1
                i += 1
        else:
            current_count = 0
            while i < len(line) and line[i] == " ":
                current_count += 1
                if current_count == replaceIndent.target:
                    blocks += 1
                    current_count = 0
                i += 1
        if blocks == 0:
            return line
        line = line[i:]
        line = replaceIndent.new_indent * blocks + line
        return line

def doYourThing():
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        with open(sys.argv[1], 'w') as writeFile:
            writeFile.write("")
            for line in lines:
                line = replaceIndent.replace(line=line)
                writeFile.write(line)

def main():
    doYourThing()

main()
