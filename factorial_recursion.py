def update(n):
    if n==0:
        return 1
    return n*update(n-1)
result=update(5)
print(result)