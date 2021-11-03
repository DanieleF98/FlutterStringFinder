import os
import os.path
import re
for dirpath, dirnames, filenames in os.walk(os.path.dirname(__file__)):
    for filename in [f for f in filenames if f.endswith(".dart")]:
            try:
                with open(os.path.join(dirpath, filename), "r") as f:
                    for line in f:
                        if (line.__contains__('\"') | line.__contains__('\'')) & line.__contains__('package') == False:
                            strTag = re.search("\"(.+?)\"|\'(.+?)\'", line)
                            if(strTag):
                                print("{}".format(strTag.group(0)))
            except:
                continue
