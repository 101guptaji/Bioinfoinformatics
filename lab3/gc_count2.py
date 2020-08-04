f = open('rosalind_gc.txt', 'r')

max_name, max_gc = '', 0

l = f.readline().rstrip()
while l:
    name, value = l[1:], ''
    l = f.readline().rstrip()
    while not l.startswith('>') and l:
        value = value + l
        l = f.readline().rstrip()
    gc = (value.count('C') + value.count('G'))/float(len(value))
    if gc > max_gc:
        max_name, max_gc = name, gc

print(max_name,'\n%.6f'%(max_gc*100))
f.close()
