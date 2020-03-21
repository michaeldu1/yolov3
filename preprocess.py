from os import listdir
from os.path import isfile, join

files_list = ["labels/" + f for f in listdir("labels") if isfile(join("labels", f))]
files_list = [f for f in listdir("labels") if isfile(join("labels", f))]

# Create gun.txt 
for filename in files_list:
    with open('gun.txt', 'a') as fout:
        fout.write("images/" + filename[0:-3] + "JPEG\n")
# for filepath in files_list:
#     with open(filepath, 'r') as fin:
#         data = fin.read().splitlines(True)
#         print(data)
    # with open(filepath, 'w+') as fout:
    #     for line in data[1:]:
    #         fout.write(line)
