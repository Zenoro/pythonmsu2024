xlist, ylist, zlist = [], [], []
while s:=input():
    x,y,z = map(float, s.split(','))
    xlist.append(x); ylist.append(y); zlist.append(z)

print(abs(max(xlist) - min(xlist)) *
      abs(max(ylist) - min(ylist)) *
      abs(max(zlist) - min(zlist)))
