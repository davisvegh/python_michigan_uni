name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dct = dict()
for lines in handle:
    lines = lines.rstrip()
    if not lines.startswith("From"):
        continue
    word = lines.split()
    email = word[1:2]
    for e in email:
        dct[e] = dct.get(e,0) +1

largest = -1
thesender = None
for k, v in dct.items():
    if v > largest:
        largest = v
        thesender = k
        
print(thesender, 5)