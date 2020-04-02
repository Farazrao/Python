from functools import reduce
nums=[2,3,4,6,8,4,5,1,2,8]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)
doubles=list(map(lambda n:n*2,nums))
print(doubles)
sum=reduce(lambda a,b:a+b,nums)
print(sum)