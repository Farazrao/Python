a=5
b=2
# handling using keyword try
try:
    print("resource open")
    print(a/b)
    k=int(input("enter he number"))
    print(k)
    # exception hanlding
except ZeroDivisionError as e:
    print("heloo1")
except ValueError as e:
    print("hello2")
except Exception as e:
    print("hello3")
finally:
    print("resource colsed")