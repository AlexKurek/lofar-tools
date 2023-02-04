# Prepare MSs list for .json files for LINC >= 4
# Place this script in main MS folder. No other folders than MSs should be there

import os
rootMSfolder='./'
listFname = "MSlist.txt"

dirList = [ item for item in os.listdir(rootMSfolder) if os.path.isdir(os.path.join(rootMSfolder, item)) ]
dirListSorted = sorted(dirList)

try:
  os.remove(listFname)
except OSError:
  pass
f = open(listFname, "a")
f.write("    \"msin\": [\n")

listLen = len(dirListSorted) - 1
for item in dirListSorted:
  f.write("        {\n")
  f.write("            \"class\": \"Directory\",\n")
  f.write("        ")
  f.write("    \"path\": \"./")
  f.write(item)
  f.write("\"\n")
  if dirListSorted.index(item) == listLen:
    f.write("        }\n")
  else:
    f.write("        },\n")
f.write("    ]")
f.close()

print ("Done. Check " + listFname + " file.")