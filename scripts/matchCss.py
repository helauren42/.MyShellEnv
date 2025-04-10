import sys
import subprocess
import os

DEBUG = False

class checker():
    @staticmethod
    def helpMessage():
        print("format: python3 matchCss.py html/jsdir cssdir")
        print("html/jsdir and cssdir, are paths to the directories containing the files")
    @staticmethod
    def args():
        if len(sys.argv) != 3:
            checker.helpMessage()
            sys.exit(1)

class fetcher():
    @staticmethod
    def getFiles(path: str, typesuffix: str):
        if(path == '.'):
            result = subprocess.run(["ls"], shell=True, capture_output=True, text=True)
        else:
            result = subprocess.run([f'cd {path}' , "ls"], shell=True, capture_output=True, text=True)
        if DEBUG == True:
            print(f"result: {result}")
        filenames = result.stdout.split()
        ret = []
        for file in filenames:
            if file.endswith(typesuffix):
                ret.append(file)
        return ret

class Object():
    def __init__(self, _file:str, _line: int, _type: str, _name: str) -> None:
        self.type = _type
        self.line = _line
        self.file = _file
        self.name = _name
    def __str__(self) -> str:
        return f'File: {self.file}, line: {self.line}, type: {self.type}, name: {self.name}'

class cssDeclarations():
    def __init__(self, _type:str, _name:str):
        self.type = _type
        self.name = _name

class AbstractMatcher():
    @staticmethod
    def extractName(line:str, temp:int, needle:str):
        equalpos = line.find('=', temp)
        character = line[equalpos +1]
        start = equalpos+2
        end = line.find(character, start)
        return line[start:end]

    @staticmethod
    def processLine(line:str, filename: str, lineNum:int):
        needles = ['id=', 'class=', 'className=']
        objects = []
        pos = 0
        while(pos >= 0):
            found = False
            for needle in needles:
                temp = line.find(needle, pos)
                if temp < 0:
                    break
                if temp >= 0:
                    _type = "id" if needle == "id=" else "class"
                    found = True
                    name = AbstractMatcher.extractName(line, temp, needle)
                    objects.append(Object(filename, lineNum, _type, name))
                    pos = line.find("=", temp) + 1 + len(needle)
                    break
            if found == False:
                break
        return objects
            
    @staticmethod
    def getObjectsFile(file:str):
        objects = []
        with open(os.path.join(sys.argv[1], file), "r") as readFile:
            lines = readFile.readlines();
            i = 1
            for line in lines:
                objects += AbstractMatcher.processLine(line, file, i)
                i += 1
        return objects

    @staticmethod
    def getDefinedTypes(cssfile):
        ret = []
        with open(os.path.join(sys.argv[2], cssfile), "r") as file:
            lines = file.readlines()
            for line in lines:
                if not line[0] == '.' and not line[0] == '#':
                    continue
                _type = 'id' if line[0] == '#' else 'class'
                end = 1
                while end < len(line) and line[end] != ' ' and line[end] != '   ' and line[end] != '{' and line[end] != ':':
                    end += 1
                name = ""
                if end == len(line):
                    name = line[1]
                else:
                    name = line[1:end]
                ret.append(cssDeclarations(_type, name))
        return ret

    @staticmethod
    def getDefinedTypesFiles(cssFiles) -> list[cssDeclarations]:
        ret = []
        for file in cssFiles:
            ret += AbstractMatcher.getDefinedTypes(file)
        return ret

class matcher(AbstractMatcher):
    @staticmethod
    def getObjects(files):
        objects = []
        for file in files:
            objects += AbstractMatcher.getObjectsFile(file)
        return objects
    @staticmethod
    def findMissMatches(objects: list[Object], definedTypes: list[cssDeclarations]):
        missMatches: list[Object] = []
        for _object in objects:
            found = False
            for defined in definedTypes:
                if _object.name == defined.name and _object.type == defined.type:
                    found = True
                    break
            if found == False:
                missMatches.append(_object)
        return missMatches

def main():
    checker.args()
    jsFiles = fetcher.getFiles(sys.argv[1], ".js")
    htmlFiles = fetcher.getFiles(sys.argv[1], ".html")
    cssFiles = fetcher.getFiles(sys.argv[2], ".css")
    objectsFiles = jsFiles + htmlFiles
    objects = matcher.getObjects(objectsFiles)
    definedTypes = AbstractMatcher.getDefinedTypesFiles(cssFiles)
    if DEBUG ==True:
        print(objectsFiles)
        print(cssFiles)
        print("Objects: ")
        for _object in objects:
            print(_object)
        print("definedTypes: ")
        for defined in definedTypes:
            print(f'name: {defined.name}, type: {defined.type}')
    missmatches = matcher.findMissMatches(objects, definedTypes)
    if(len(missmatches) == 0):
        print("No missmatches found, keep up the good work!")
    else:
        print("Found unmatched css objects:")
        for _object in missmatches:
            print(_object)

main()
