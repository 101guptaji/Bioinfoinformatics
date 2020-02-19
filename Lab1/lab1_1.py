#naive algorithm fot string matching
f=open("ori.txt","r")
l = []
#Q-1
for line in f:
	print("Ans.1 length of the Cholerae ori",len(line))
#print(line)
for i in line:
	l.append(i)
#print(l)	
#print(len(l))

#Q-2
j=0
for i in range(len(l)):
	if (l[i]=='T'):
		if(l[i+1]=='G'):
			if(l[i+2]=='A'):
				if(l[i+3]=='T'):
					if(l[i+4]=='C'):
						if(l[i+5]=='A'):
							j+=1
	else:
		continue
print("Ans.2 number of times that the string Pattern = 'TGATCA' occurs in the string Text=",j)

#Q-3.1
s="GATCCAGATCCCCATAC"
t=[]
print("Ans.3.1  2-mer in GATCCAGATCCCCATAC are")
for i in s:
	t.append(i)
for i in range(len(t)-1):
	m=t[i]
	n=t[i+1]
	x=0
	for j in range(i+1,len(t)-1):
		if(t[j]==m):
			if(t[j+1]==n):
				x+=1
	if(x==2):
		print(m,n)

	
#Q3.2
s=input("enter text")
p=int(input("enter k"))
t=[]
for i in s:
	t.append(i)
#print(t)
str2=''
print("Ans.3.2",p,"-mer in text ",s,"are ")
for i in range(len(t)-p-1):
	x=[]
	for k in range(p):
		x.append(t[i+k])
	#print("x=",x)
	str1=''
	for ele in x:
		str1+=ele
	#print(str1)
	n=len(s)
	
	if( str1 in s[i+p:n]):
		if( str1 not in str2):
			print(str1)
			str2+=str1
	
f.close()
