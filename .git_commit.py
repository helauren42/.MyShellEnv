import sys
import os
import subprocess

def runCommand(command):
	result = subprocess.run(command, shell=True, text=True, capture_output=True)

	if result.returncode:
		print(f"Error: {result.stderr}")
		sys.exit(1)
	else:
		print(result.stdout)

def main():

	if len(sys.argv) < 2:
		print("Usage: ./gitcom your commit message")
		sys.exit(1)
	
	message = sys.argv[1]

	if len(sys.argv) > 2:
		message = " ".join(sys.argv[1:])

	message = message.strip()
	print(message)

	os.system("git add .")
	runCommand(f"git commit -m \"{message}\"")

if __name__ == "__main__":
	main()
