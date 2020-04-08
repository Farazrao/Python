def topten():
    n=1
    while n<=10:
        sq=n*n
        # yield is a keyword to convert a function into geerators
        yield sq
        n+=1
values=topten()
for i in values:
    print(i)