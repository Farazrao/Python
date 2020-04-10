names = ("rao","faraz","shakeel")
comps = ("dell","master","father")
# list form also
zipped = list(zip(names,comps))
print(zipped)
# zipped = dict(zip(names,comps))
# print(zipped)

# list format
for (a,b) in zipped:
    print(a,b)