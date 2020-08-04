fname='hamming.txt' #input("file name")
fhand=open(fname,'r')
a1=fhand.readline()
a2=fhand.readline()
count=0
if(len(a1)==len(a2)):
	for i in range(len(a1)):
		if(a1[i]!=a2[i]):
			count+=1
else:
	print("input strings are of different length")
print(count)
