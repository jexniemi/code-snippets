from os import listdir
from os.path import isfile, join
import json

"""
Simple python snippet that reads all file and directory names in 
a directory and creates a json array out of them.
"""

mypath = "/path/to/your/directory"

def main():
  data = []
  onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  for file in onlyfiles:
    data.append({ "name": file })

  jsonData = json.dumps(data)
  f = open("result.json", "a")
  f.write(jsonData)
  f.close()

if __name__ == "__main__":
    main()