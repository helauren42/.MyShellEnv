import sys
import subprocess
import os
import argparse

parser = argparse.ArgumentParser(prog="build dojo dir", description="Build a directory with subdirectories and files for the dojo")
parser.add_argument("path", type=str, help="the project directory path")
parser.add_argument("amount", type=int, help="the amount of exercises for that dojo project")
args = parser.parse_args()

CWD = os.getcwd()
PATH = os.path.abspath(os.path.join(CWD, args.path))
AMOUNT = args.amount

print(f"CWD: {CWD}")
print(f"Amount: {AMOUNT}")
subprocess.run(["mkdir", f"{PATH}"])

if not os.path.isdir(PATH):
    print(f"Error path not valid: {PATH}")
    sys.exit(1)

print(f"PATH:{PATH}")

for i in range(1, AMOUNT +1):
    subprocess.run(["mkdir", "-p", f"{i}"], cwd=PATH)
    subprocess.run(f"touch script{i}.py", shell=True, cwd=os.path.join(PATH, str(i)))
