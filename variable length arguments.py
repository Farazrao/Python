def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('faraz',age=24, city='chemnitz', mob= 3986548)