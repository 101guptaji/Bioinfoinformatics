s=input("enter text")
p=input("enter pattern")
t=[]
p1=[]
for i in s:
	t.append(i)
print(t)
for i in p:
	p1.append(i)
print(p1)
pl=len(p1)
tl=len(t)

for i in range(pl-1,0):
	if(t[i]==p1[i]):
		continue
				
	else:
		b=t[i]
		k=i-1
		while(k>0):
			if(b==p1[k]):	

'''
str2=''
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
			print(str1,"found")
			
'''
