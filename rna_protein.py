n=input()
#file = open(f, "r") 
#n=file.read()
d={"GGU":"G","GGC":"G","GGA":"G","GGG":"G",
"GAU":"D","GAC":"D","GAA":"E","GAG":"E",
"GCU":"A","GCC":"A","GCA":"A","GCG":"A",
"GUU":"V","GUC":"V","GUA":"V","GUG":"V",
"UUU":"F","UUC":"F","UUA":"L","UUG":"L",
"UCU":"S","UCC":"S","UCA":"S","UCG":"S",
"UAU":"Y","UAC":"Y","UAA":"\0","UAG":"\0",
"UGU":"C","UGC":"C","UGA":"\0","UGG":"W",
"CUU":"L","CUC":"L","CUA":"L","CUG":"L",
"CCU":"P","CCC":"P","CCA":"P","CCG":"P",
"CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",
"CGU":"R","CGC":"R","CGA":"R","CGG":"R",
"AUU":"I","AUC":"I","AUA":"I","AUG":"M",
"ACU":"T","ACC":"T","ACA":"T","ACG":"T",
"AAU":"N","AAC":"N","AAA":"K","AAG":"K",
"AGA":"R","AGG":"R","AGU":"S","AGC":"S"
}
#replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace(x).replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace().replace()
#str1=n.replace("GGU","G").replace("GGC","G").replace("GGA","G").replace("GGG","G").replace("GAU","D").
l=len(d)
str1=""
for i in range(0,len(n),3):
	a1=n[i:i+3]
	if(a1=="UAA" or a1=="UAG" or a1=="UGA"):
		break
	else:
		str1+=d[a1]
print(str1)
