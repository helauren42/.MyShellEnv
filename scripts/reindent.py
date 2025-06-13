import sys

def help(file=sys.stdout):
    print("Ex: reindent old_format size new_format size files..", file=file)
    print('format must be described as "spaces" or "tabs"', file=file)
    sys.exit(0)

def error():
    help(file=sys.stderr)
    sys.exit(1)

class checkValid:
    @staticmethod
    def validArgs():
        if len(sys.argv) == 1 or (len(sys.argv) == 2 and (sys.argv[1] == "--help" or sys.argv[1] == "-h")):
            help()
        if len(sys.argv) < 6:
            error()
        if not (sys.argv[2].isdigit() and sys.argv[4].isdigit() and int(sys.argv[2]) > 0 and int(sys.argv[4]) > 0):
            error()
        if sys.argv[1] not in ["spaces", "tabs"] or sys.argv[3] not in ["spaces", "tabs"]:
            error()

checkValid.validArgs()

class replaceIndent:
    old_format = sys.argv[1]
    new_format = sys.argv[3]
    old_size = int(sys.argv[2])
    new_size = int(sys.argv[4])

    @staticmethod
    def replace(line: str):
        # Calculate total visual columns from leading whitespace
        total_columns = 0
        i = 0
        
        if replaceIndent.old_format == "tabs":
            # Count tabs and multiply by tab width (old_size)
            tab_count = 0
            while i < len(line) and line[i] == '\t':
                tab_count += 1
                i += 1
            total_columns = tab_count * replaceIndent.old_size
        else:  # old_format == "spaces"
            # Count raw spaces (ignore old_size for column count)
            space_count = 0
            while i < len(line) and line[i] == ' ':
                space_count += 1
                i += 1
            total_columns = space_count

        # Generate new indentation
        if replaceIndent.new_format == "tabs":
            tabs = total_columns // replaceIndent.new_size
            spaces = total_columns % replaceIndent.new_size
            new_indent = "\t" * tabs + " " * spaces
        else:  # new_format == "spaces"
            new_indent = " " * total_columns

        return new_indent + line[i:]

def doYourThing(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    with open(filename, 'w') as writeFile:
        for line in lines:
            processed_line = replaceIndent.replace(line)
            writeFile.write(processed_line)

def main():
    for i in range(5, len(sys.argv)):
        doYourThing(sys.argv[i])

if __name__ == "__main__":
    main()
