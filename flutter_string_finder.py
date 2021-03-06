import os
import os.path
import re
from enum import Enum

class DirectoriesToSkip(Enum):
    models = 1

constants = []

fileExtension = input("Please enter the extension of files to search (w/o the . at the beginning): ")

for dirpath, dirnames, filenames in os.walk(os.path.dirname(__file__)):
    for dirnameg in dirnames:
        for dir in DirectoriesToSkip:
            if(dirnameg.__contains__(f'{dir.name}')):
                continue
        else:
            for filename in [f for f in filenames if f.endswith(f".{fileExtension}")]:
                with open(os.path.join(dirpath, filename), "r") as f:
                    for line in f:
                        if(re.search('\$', line) == None):
                            if (line.__contains__('dart') == False & line.__contains__('package') == False):
                                strTag = re.search("\"(.+?)\"|\'(.+?)\'", line)
                                if(strTag):
                                    constants.append("const {} = {};".format(re.sub(
                                        '[^A-Za-z0-9]+', '', strTag.group(0).title()), strTag.group(0).replace('\'', "\\'")))
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue
for w in list(dict.fromkeys(constants)):
    print(w)