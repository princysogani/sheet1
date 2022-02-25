d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
name1 = d['Name']
sub1 = d['Subject']
ratings1 = d['Ratings']
inp = input("input: ")
x = []
y = []
z = []
count = sub1.count(inp)
for i in range(count):
    j = sub1.index(inp)
    x.append(name1[j])
    y.append(sub1[j])
    z.append(ratings1[j])
    del name1[j]
    del sub1[j]
    del ratings1[j]
newData = dict()
newData['Name'] = x
newData['Subject'] = y
newData['Ratings'] = z
print(newData)
