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
file = open(list_fname, "a")
file.write("    \"msin\": [\n")

list_len = len(dir_list_sorted) - 1
for item in dir_list_sorted:
  file.write("        {\n")
  file.write("            \"class\": \"Directory\",\n")
  file.write("        ")
  file.write("    \"path\": \"./")
  file.write(item)
  file.write("\"\n")
  if dir_list_sorted.index(item) == list_len:
    file.write("        }\n")
  else:
    file.write("        },\n")
file.write("    ]")
file.close()

print(f'Done. Check {list_fname} file.')
