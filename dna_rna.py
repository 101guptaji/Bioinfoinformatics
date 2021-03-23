# dna to RNA string 
f=input()
file = open(f, "r") 
n=file.read()
str1=n.replace("T","U")
print(str1)
