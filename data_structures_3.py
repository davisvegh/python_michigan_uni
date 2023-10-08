name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt.rtf"
handle = open(name)


dict = dict()
hourlist = []
for lines in handle:
    lines = lines.rstrip()
    if not lines.startswith("From "):
        continue
    words = lines.split()
    date = words[5:6]
    for hour in date:
        part = hour.split(":")
        if len(part) > 0:
            first = part[0]
            hourlist.append(first)
    hourlist.sort()

for hour in hourlist:
    dict[hour] = dict.get(hour, 0) +1

for k, v in dict.items():
    print(k, v)
