import os
import csv
import shutil 


fileTrain = csv.reader(open("trainLabels.csv"),dialect='excel', delimiter=",")
fileTrain.next()
fileLabes = open("labels.csv","w")
for i in fileTrain:
	print i[0],i[1]
	if not os.path.exists("dataset/"+i[1]):
		os.mkdir("dataset/"+i[1])
	shutil.copy2("train/"+i[0]+".png","dataset/"+i[1]+"/"+i[0]+".jpg")
	fileLabes.write(i[1]+"\n")
fileLabes.close()
