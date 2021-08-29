import os
import re

path = r"D:\\Programming\\Algo Expert"

filenames = []
bad = ["Easy", "Medium", "Hard", "Very Hard"]

with open("filenames.txt", "r") as file:
    badNames = file.readlines()

    for name in badNames:
        name = name.strip()

        if name not in bad:
            new_name = name[3:-4]
            filenames.append(new_name.strip())


path_files = set()
pattern = r"[a-zA-Z\s]+.mp4$"

for f in os.listdir(path):
    if os.path.isdir(os.path.join(path, f)):
        for f2 in os.listdir(os.path.join(path, f)):
            res = re.search(pattern, f2)
            if res:
                s, e = res.span()
                path_files.add(f2[s:e].strip()[:-4])

    res = re.search(pattern, f)
    if res:
        s, e = res.span()
        path_files.add(f[s:e].strip()[:-4])


for filename in filenames:
    if filename not in path_files:
        print(filename)
