

def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("The sum is: ", a+b)



def add(a, b):
 
    return a + b


print(add(5, 10))


# *args
# **kwargs


def total(*nums):
    return sum(nums)

print(total(1,2,5,6,8,4))


def student(**kwargs):
    print(kwargs)


student(name = "abc", age = 20, id = 1234)
