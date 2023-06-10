

import numpy as np
files=["tmp.pp_K001_B116au-ti.cube_nohead",
       "tmp.pp_K001_B117au-ti.cube_nohead"]
with open("input.txt","r") as f:
    files=f.read().splitlines()
sum=0
for file in files:
    print(file)
    a=np.loadtxt(file)
    sum =sum +a
average = sum / float(len(files))

np.savetxt("average_files.cube",average)
