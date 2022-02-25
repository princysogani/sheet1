n = int(input("enter an integer: ")
def gnrtfunc():
    for i in range(0,n):
        if i%7==0:
            yield i
        else:
            break
values = gnrtfunc()
print(values)
print(next(values))

for i in values:
    print(i)
        
