fst = int(input())
counter, max_counter = 1, 1
while s:=int(input()):
    if s >= fst:
        counter += 1
    else:
        max_counter = max(max_counter, counter)
        counter = 1
    fst = s

print(max(max_counter, counter))
