import os
import sys
import json

input_dir = sys.argv[1]
input_dir_path = input_dir+"/"
clusters = os.listdir(input_dir_path)
dict_arr = []
for c in clusters:
    input_path = input_dir_path+c
    for file in os.listdir(input_path):
        dict_arr.append({
            "subtype": c,
            "id": file[:-6]
        })

with open("../metadata/"+input_dir+".json", "w") as outfile:  
    json.dump(dict_arr, outfile)


