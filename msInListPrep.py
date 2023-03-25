# Prepare MSs list for .json files for LINC >= 4
# Place this script in main MS folder. No other folders than MSs should be there

import os
root_MS_folder ='./'
list_fname = "MSlist.txt"

dir_list = [ item for item in os.listdir(root_MS_folder ) if os.path.isdir(os.path.join(root_MS_folder , item)) ]
dir_list_sorted = sorted(dir_list)

try:
  os.remove(list_fname)
except OSError:
  pass
f = open(list_fname, "a")
f.write("    \"msin\": [\n")

list_len = len(dir_list_sorted) - 1
for item in dir_list_sorted:
  f.write("        {\n")
  f.write("            \"class\": \"Directory\",\n")
  f.write("        ")
  f.write("    \"path\": \"./")
  f.write(item)
  f.write("\"\n")
  if dir_list_sorted.index(item) == list_len:
    f.write("        }\n")
  else:
    f.write("        },\n")
f.write("    ]")
f.close()

print ("Done. Check " + list_fname + " file.")
