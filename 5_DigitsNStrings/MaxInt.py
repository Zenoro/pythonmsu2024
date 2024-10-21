maximum = []
while s:=input():
    s = s.split()
    for elem in s:
        if elem.startswith("+"):
            continue
        try:
            k = int(elem)
            maximum.append(k)
        except ValueError:
            continue
print(max(maximum)) if maximum else print(0)
