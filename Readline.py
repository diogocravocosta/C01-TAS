import numpy as np
import math

f = open("first.txt", "r")
#print(f.read()) 


content = f.readlines() 

#print("r")
#print(content[2])
line = content[2]
xval = line[2:15]
print(xval)