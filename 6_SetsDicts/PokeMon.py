from collections import defaultdict

playersNcolod = defaultdict(list)
colodNcards = defaultdict(list)

# sort input into players and card sets
while s := input():
    s = s.split(' / ')
    if s[0].isdigit():
        colodNcards[s[0]].append(s[1])
    else:
        playersNcolod[s[0]].append(s[1])

# counting cards quantity for each players
for key in playersNcolod:
    lencards = []
    for numcolod in playersNcolod[key]:
        lencards += colodNcards[numcolod]
    playersNcolod[key] = len(set(lencards))
# print(playersNcolod)

# find maximum
resValue = max(playersNcolod.values())
resNames = list()
for name in playersNcolod:
    if playersNcolod[name] == resValue:
        resNames.append(name)

#output
resNames.sort()

print('\n'.join(resNames))
