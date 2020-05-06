# def greeting(name):
#     print('Hello',name)

# # print(greeting('Ömer'))
# # print(greeting)

# sayHello = greeting # adres kopyalama işlemi olur

# # print(sayHello)
# # print(greeting)

# del greeting # adresi daha önceden sayHello ya kopyaladık sayHello silinmez

# sayHello('ali')

# encapsulation
# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)

# outer(10)

def factorial(num):
    def inner_factorial(num):
        if num <=1:
            return 1
        return num * inner_factorial(num -1)
    return inner_factorial(num)

print(factorial(5))