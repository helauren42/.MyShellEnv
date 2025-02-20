import argparse
from typing import Optional
import sys

parser = argparse.ArgumentParser(prog="file line separator", description="create a line separator for the given line in file")

parser.add_argument("file", type=str, help="The file in which to add a line separator")
parser.add_argument("line", type=int, help="The line number in which to add the line separator")
parser.add_argument("-c", "--comment", nargs='?', type=str, default=None, help="The comment in the middle of the line (optional)")

args = parser.parse_args()

def readFile() -> list[str]:
    with open(args.file, "r") as file:
        red = file.readlines()
    return red

def addLine(lines: list[str]):
    with open(args.file, "w") as file:
        for i, line in enumerate(lines):
            if i == args.line -1 and args.comment == None:
                file.write(120 * '-' + '\n')
            elif i == args.line -1:
                num = int((120 - (len(args.comment) + 2)) // 2)
                file.write(num * '-' + f" {args.comment} " + num * '-' + '\n')
            file.write(line)
        print(i)
        if i == args.line -2 and args.comment == None:
            file.write(120 * '-' + '\n')
        elif i == args.line -2:
            num = int((120 - (len(args.comment) + 2)) // 2)
            file.write(num * '-' + f" {args.comment} " + num * '-' + '\n')

def main():
    lines = readFile()
    if args.line > len(lines) +1:
        print(f"The file has {len(lines)} lines can't write to line {args.line}")
        sys.exit(1)
    addLine(lines)

main()
