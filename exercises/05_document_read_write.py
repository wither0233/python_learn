# count 'itheima' in txt
with open(r"c:\users\zENITH\learn-python\text.txt",'r',encoding="utf_8") as f:
    lines = []
    for line in f:
        lines.append(line)
total = 0
for line in lines:
    total += line.count("itheima")
print(total)
