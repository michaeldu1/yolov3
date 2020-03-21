from os import listdir
from os.path import isfile, join
import cv2

files_list = ["labels/" + f for f in listdir("labels") if isfile(join("labels", f))]
# files_list = [f for f in listdir("labels") if isfile(join("labels", f))]

# Create gun.txt 
# for filename in files_list:
#     with open('gun.txt', 'a') as fout:
#         fout.write("images/" + filename[0:-3] + "JPEG\n")

# for filepath in files_list:
#     with open(filepath, 'r') as fin:
#         data = fin.read().splitlines(True)
#         print(data)
    # with open(filepath, 'w+') as fout:
    #     for line in data:
    #         print("0 " + line)
    #         fout.write("0 " + line)

# normalize 
for filepath in files_list:
    print("images/" + filepath[7:-3] + "JPEG")
    im = cv2.imread("images/" + filepath[7:-3] + "JPEG")
    height, width, _ = im.shape
    with open(filepath, 'r') as fin:
        data = fin.read().splitlines(True)
        for i in range(len(data)):
            # data[i] = 
            res = ""
            for j in range(1, len(data[i][:-1].split())):
                if j % 2 == 0:
                    norm = int(data[i][:-1].split()[j])/width
                else:
                    norm = int(data[i][:-1].split()[j])/height
                res += str(norm) + " "
            data[i] = res.strip()+"\n"
            # print(data[i][:-1].split())

    with open(filepath, 'w+') as fout:
        for line in data:
            print("0 " + line)
            fout.write("0 " + line)
