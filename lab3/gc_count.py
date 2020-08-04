f=input("enter file name")
file = open(f, "r") 
n=file.readlines()
#print(n)
l1=[]
l2=[]
i=0
while(i!=len(n)) :
	l=n[i]
	#print(l)
	if(l[0]=='>'):
		l1.append(l)
		i+=1
		m=n[i]
		#print(m)
		str1=""
		while(m[0]!='>'):
			if(i<(len(n)-1)):
				str1+=m
				i+=1
				#print(str1)
				m=n[i]
			else:
				str1+=m
				break
		l2.append(str1)	
	else:
		i+=1
	#print(l1,l2)
l3=[]
for i in range(len(l2)):
	c=l2[i].count("C")
	g=l2[i].count("G")
	a=l2[i].count("A")
	t=l2[i].count("T")
	s=c+g+a+t
	s1=c+g
	p=(s1/s)*100
	l3.append(p)
max1=max(l3)
ind=l3.index(max1)
r=l1[ind]
r=r.lstrip('>')
print(r,'%.6f'%max1)
file.close()
