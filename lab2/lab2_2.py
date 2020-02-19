a=input("enter string A ")
b=input("enter search string B ")
c=input("enter search string C ")
t=list(a)
p1=list(b)
p2=list(c)

tl=len(t)
l1=[]
l2=[]
def kmpsearch(t,p1,l1):
	pl=len(p1)
	#lps construction
	lps=[]
	for i in range(pl):
		lps.append(0)
	j=0
	i=1
	while(i<pl):
		if(p1[i]==p1[j]):
			j+=1
			lps[i]=j
			i+=1
		else:
			if(j!=0):
				j=lps[j-1]
				#j-=1
			else:
				lps[i]=0
				i+=1
	print("lps=",lps)

	#kmp string matching
	j=0
	i=0
	while(i<tl):
		if(p1[j]==t[i]):
			i+=1
			j+=1
		if(j==pl):
			l1.append(i-j)
			j=lps[j-1]
		elif(i<tl and p1[j]!=t[i]):
			if(j!=0):				
				j=lps[j-1]
			else:
				i+=1

kmpsearch(a,b,l1)
kmpsearch(a,c,l2)
print(l1,l2)
bl=len(b)
cl=len(c)
lap=0
for i in l1:
	for j in l2:
		if(j<(i+bl) and j>(i-cl)):
			lap=1
		if(lap==1):
			break
	if(lap==1):
		break
if (lap == 1):
    print("Yes, SearchString",b," and SearchString",c," overlap in String",a)
else:
    print("No, SearchString",b," and SearchString",c," do not overlap in String",a)

#complexity=Big'O(len(A)+Max(len(B),len(C))+occurances of string B in String A * occurance of string C in String A)
