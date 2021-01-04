import re

file = "/home/zam/jupyters/dummy/data/train.csv"

data = open(file, "r").read()

data = re.sub("","",data)

print(data[0:1024])
# open("train-clean.csv", "w").write(data)