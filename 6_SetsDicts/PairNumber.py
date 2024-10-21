aws = []

while s:=input():
    aws += s.split()

ss = []
for ind in range(1, len(aws)):
    qq = sorted((aws[ind-1], aws[ind]))
    ss.append(''.join(qq)) 

print(len(set(ss)))
