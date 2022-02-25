
inp = input("enter the input:\n ")
raw = inp.split("#")
for i in range(len(raw)):
    raw[i]=raw[i].split(" ")
rx = raw[0]
ry = raw[1]
x = [ ]
y =[ ]
for i in rx:
    x.append(int(i))
for i in ry:
    y.append(int(i))
print("x = ",x)
print("y = ",y)

