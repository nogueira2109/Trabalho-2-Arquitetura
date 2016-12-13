import numpy as np
import sys
import os
from random import shuffle


_base = sys.argv[1]
_class = sys.argv[2]
#_baseName = sys.argv[3]
fileBase = open(_base,"r")
files = []
for i in fileBase:
	i = i.replace('\n','')
	i = i.replace('\r','')
	files.append(i)
fileBase.close()

labels = []
fileClass = open(_class,"r")
for i in fileClass:
	i = i.replace('\n','')
	i = i.replace('\r','')
	labels.append(i)
fileClass.close()


aux = []
auxFiles = []
labelsID = []
data = []
for i in xrange(0,len(labels)):
	if not labels[i] in aux:
		aux2 = []
		aux.append(labels[i])
		auxFiles.append(labels[i])
		aux2.append(labels[i])
		aux2.append(files[i])
		data.append(aux2)	
	else:
		idx = aux.index(labels[i])
		data[idx].append(files[i])
		
	idx = aux.index(labels[i])
	labelsID.append(idx)




if(not os.path.isdir("folds/")):
	os.mkdir("folds/")


for i in xrange(0,5):
	if(not os.path.isdir("folds/fold-"+str(i))):
		os.mkdir("folds/fold-"+str(i))
	for j in xrange(0,10):
		temp = data[j]
		shuffle(temp)
		train = temp[0:3000]
		test = temp[3001:4000]
		vali = temp[4001:]
		_kFile = open("folds/fold-"+str(i)+"/Training.dat","a+")
		for x in train:
			_kFile.write("/dados/CIFAR-10/"+x+" "+str(j)+'\n')		

		_kFile.close()

		_kFile = open("folds/fold-"+str(i)+"/Test.dat","a+")
		for x in test:
			_kFile.write("/dados/CIFAR-10/"+x+" "+str(j)+'\n')		

		_kFile.close()

		_kFile = open("folds/fold-"+str(i)+"/Validation.dat","a+")
		for x in vali:
			_kFile.write("/dados/CIFAR-10/"+x+" "+str(j)+'\n')		

		_kFile.close()
		#print data[j][i*1000:(i+1)*1000]
		print len(vali)
		print "--------------"
exit()


"""
for train, test in skf.split(X, labelsID):
	print len(train),len(test)

	if(not os.path.isdir("folds/"+_baseName+"/fold-"+str(cont))):
		os.mkdir("folds/"+_baseName+"/fold-"+str(cont))
	_kFile = open("folds/"+_baseName+"/fold-"+str(cont)+"/Training.dat","w+")	
	for idx in train:
		_kFile.write('/dados/CIFAR-10/train/'+str(idx+1)+'.png '+str(labelsID[idx])+'\n')
	_kFile.close()

	_kFile = open("folds/"+_baseName+"/fold-"+str(cont)+"/Test.dat","w+")	
	for idx in test:
		_kFile.write('/dados/CIFAR-10/train/'+str(idx+1)+'.png '+str(labelsID[idx])+'\n')
	_kFile.close()

	cont += 1
"""